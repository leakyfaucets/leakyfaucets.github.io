import numpy as np
import time
import matplotlib.pyplot as plt

def preprocess(text) -> tuple[np.ndarray, dict, dict]:

    text = text.lower()
    text = text.replace('.', ' .')
    words = text.split(' ')
    word_to_id = {}
    id_to_word = {}
    for word in words:
        if word not in word_to_id:
            new_id = len(word_to_id)
            word_to_id[word] = new_id
            id_to_word[new_id] = word
    corpus = np.array([word_to_id[w] for w in words])

    return corpus, word_to_id, id_to_word

def create_contexts_target(corpus, window_size=1):

    target = []
    contexts = []
    for index in range(window_size, len(corpus) - window_size):
        target.append(corpus[index])
        contexts.append(np.concatenate((corpus[index - window_size: index], corpus[index + 1: index + window_size + 1])))

    return np.array(contexts), np.array(target)

def clip_grads(grads, max_norm):
    total_norm = 0
    for grad in grads:
        total_norm += np.sum(grad ** 2)
    total_norm = np.sqrt(total_norm)

    rate = max_norm / (total_norm + 1e-6)
    if rate < 1:
        for grad in grads:
            grad *= rate

def remove_duplicate(params, grads):
    '''
    将参数列表中重复的权重整合为1个，
    加上与该权重对应的梯度
    '''
    params, grads = params[:], grads[:]  # copy list

    while True:
        find_flg = False
        L = len(params)

        for i in range(0, L - 1):
            for j in range(i + 1, L):
                # 在共享权重的情况下
                if params[i] is params[j]:
                    grads[i] += grads[j]  # 加上梯度
                    find_flg = True
                    params.pop(j)
                    grads.pop(j)
                # 在作为转置矩阵共享权重的情况下（weight tying）
                elif params[i].ndim == 2 and params[j].ndim == 2 and \
                     params[i].T.shape == params[j].shape and np.all(params[i].T == params[j]):
                    grads[i] += grads[j].T
                    find_flg = True
                    params.pop(j)
                    grads.pop(j)

                if find_flg: break
            if find_flg: break

        if not find_flg: break

    return params, grads

class Affine:

    def __init__(self, w: np.ndarray, b: np.ndarray | None = None):

        if b is None:
            b = np.zeros(w.shape[-1], dtype=w.dtype)
        self.params = [w, b]
        self.grads = [np.zeros_like(w), np.zeros_like(b)]

    def forward(self, x:np.ndarray) -> np.ndarray:

        w, b = self.params[0], self.params[1]
        self.x = x

        return np.dot(x, w) + b

    def backward(self, grad:np.ndarray) -> np.ndarray:

        w = self.params[0]
        self.grads[0][...] = np.dot(self.x.T, grad) # [...]取整个数组进行赋值，self.grads['w'] = ...只是更改绑定，没有修改原数组。
        self.grads[1][...] = np.sum(grad, axis=0) # 偏置在正向传播时进行了广播，反向传播时需要将梯度沿第零轴求和

        return np.dot(grad, w.T)


class SoftmaxWithLoss:

    def forward(self, x, t):

        self.t = t
        f = x - np.max(x, axis=-1, keepdims=True)
        exp = np.exp(f)
        exp_sum = np.sum(exp, axis=-1, keepdims=True)
        self.y = exp / exp_sum
        g = f - np.log(exp_sum)

        return -np.sum(t * g) / x.shape[0]

    def backward(self, dout=1):

        return dout * (self.y - self.t) / self.y.shape[0]

class SimpleCBOW:

    def __init__(self, vocab_size, hidden_size):

        w_in = 0.01 * np.random.randn(vocab_size, hidden_size).astype(np.float16)
        w_out = 0.01 * np.random.randn(hidden_size, vocab_size).astype(np.float16)
        
        self.input_layer_0 = Affine(w_in)
        self.input_layer_1 = Affine(w_in)
        self.output_layer = Affine(w_out)
        self.loss_layer = SoftmaxWithLoss()
        self.word_vecs = w_in

        self.params, self.grads = [], []
        for layer in [self.input_layer_0, self.input_layer_1, self.output_layer]:
            self.params += layer.params
            self.grads += layer.grads

    def forward(self, contexts, target):
        
        h_0 = self.input_layer_0.forward(contexts[:, 0])
        h_1 = self.input_layer_1.forward(contexts[:, 1])
        score = self.output_layer.forward((h_0 + h_1) / 2)
        loss = self.loss_layer.forward(score, target)

        return loss

    def backward(self, grad_0=1):

        grad_1 = self.loss_layer.backward(grad_0)
        grad_2 = self.output_layer.backward(grad_1)
        self.input_layer_0.backward(0.5 * grad_2)
        self.input_layer_1.backward(0.5 * grad_2)

class Adam:

    def __init__(self, lr=0.001, beta_1=0.9, beta_2=0.999):
        
        self.lr = lr
        self.beta_1 = beta_1
        self.beta_2 = beta_2
        self.t = 0

    def update(self, params, grads):

        if self.t == 0:
            self.m = self.v = [np.zeros_like(p, dtype=np.float16) for p in params]
        
        self.t += 1
        denom_1 = 1 - self.beta_1 ** self.t
        denom_2 = 1 - self.beta_2 ** self.t
        
        for i in range(len(params)):
            self.m[i] = self.beta_1 * self.m[i] + (1 - self.beta_1) * grads[i]
            self.v[i] = self.beta_2 * self.v[i] + (1 - self.beta_2) * np.square(grads[i])
            m_hat = self.m[i] / denom_1
            v_hat = self.v[i] / denom_2
            params[i] -= self.lr * m_hat / (np.sqrt(v_hat) + 1e-8)

class Trainer:
    def __init__(self, model, optimizer):
        self.model = model
        self.optimizer = optimizer
        self.loss_list = []
        self.eval_interval = None
        self.current_epoch = 0

    def fit(self, x, t, max_epoch=10, batch_size=32, max_grad=None, eval_interval=20):
        data_size = len(x)
        max_iters = data_size // batch_size
        self.eval_interval = eval_interval
        model, optimizer = self.model, self.optimizer
        total_loss = 0
        loss_count = 0

        start_time = time.time()
        for epoch in range(max_epoch):
            # 打乱
            idx = np.random.permutation(np.arange(data_size))
            x = x[idx]
            t = t[idx]

            for iters in range(max_iters):
                batch_x = x[iters*batch_size:(iters+1)*batch_size]
                batch_t = t[iters*batch_size:(iters+1)*batch_size]

                # 计算梯度，更新参数
                loss = model.forward(batch_x, batch_t)
                model.backward()
                params, grads = remove_duplicate(model.params, model.grads)  # 将共享的权重整合为1个
                if max_grad is not None:
                    clip_grads(grads, max_grad)
                optimizer.update(params, grads)
                total_loss += loss
                loss_count += 1

                # 评价
                if (eval_interval is not None) and (iters % eval_interval) == 0:
                    avg_loss = total_loss / loss_count
                    elapsed_time = time.time() - start_time
                    print('| epoch %d |  iter %d / %d | time %d[s] | loss %.2f'
                          % (self.current_epoch + 1, iters + 1, max_iters, elapsed_time, avg_loss))
                    self.loss_list.append(float(avg_loss))
                    total_loss, loss_count = 0, 0

            self.current_epoch += 1

    def plot(self, ylim=None):
        x = np.arange(len(self.loss_list))
        if ylim is not None:
            plt.ylim(*ylim)
        plt.plot(x, self.loss_list, label='train')
        plt.xlabel('iterations (x' + str(self.eval_interval) + ')')
        plt.ylabel('loss')
        plt.show()

window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

text = 'You say goodbye and I say hello.'

corpus, word_to_id, id_to_word = preprocess(text)
vocab_size = len(word_to_id)
contexts, target = create_contexts_target(corpus, window_size)
contexts = np.eye(vocab_size)[contexts]
target = np.eye(vocab_size)[target]
model = SimpleCBOW(vocab_size, hidden_size)
optimizer = Adam()
trainer = Trainer(model, optimizer)
trainer.fit(contexts, target, max_epoch, batch_size)
trainer.plot()
word_vecs = model.word_vecs
for word_id, word in id_to_word.items():
    print(word, word_vecs[word_id])