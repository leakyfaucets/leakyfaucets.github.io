50%：期末大作业 50%：一人讲一篇文章，线性代数相关，可结合语言（最好）、计算机等。
## 行列式
### 二阶和三阶行列式

**二阶行列式**：四个数$a_{11}, a_{12}, a_{21}, a_{22}$排成两行两列，两边加竖线，称为二阶行列式。它表示一个数，其定义式为
$$
\begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix}
=a_{11}a_{22}-a_{12}a_{21}
$$
，其中$a_{ij}$称为元素，$i$为行数，$j$为列数；从左上到右下为主对角线，从左下到右上为次对角线/副对角线。

**三阶行列式**：九个数排成三行三列，两边加竖线，称为三阶行列式。它表示一个数，其定义式为
$$
\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}
=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}-a_{11}a_{23}a_{32}
$$
，式中每一项的三个数都在不同行和不同列。

上三角形行列式：主对角线左下方的元素均为0，如
$$
\begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
0 & a_{22} & a_{23} \\
0 & 0 & a_{33}
\end{vmatrix}
=a_{11}a_{22}a_{33}
$$
，该行列式等于主对角线元素的乘积。

下三角形行列式：主对角线右上方的元素均为0，如
$$
\begin{vmatrix}
a_{11} & 0 & 0 \\
a_{21} & a_{22} & 0 \\
a_{31} & a_{32} & a_{33}
\end{vmatrix}
=a_{11}a_{22}a_{33}
$$
，该行列式等于主对角线元素的乘积。

对角形行列式：主对角线右上方和左下方的元素均为0，如
$$
\begin{vmatrix}
a_{11} & 0 & 0 \\
0 & a_{22} & 0 \\
0 & 0 & a_{33}
\end{vmatrix}
=a_{11}a_{22}a_{33}
$$
，该行列式等于主对角线元素的乘积。
### 排列

**$n$级排列**：由$1,2,\dots,n$组成的有序数组称作$n$级排列。

$n$级标准排列：在$n$级排列$i_1i_2\cdots i_n$中，$i_1<i_2<\cdots<i_n$，则称该排列为$n$级标准排列。

**逆序**：在$n$级排列$i_1i_2\cdots i_n$中，如果较大的数$i_s$排在较小的数$i_t$的前面，则称$i_s$与$i_t$构成一个逆序。

**逆序数**：$n$级排列$i_1i_2\cdots i_n$的逆序数为该排列的逆序个数，记为$N(i_1i_2\cdots i_n)$。如$N(6471325)=13$，先看6后面比它小的数有5个，再看4前面比它小的数有3个，7前面有4个，1前面没有，3前面有1个，2前面没有，加起来为13。

**奇排列**：逆序数为奇数的排列。

**偶排列**：逆序数为偶数的排列。

例题：若6级排列$4k52t1$是奇排列，则$k=\_\_,t=\_\_$。

首先由$4k52t1$是6级排列可得到$k=3,t=6$或$k=6,t=3$，把这两种情况均计算一遍即可得到答案。

**对换**：在一个$n$级排列中，互换某两个数的位置，其余数不变，可得到另一个排列。这样的变换称为对换。

**定理1.1**：一个排列经过一次对换后，奇偶性改变。

证明：对于一个排列中相邻的数所进行的对换，该对换只会让逆序数+1或-1，因此在这种情况下排列的奇偶性改变。对于不相邻数所进行的对换，可以转换成$2k+1$次相邻数的对换，因此在这种情况下排列的奇偶性也会改变。如1234变为4231要进行5次对换，$1234\to1243\to1423\to4123\to4213\to4231$，$k$为两数之间的数的数量。

**定理1.2**：$n$级排列共有$n!$个，其中奇排列和偶排列各占一半，各为$\frac{n!}{2}(n\geq2)$个。
### n阶行列式

从3阶行列式公式$a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}-a_{11}a_{23}a_{32}$可得：行标均为$3$级标准排列；列标取排列的所有可能，共有$3!=6$种；每项前的正负号由该项列排列的奇偶性决定，偶排列为正号，奇排列为负号。

定义1（按行展开）：
$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
=\sum_{j_1j_2\cdots j_n}(-1)^{N(j_1j_2\cdots j_n)}a_{1j_1}a_{2j_2}\cdots a_{nj_n}
$$
说明：
1. 行标为$n$级标准排列；
2. 列标取$j_1,j_2,\dots,j_n$的所有可能排列，共$n!$种；
3. $(-1)^{N(j_1j_2\cdots j_n)}$体现了偶排列为正号，奇排列为负号。

定义2（按列展开）：
$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
=\sum_{i_1i_2\cdots i_n}(-1)^{N(i_1i_2\cdots i_n)}a_{i_1 1}a_{i_2 2}\cdots a_{i_n n}
$$
说明：
1. 列标为$n$级标准排列；
2. 行标取$i_1,i_2,\dots,i_n$的所有可能排列，共$n!$种；
3. $(-1)^{N(i_1 i_2\cdots i_n)}$体现了偶排列为正号，奇排列为负号。

定义3（通式）：
$$
\begin{vmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \cdots & a_{nn}
\end{vmatrix}
=\sum_{i_1i_2\cdots i_n\&j_1j_2\cdots j_n}(-1)^{N(i_1i_2\cdots i_n)+N(j_1j_2\cdots j_n)}a_{i_1 j_1}a_{i_2 j_2}\cdots a_{i_n j_n}
$$
说明：
1. $(-1)^{N(i_1i_2\cdots i_n)+N(j_1j_2\cdots j_n)}$说明每一项的正负号由行标和列标的逆序数之和的奇偶性决定。

特殊行列式：
1. 若某行列式的某行或某列的元素均为0，则此行列式的值为0。
2. （主对角线为长边的）三角形行列式等于主对角线上元素的乘积。
3. 对于副对角线为长边的三角形行列式，其值等于副对角线上元素的乘积×$(-1)^\frac{n(n-1)}{2}$，其中$\frac{n(n-1)}{2}=N(n\;n-1\;\cdots\;1)$。

转置行列式：对于$n$阶行列式$D$，将其行列互换后得到其转置行列式，记为$D^\top$。行列式：determinant，转置：transpose v&n。

对称行列式：行列式关于主对角线“对称”，且主对角线上的元素全为0。如$\begin{vmatrix}0&2&6\\2&0&1\\6&1&0\end{vmatrix}$

反对称行列式：主对角线对称位置上的元素互为相反数，且主对角线上的元素全为0。**奇数阶反对称行列式的值为0**，如$\begin{vmatrix}0&2&6\\-2&0&1\\-6&-1&0\end{vmatrix}=0$
### 行列式的性质

1. 对任何行列式，有$D=D^\top$。
2. 交换某个行列式的两行/列，其值变为相反数。可利用排序对换奇偶性改变来证明。
	1. 推论：若行列式有两行/列的对应元素相等，则行列式值为零。可利用上述性质交换两行/列，其值变为相反数后不变，说明其值为零。
3. 用数$k$乘以行列式某一行/列的所有元素，等于用$k$乘以该行列式。
	1. 推论：若行列式某一行/列的所有元素有公因数，则该公因数可以提到行列式外面。$\begin{vmatrix}k&2k\\6&9\end{vmatrix}=3k\begin{vmatrix}1&2\\2&3\end{vmatrix}$
	2. 若行列式有两行/列的元素对应成比例，则此行列式值为零。
4. 若行列式的某一行/列的各元素都是两个数之和，则此行列式等于两个行列式之和，这两个行列式分别以这两个数之一作为所在行/列对应位置的元素，**其他位置的元素与原行列式相同**。如$\begin{vmatrix}1+2&2+3\\a&b\end{vmatrix}=\begin{vmatrix}1&2\\a&b\end{vmatrix}+\begin{vmatrix}2&3\\a&b\end{vmatrix}$
5. 将行列式的某一行/列的所有元素乘以同一数$k$后加到另一行/列对应位置的元素上，则行列式的值不变。利用性质4和推论3.2即可证明。
### 行列式按行/列展开

余子式：在$n(n>1)$阶行列式$D=|a_{ij}|$中，除元素$a_{ij}$所在行和列的所有元素以外的元素所构成的$n-1$阶行列式称为$D$中元素$a_{ij}$的余子式，记为$M_{ij}$，把$(-1)^{i+j}M_{ij}$称为元素$a_{ij}$的代数余子式，记为$A_{ij}$。

行列式按一行/列展开：$n$阶行列式$D=|a_{ij}|$等于它的任意一行/列的各元素与其对应的代数余子式乘积的和，即$$D=a_{i1}A_{i1}+a_{i2}A_{i2}+\cdots+a_{in}A_{in}(i=1,2,\cdots,n)$$（按第$i$行展开）。为了计算简便，一般优先按0多的行/列展开。如果没有，可以利用上一部分的性质5构造尽可能多的0。

**异乘变零定理**：$n$阶行列式$D=|a_{ij}|$的某一行/列的所有元素与另一行/列中对应元素的代数余子式乘积的和等于零，即$$a_{i1}A_{k1}+a_{i2}A_{k2}+\cdots+a_{in}A_{kn}=0,i\neq k$$
例题：设行列式$D=\begin{vmatrix}3&0&4&0\\3&2&2&2\\0&-7&0&0\\5&3&-2&2\end{vmatrix}$，求：（1）$A_{41}+A_{42}+A_{43}+A_{44}$；（2）$M_{41}+M_{42}+M_{43}+M_{44}$。

解：（1）$A_{41}+A_{42}+A_{43}+A_{44}=\begin{vmatrix}3&0&4&0\\3&2&2&2\\0&-7&0&0\\1&1&1&1\end{vmatrix}=(-7)\times(-1)^{3+2}\times\begin{vmatrix}3&4&0\\3&2&2\\1&1&1\end{vmatrix}=7\times\begin{vmatrix}3&4&0\\1&0&0\\1&1&1\end{vmatrix}=7\times(-1)^{3}\times\begin{vmatrix}4&0\\1&1\end{vmatrix}=-28$
（2）$M_{41}+M_{42}+M_{43}+M_{44}=-A_{41}+A_{42}-A_{43}+A_{44}=\begin{vmatrix}3&0&4&0\\3&2&2&2\\0&-7&0&0\\-1&1&-1&1\end{vmatrix}=\dots=-56$

$k$阶子式的余子式和代数余子式：在$n$阶行列式$D$中，任意选取$k$行和$k$列（$1\leq k\leq n$），位于这些行列交叉点处的$k^2$个元素，按照原来的相对位置所构成的$k$阶行列式$N$为$D$的一个$k$阶子式。在这些行列之外的元素，按照原来的相对位置所构成的$n-k$阶行列式$M$为$N$的余子式。$N$的代数余子式的正负性由所有行号和列号之和决定。

行列式按多行/列展开（拉普拉斯定理，Laplace theorem）：在$n$阶行列式$D$中，任意取定$k$行/列，则由这$k$行/列元素所能构成的所有$k$阶子式$N_1,N_2,\cdots,N_t(t=C_n^k)$与它们的对应代数余子式$A_1,A_2,\cdots,A_t$乘积之和等于行列式$D$的值，即$$D=N_1A_1+N_2A_2+\cdots+N_tA_t$$

推论：
$\begin{vmatrix}A&\mathbf{0}\\\mathbf{0}&B\end{vmatrix}=\begin{vmatrix}A&\mathbf{0}\\C&B\end{vmatrix}=\begin{vmatrix}A&C\\\mathbf{0}&B\end{vmatrix}=|A|\times|B|$，$\begin{vmatrix}\mathbf{0}&A\\B&\mathbf{0}\end{vmatrix}=\begin{vmatrix}\mathbf{0}&A\\B&C\end{vmatrix}=\begin{vmatrix}C&A\\B&\mathbf{0}\end{vmatrix}=(-1)^{mn}|A|\times|B|$，其中$A$的阶数为$m$，$B$的阶数为$n$。注意与三角形行列式中对角线与正负号的关系不同。

证明：
对于$\begin{vmatrix}A&\mathbf{0}\\C&B\end{vmatrix}$，其中$A$的阶数为$m$，$B$的阶数为$n$。根据拉普拉斯定理取前$m$行，则必须取$m$列。只有当取前$m$列时，子式才不会有元素全为0的列，因此有$\begin{vmatrix}A&\mathbf{0}\\C&B\end{vmatrix}=|A|\times(-1)^{2(1+2+3+\cdots+m)}|B|=|A|\times|B|$。
对于$\begin{vmatrix}\mathbf{0}&A\\B&C\end{vmatrix}$，其中$A$的阶数为$m$，$B$的阶数为$n$。根据拉普拉斯定理取前$m$行，则必须取$m$列。只有当取后$m$列时，子式才不会有元素全为0的列，因此有$\begin{vmatrix}\mathbf{0}&A\\B&C\end{vmatrix}=|A|\times(-1)^{1+2+\cdots+m+n+1+n+2+\cdots+n+m}|B|=(-1)^{mn}|A|\cdot|B|$。

行列式的乘法：
$\begin{vmatrix}1&2&3\\1&1&0\\0&0&5\end{vmatrix}\cdot\begin{vmatrix}0&1&1\\1&2&3\\1&1&-6\end{vmatrix}=\begin{vmatrix}1\times0+2\times1+3\times1&1\times1+2\times2+3\times1&1\times1+2\times3+3\times(-6)\\1\times0+1\times1+0\times1&1\times1+1\times2+0\times1&1\times1+1\times3+0\times(-6)\\\cdots&\cdots&\cdots\end{vmatrix}$
### 克莱姆法则 Cramer Rule

克莱姆法则：对于含有$n$个方程和$n$个未知数的$n$元线性方程组$\begin{cases}a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n=b_1\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n=b_2\\\cdots\\a_{n1}x_1+a_{n2}x_2+\cdots+a_{nn}x_n=b_n\end{cases}$，当其系数行列式$D=\begin{vmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{n1}&a_{n2}&\cdots&a_{nn}\end{vmatrix}\neq0$时，方程组有唯一解$x_1=\frac{D_1}{D},x_2=\frac{D_2}{D},\cdots,x_n=\frac{D_n}{D}$，其中$D_1=\begin{vmatrix}b_1&a_{12}&\cdots&a_{1n}\\b_2&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\b_n&a_{n2}&\cdots&a_{nn}\end{vmatrix}$，$D_2=\begin{vmatrix}a_{11}&b_1&\cdots&a_{1n}\\a_{21}&b_2&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{n1}&b_n&\cdots&a_{nn}\end{vmatrix}$，$\cdots$，$D_n=\begin{vmatrix}a_{b_1}&a_{12}&\cdots&b_1\\b_2&a_{22}&\cdots&b_2\\\vdots&\vdots&\ddots&\vdots\\b_n&a_{n2}&\cdots&b_n\end{vmatrix}$。

定理：对于含有$n$个方程和$n$个未知数的$n$元齐次（常数项均为0）线性方程组$\begin{cases}a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n=0\\a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n=0\\\cdots\\a_{n1}x_1+a_{n2}x_2+\cdots+a_{nn}x_n=0\end{cases}$，当系数行列式$D=\begin{vmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&\ddots&\vdots\\a_{n1}&a_{n2}&\cdots&a_{nn}\end{vmatrix}\neq0$，此方程组只有零解。

推论：（含有$n$个方程和$n$个未知数的）齐次线性方程组有非零解的充分必要条件是系数行列式的值为0；只有零解的充要条件是系数行列式的值为0。
## 矩阵

矩阵：$m\times n$个数$a_{ij}(i=1,2,\cdots,m;j=1,2,\cdots,n)$排成一个$m$行$n$列的数表，称为一个$m\times n$矩阵，$a_{ij}$称为元素。

同型矩阵：若矩阵$A$与矩阵$B$的行数和列数均相等，则称$A$与$B$为同型矩阵。

矩阵相等：若矩阵$A$与矩阵$B$为同型矩阵，且对应位置的元素相等，则$A=B$。

方阵：行数、列数相等的矩阵。一阶方阵就是一个数。只有方阵能称几阶，只有方阵有主对角线和次对角线。

行矩阵：只有一行的矩阵，即为行向量

列矩阵：只有一列的矩阵，即列行向量

零矩阵：元素全为0的矩阵，记为$O$。

负矩阵：将矩阵$A$的所有元素取相反数后得到的矩阵，叫做$A$的负矩阵，记为$-A$。

上三角形矩阵：主对角线下方的元素全为零的方阵。

上三角形矩阵：主对角线上方的元素全为零的方阵。

对角形矩阵：主对角线上、下方的元素全为零的方阵，也可记为$diag(a_1,a_2,\cdots,a_n)$。

数量矩阵：主对角线上的所有元素相等的对角形矩阵，即$diag(a,a,\cdots,a)$

单位矩阵：主对角线上的元素全为1，其他元素均为0的方阵。$n$阶单位矩阵$E=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}$
### 矩阵的运算

加法：只有**同型矩阵**能相加，将对应位置元素求和即可。

减法：只有**同型矩阵**能相减，将对应位置元素求差即可。

矩阵加/减法满足交换律、结合律。

数乘：数与矩阵相乘，将矩阵的每个元素乘以该数即可。

与行列式的区别：矩阵要提出所有元素的公因子，只需提一次即可。

矩阵数乘满足分配律、交换律和结合律。

矩阵乘法：只有当左边矩阵的列数等于右边矩阵的行数时，两个矩阵才能相乘，即对于矩阵$A_{j\times k}$和$B_{m\times n}$，只有当$k=m$时，两矩阵才可以相乘。方法：用左边矩阵的第一行分别乘以右边矩阵的每一列，得到乘积矩阵的第一行，依次进行下去得到乘积矩阵的所有行。因此，**乘积矩阵的行数等于左边矩阵的行数，列数等于右边矩阵的列数**，即$A_{i\times j}B_{j\times k}=(AB)_{i\times k}$。

注：
1. 矩阵乘法满足结合律、分配律：$BA-B=B(A-E)$
2. $AE=A$，$EA=A$，即单位矩阵在矩阵乘法中相当于数乘1。
3. $\begin{pmatrix}a_1&0&\cdots&0\\0&a_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&a_n\end{pmatrix}\begin{pmatrix}b_1&0&\cdots&0\\0&b_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&b_n\end{pmatrix}=\begin{pmatrix}a_1b_1&0&\cdots&0\\0&a_2b_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&a_nb_n\end{pmatrix}$

注意：
1. 矩阵乘法不满足交换律和消去律，即$AB=AC(A\neq O)$得不到$B=C$。
2. $AB=0$得不到$A=O$或$B=O$。

矩阵的可交换：若矩阵$A$，$B$满足$AB=BA$，则称$A$与$B$可交换，否则称为不可交换。

注：
1. 可交换的矩阵一定是同阶方阵。
2. 单位矩阵和任一同阶方阵可交换。
3. 两个同阶对角形矩阵可交换，可由上述式子3得到。

方阵的幂：对于方阵$A$和正整数$k$，$A$的$k$次幂定义为$$A^k=A\cdot A\cdot \cdots \cdot A $$，并规定$A^0=E$。

运算规律：
1. $A^mA^n=A^{m+n}$
2. $(A^m)^n=A^{mn}$
3. $(lA)^k=l^kA^k$

注意：
1. $(AB)^n=A^nB^n$，当且仅当$A$，$B$可交换时成立。
2. $(A+B)^2=A^2+AB+BA+B^2$，$(A-B)^2=A^2-AB-BA+B^2$
3. $(A+B)(A-B)=A^2-AB+BA-B^2$
4. 设$f(x)=x^2-2x+3$，则$f(A)=A^2-2A+3E$，注意常数项要乘$E$。
5. $A^3+B^3=(A+B)(A^2-AB+B^2)$，$A^3-B^3=(A-B)(A^2+AB+B^2)$
### 矩阵的转置

定义：将矩阵的各行依次变为列。

性质：
1. $(A^\top)^\top=A$
2. $(A\pm B)^\top=A^\top\pm B^\top$
3. $(kA)^\top=kA^\top$
4. $(AB)^\top=B^\top A^\top$，$(ABC)^\top=C^\top B^\top A^\top$，注意顺序发生了变化。
5. $(A^k)^\top=(A^\top)^k$

对称矩阵：矩阵中各元素关于主对角线对称，即$a_{ij}=a_{ji}$，此时$A^\top=A$。若$A^\top=-A$，即$a_{ij}=-a_{ji}$，则称该矩阵为反对称矩阵。

性质：
1. 若$A$，$B$为同阶对称矩阵，则$AB$为对称矩阵的充要条件是$AB=BA$。
2. 对任意矩阵$A$，$A^\top A$，$AA^\top$均为对称矩阵。
3. 若$A$为反对称矩阵，$k$为正整数，则当$k$为偶数时，$A^k$为对称矩阵；当$k$为奇数时，$A^k$为反对称矩阵。
### 方阵

方阵的行列式：对于$n$阶方阵$A$，其行列式$|A|$定义为与其各元素均相同的行列式。

性质：
1. $|A^\top|=|A|$
2. $|kA|=k^n|A|$
3. $|AB|=|A||B|$
4. $|A^m|=|A|^m$
5. $|E|=1$

方阵的伴随矩阵：按行求矩阵每个元素的代数余子式后按列放置形成伴随矩阵。对于$n$阶方阵$A$，其行列式$|A|$中元素$a_{ij}$的代数余子式为$A_{ij}$，则$A$的伴随矩阵$A^*$定义为$$A^*=\begin{pmatrix}A_{11}&A_{21}&\cdots&A_{n1}\\A_{12}&A_{22}&\cdots&A_{n2}\\\vdots&\vdots&\ddots&\vdots\\A_{1n}&A_{2n}&\cdots&A_{nn}\end{pmatrix}$$
性质：
1. $AA^*=A^*A=|A|E$
2. 若$A$为$n$阶方阵，则$|A^*|=|A|^{n-1}$
3. $(A^\top)^*=(A^*)^\top$
4. 若$A$为$n$阶方阵，$k$为常数，则$(kA)^*=k^{n-1}A^*$。提出来$k$是$n-1$次是因为余子式是$n-1$阶行列式
5. 对于二阶方阵$A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$，$A^*=\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$，即主对角线上的元素交换位置，副对角线上的元素变为相反数。
### 逆矩阵

方阵的逆矩阵：对于$n$阶方阵$A$，若存在$n$阶方阵$B$，使得$AB=BA=E$，则称$A$是可逆矩阵，$B$为$A$的逆矩阵，记为$A^{-1}$，即$A^{-1}=B$。

注意：不是所有方阵都是可逆矩阵。若方阵可逆，则该方阵的逆矩阵是唯一的。

定义：对于$n$阶方阵$A$，若$|A|\neq 0$，则称$A$是非奇异矩阵；若$|A|=0$，则称$A$是奇异矩阵。

定理：方阵可逆的充要条件是该方阵为非奇异矩阵（$|A|\neq 0$）。当$A$可逆时，$$A^{-1}=\frac{A^*}{|A|}$$，该求逆矩阵方法被称为伴随矩阵法。

推论1：对角形矩阵$A=\begin{pmatrix}a_1&0&\cdots&0\\0&a_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&a_n\end{pmatrix}$可逆的充要条件是$a_1,a_2,\cdots,a_n$均为0。当$A$可逆时，有$$A^{-1}=\begin{pmatrix}\frac{1}{a_1}&0&\cdots&0\\0&\frac{1}{a_2}&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&\frac{1}{a_n}\end{pmatrix}$$
推论2（定义的推广）：对于$n$阶方阵$A$，若存在$n$阶方阵$B$，使得$AB=E$或$BA=E$，则$A$可逆，且$A^{-1}=B$。

性质：
1. 
## 向量

定义：由$n$个数$a_1,a_2,a_3,\dots,a_n$组成的有序数组$\alpha=(a_1,a_2,a_3,\dots,a_n)$称为向量。其中数$a_i$叫做向量的第$i$个分量，$i=1,2,3,\dots,n$。分量的个数称为向量的维数。此时称向量$\alpha$为$n$维向量。

行向量、列向量：

零向量：所有分量为0的向量，记作$\mathbf{0}$，可以是行向量也可以是列向量，维度为n。

负向量：将某个向量的所有分量取负数所得到的向量。

向量的转置：

向量的相等：两个向量如果对应位置上的分量均相等，那么这两个向量相等。如果维数不相等，那么一定不相等。

向量的加减法：对应位置的分量相加减。

向量的数乘：设k为常数，则$k\alpha=(ka_1,ka_2,ka_3,\dots,ka_n)$。

向量的交换律：$\alpha+\beta=\beta+\alpha$

向量的结合律：$(\alpha+\beta)+\gamma=\alpha+(\beta+\gamma)$，$kl\alpha=k(l\alpha)=l(k\alpha)$

向量的分配律：$k(\alpha+\beta)=k\alpha+k\beta$，$(k+l)\alpha=k\alpha+l\alpha$

$\alpha+\mathbf{0}=\mathbf{0}+\alpha=\alpha$

$k\alpha=0\Leftrightarrow k=0或\alpha=\mathbf{0}$

### 向量的线性组合

定义：对于一组$n$维向量$\alpha_1,\alpha_2,\cdots,\alpha_m$和一组常数$k_1,k_2,\cdots,k_m$，称$k_1\alpha_1, k_2\alpha_2,\cdots,k_m\alpha_m$为该组向量的一个线性组合，该组常数称为组合系数。

定义：对于一组$n$维向量$\beta,\alpha_1,\alpha_2,\cdots,\alpha_m$和一组常数$k_1,k_2,\cdots,k_m$，如果有$\beta=k_1\alpha_1, k_2\alpha_2,\cdots,k_m\alpha_m$，则称$\beta$是$\alpha_1,\alpha_2,\cdots,\alpha_m$的线性组合，也可称$\beta$可由$\alpha_1,\alpha_2,\cdots,\alpha_m$线性表示。

性质：
1. 零向量是任意向量的线性组合
2. 向量组中的任意向量都可以由该向量组线性表示（其他向量系数取0即可）
3. 任何一个$n$维向量都可以由$n$维基本单位向量组（以三维为例，（1，0，0），（0，1，0），（0，0，1））线性表示，即$\alpha=a_1\varepsilon_1+a_2\varepsilon_2+\cdots+a_n\varepsilon_n$。

定义：对于向量组$\alpha_1,\alpha_2,\cdots,\alpha_n$和$\beta_1,\beta_2,\cdots,\beta_n$，若第一个向量组中的每个向量都可由第二个向量组线性表示，则称第一个向量组可由第二个向量组线性表示。若两个向量组能互相线性表示，则称两个向量组等价，记作$\alpha_1,\alpha_2,\cdots,\alpha_n\cong\beta_1,\beta_2,\cdots,\beta_n$

性质：
1. 等价具有传递性
2. 等价具有交换性
3. 一个向量组与其自身等价

向量组的线性相关性：对于$m$维向量组$\alpha_1,\alpha_2,\cdots,\alpha_n$，若存在不全为0的数组$k_1,k_2,\cdots,k_n$，使得$k_1\alpha_1, k_2\alpha_2,\cdots,k_n\alpha_n=0$，则称该向量组线性相关，该数组为该向量组的一组相关系数；否则称该向量组线性无关。

推论：
1. 含有零向量的向量组必定线性相关（零向量系数不为0，其他向量系数为0）
2. 向量组中有两个向量成比例，则该向量组必定线性相关。
3. 若某个向量线性相关，则该向量必为零向量；若某个向量线性无关，则该向量必不为零向量
4. 若$\alpha_1,\alpha_2,\cdots,\alpha_n$线性相关，则$\alpha_1,\alpha_2,\cdots,\alpha_n,\alpha_{n+1},\cdots,\alpha_{n+m}$也线性相关。（部分线性相关，则整体必定线性相关）
5. 4的逆否命题也成立：整体线性无关，则部分线性无关
6. 线性无关的向量组接长后仍是线性无关，线性相关的向量组截短后也线性相关。接长/截短指增加/减少向量的维数。
7. 