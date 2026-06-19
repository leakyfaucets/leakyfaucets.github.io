---
layout: post
title: "HTML学习笔记"
categories: [HTML, Web]
author:
- Frank Zhang
comments: true
# modified_date: 2026-06-11
---

本文为作者在学习[MDN学习区](https://developer.mozilla.org/zh-CN/docs/Learn_web_development)时的笔记。作者对结构进行了调整，并补充了一些说明和例子。本文同样遵循[CC-BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5)协议。

## 基础语法

以下是一些HTML的基础语法。

### 元素

HTML（HyperText Markup Language，超文本标记语言）文档由一系列的元素（element）组成。大部分元素由开始标签`<element_name>`、内容`content`和结束标签`</element_name>`组成，只有一个标签的元素被称作空元素（void element）。HTML没有要求在空元素的标签末尾添加/。当希望HTML是有效的XML时，可以这样做，如`<img src="images/cat.jpg" alt="猫"/>`。HTML中的标签不区分大小写。例如，`<title>`标签可以写成`<title>`、`<TITLE>`、`<Title>`、`<TiTlE>`等，但为了保持一致性和可读性，建议所有标签都用小写书写。

元素可以放置在其他元素内部，这被称为嵌套，如：`<p>我们的小猫脾气<strong>很</strong>暴躁。</p>`。标签必须以它们相互嵌套或分离的方式打开和关闭，元素重叠可能会导致错误。~~`<p>我们的小猫脾气<strong>很暴躁。</p></strong>`~~

### 属性

元素也可以有属性，属性位于标签内。一个属性应该有：

- 一个在它和元素名之间的空格。对于拥有多个属性的元素，属性之间用空格分隔。
- 属性名，后跟一个等号。
- 属性值，用一对引号包裹。多个属性值之间用分号加空格分隔。

例如：`<img src="<URL-OF-IMAGE>" alt="图像的描述" width="300" />`

**注意**：属性值可以用单引号或双引号包裹，但不能混合使用。若要在属性值内使用引号，可以使用不同类型的引号，也可以直接使用[字符引用](#字符引用)，如下面两种效果相同的写法：


```html
<p><a href="https://www.example.com" title='A link to "example".'>This is an example.</a></p>
<p><a href="https://www.example.com" title="A link to &quot;example&quot;.">This is an example.</a></p>
```

布尔属性（boolean attribute）是表示`true`或`false`值的属性。如果HTML标签包含布尔属性，无论该属性的值如何，该属性都会在该元素上设置为`true`。如果HTML标签不包含该属性，则该属性被设置为`false`。以布尔属性`checked`为例：


```html
<!-- 以下复选框在初始渲染时将被选中 -->
<input type="checkbox" checked />
<input type="checkbox" checked="" />
<input type="checkbox" checked="checked" />
<!-- 以下复选框在初始渲染时将不被选中 -->
<input type="checkbox" />
```

**注意**：要将属性设置为`false`，则该属性不应出现在元素标签中。尽管现代浏览器将任何字符串值视为`true`，但也不应该把值设为`true`。

### 字符引用

字符引用（character reference）用作替代HTML中的保留字符，还可用于无法在标准键盘上键入的不可见字符，包括不换行空格、从左到右和从右到左标记等控制字符。 

字符引用有三种类型：

- 命名字符引用：`&`+`name`+`;`。
- 十进制数字字符引用：`&#`+`decimal_unicode`。
- 十六进制数字字符引用：`%#x`或`%#X`+`hexadecimal_unicode`。

常见字符的命名引用见下方表格：

| 字符 | 字符名称 | 命名引用 |
|:---:|:---:|:---:|
| &amp; | ampersand | `&amp;` |
| &lt; | lesser than | `&lt;` |
| &gt; | greater than | `&gt;` |
| &quot; | double quotation mark | `&quot;` |
| &apos; | apostrophe | `&apos;` |
| &ndash; | narrow dash | `&ndash;` |
| &mdash; | middle dash | `&mdash;` |
| &copy; | copyright | `&copy;` |
| &reg; | registered | `&reg;` |
| &trade; | trademark | `&trade;` |
| &asymp; | approximately equal to | `&asymp;` |
| &ne; | not equal to | `&ne;` |
| &pound; | pound | `&pound;` |
| &euro; | euro | `&euro;` |
| &deg; | degree | `&deg;` |

### 注释

注释需要包裹在`<!--`和`-->`中。

### 列表

列表可以进行嵌套。

#### 无序列表

`<ul>`（unordered list）元素用于建立无序列表，其中需要用`<li>`（list item）元素把每个项目单独包裹起来。


```html
<ul>
  <li>豆浆</li>
  <li>油条</li>
  <li>豆汁</li>
  <li>焦圈</li>
</ul>
```

#### 有序列表

有序列表使用`<ol>`（ordered list）元素。


```html
<ol>
  <li>沿这条路走到头</li>
  <li>右转</li>
  <li>直行穿过第一个十字路口</li>
  <li>在第三个十字路口处左转</li>
  <li>继续走 300 米，学校就在你的右手边</li>
</ol>
```

#### 描述列表

`<dl>`（description list，描述列表）元素的目的是标记一组项目及其相关描述，如术语和定义或问题和答案。每一项都用`<dt>`（description term，描述术语）元素包裹。每个描述都用`<dd>`（description definition，描述定义）元素包裹，一个术语可以同时有多个描述。浏览器的默认样式会在描述列表的术语及其定义之间产生缩进。


```html
<dl>
  <dt>旁白</dt>
  <dd>
    戏剧中，为渲染幽默或戏剧性效果而进行的场景之外的补充注释念白，只面向观众，内容一般都是角色的感受、想法、以及一些背景信息等。
  </dd>
  <dd>
    写作中，指与当前主题相关的一段内容，通常不适于直接置于内容主线中，因此置于附近的其他位置（通常位于主线内容旁边一个文本框内）。
  </dd>
</dl>
```

### 表格

表格由`<table>`创建，其中允许的内容按顺序如下：

1. 零个或一个`<caption>`元素作为表格的标题。
2. 零个或多个`<colgroup>`元素。`<colgroup>`通常用于对列进行分组。如果某个列组需要相同的属性时，可直接使用一个`<colgroup>`的`span`属性；如果需要不同的属性时，可使用`<col>`子元素的`span`属性对组内的列进行精细控制。默认从首列开始设置属性，如需要从某列开始设置属性，需要将前面列的属性设为空。`span`属性指定了设置属性的列数（默认为1）。
3. 零个或一个`<thead>`元素，包住表格的列表头。
4. 零个或多个`<tbody>`元素，包住表格的主要部分。
5. 零个或一个`<tfoot>`元素，包住表格的列表尾。

表格的行由`<tr>`（table row）元素定义，行内的单元格由子元素`<td>`（table data）定义。表头由`<th>`（table header）元素定义，浏览器默认将其加粗。表头的`scope`属性定义了表头为行表头还是列表头，以便屏幕阅读器用户可以类似于视力正常的用户的操作来理解表格，允许的值有：

- col：该表头为列表头
- row：该表头为行表头
- colgroup：该表头为某一列组的表头
- rowgroup：该表头为某一行组的表头

`<td>`和`<th>`的`colspan`和`rowspan`属性可以改变它们的宽度或高度，如`colspan="2"`会使单元格横跨两列、`rowspan="2"`会使单元格横跨两行，下一行/列的单元格将会跳过该单元格。


```html
<table>
  <caption>2016年8月出售的物品</caption>
  <colgroup span="2" class="row header"></colgroup>
  <colgroup span="3" class="clothing"></colgroup>
  <colgroup span="2" class="jewelry"></colgroup>
  <thead>
    <tr>
      <th colspan="2"></th>
      <th colspan="3" scope="colgroup">衣物</th>
      <th colspan="2" scope="colgroup">饰品</th>
    </tr>
    <tr>
      <th colspan="2"></th>
      <th scope="col">长裤</th>
      <th scope="col">衬衫</th>
      <th scope="col">裙子</th>
      <th scope="col">手镯</th>
      <th scope="col">戒指</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" scope="rowgroup">比利时</th>
      <th scope="row">安特卫普</th>
      <td>56</td>
      <td>22</td>
      <td>43</td>
      <td>72</td>
      <td>23</td>
    </tr>
    <tr>
      <th scope="row">根特</th>
      <td>46</td>
      <td>18</td>
      <td>50</td>
      <td>61</td>
      <td>15</td>
    </tr>
    <tr>
      <th scope="row">布鲁塞尔</th>
      <td>51</td>
      <td>27</td>
      <td>38</td>
      <td>69</td>
      <td>28</td>
    </tr>
    <tr>
      <th rowspan="2" scope="rowgroup">荷兰</th>
      <th scope="row">阿姆斯特丹</th>
      <td>89</td>
      <td>34</td>
      <td>69</td>
      <td>85</td>
      <td>38</td>
    </tr>
    <tr>
      <th scope="row">乌特勒支</th>
      <td>80</td>
      <td>12</td>
      <td>43</td>
      <td>36</td>
      <td>19</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th colspan="2" scope="row">总计</th>
      <td>200</td>
      <td>200</td>
      <td>200</td>
      <td>200</td>
      <td>200</td>
    </tr>
  </tfoot>
</table>
```

### 图片

图片通过`<img>`元素嵌入。有两个属性是必须的：`src`属性：一个指向要嵌入页面的图像的URL；`alt`属性：图片无法显示的情况下会显示该属性的值。可以用`width`和`height`属性来指定图片的宽度和高度。它们的值是不带单位的整数，以像素为单位。如果指定了图片的实际大小，那么在下载图片之前，浏览器就知道需要为其留出多少空间。当图片下载完成时，浏览器就不需要移动周围的内容。

**注意**：

1. 搜索引擎会读取图像文件名并将其计入SEO（search engine optimization，搜索引擎优化）。因此，应该为图像起一个描述性的文件名。例如，`dinosaur.jpg`比`img835.png`更好。

2. 不建议使用绝对URL进行链接。从维护的角度来说，使用相对 URL比绝对URL更有效率：当将网站迁移到不同的域名时，不需要更新所有URL。

3. 未经许可，绝对不要将`src`属性指向其他网站上的图像。大多数人认为这是不道德的，因为这会导致每当有人访问页面时都会有不知情的人为图像交付带宽费用。这也可能会导致图像在不知情的情况下，被删除或被替换为尴尬的内容。

4. 不应该使用`width`和`height`属性来调整图片的大小。如果设置的图片大小过大，图片将看起来粗糙、模糊，不仅浪费带宽，图片还不符合用户需求。如果长宽比不正确，图片也可能会变形。这两个属性应该设定为图片的实际大小。




```html
<p>
  <img
    src="https://leakyfaucets.github.io/assets\images\avatar_FZ_32x32.png"
    alt="An avatar with two letters 'FZ' on it."
    width="32"
  />
</p>
<p>
  <img
    src="avatar_FZ_32x32.png"
    alt="An avatar with two letters 'FZ' on it."
    width="32"
  />
</p>

```

#### 为图片添加标题

`<figure>`元素提供一个容器，在`<img>`元素和`<figcaption>`元素（如果有）之间建立起清晰的关联。


```html
<figure>
  <img
    src="https://leakyfaucets.github.io/assets/images/avatar_FZ_32x32.png"
    alt="My avatar with two letters 'FZ' on it."
    width="32"
  />
  <figcaption>FZ Avatar</figcaption>
</figure>
```

#### 添加矢量图

可以通过`<img>`元素嵌入矢量图，也可以通过`<svg>`元素引入SVG代码。


```html
<p>
  <img src="../assets/images/example.svg" alt="Example Image" height="100" width="100" />
</p>
<p>
  <svg width="100" height="100">
    <rect width="100%" height="100%" fill="green" />
  </svg>
</p>
```

### 视频和音频

#### 视频

可以借助`<video>`元素来嵌入视频。一个简单的例子如下：


```html
<video src="https://leakyfaucets.github.io/assets/videos/rabbit320.mp4" controls>
  <p>
    你的浏览器不支持 HTML 视频。可点击<a href="rabbit320.mp4">此链接</a>观看。
  </p>
</video>
```

其中，应当使用`controls`属性来让视频或音频包含浏览器自带的控制界面。`<video>`元素的内容叫做后备内容，当浏览器不支持该元素时，就会显示这段内容，借此对旧的浏览器提供回退。

#### 使用多个播放源以提高兼容性

将`src`属性从`<video>`元素中移除，转而将它放在几个单独的`<source>`元素中，这些元素分别指向各自的资源。浏览器会检查`<source>`元素，并且播放第一个与其自身codec相匹配的媒体。WebM和MP4这两种格式在目前已经足够，在大多数平台和浏览器上都能正确播放。`type`属性是可选的，但是建议添加。它包含了`<source>`指定的MIME类型，同时浏览器也会通过检查这个属性来迅速的跳过那些不支持的格式。如果没有添加`type`属性，浏览器会尝试加载每一个文件，直到找到一个能正确播放的格式，但是这样会消耗掉大量的时间和资源。


```html
<video controls poster="https://leakyfaucets.github.io/assets\images\poster.png" preload="metadata">
  <source src="https://leakyfaucets.github.io/assets\videos\rabbit320.mp4" type="video/mp4" />
  <source src="https://leakyfaucets.github.io/assets\videos\rabbit320.webm" type="video/webm" />
  <p>你的浏览器不支持此视频。可点击<a href="https://leakyfaucets.github.io/assets\videos\rabbit320.mp4">此链接</a>观看</p>
</video>
```

其他属性：
- `poster`属性指向了一个图像的URL，这个图像会在视频播放前显示。
- `preload`属性可能是下列值之一：
    - `none`: 表示不应该预加载视频。
    - `metadata`：表示仅预先获取视频的元数据（例如长度）。
    - `auto`：可以预加载整个视频文件。
    - 空字符串：与`auto`值行为一致。

#### 音频

`<audio>`元素与`<video>`元素的使用方式几乎完全相同。因为音频播放器没有视觉部件，所以`<audio>`元素不支持`width`/`height`/`poster`属性。除此之外，`<audio>`元素支持所有 `<video>`元素的属性。一个典型的例子如下：


```html
<audio controls>
  <source src="https://leakyfaucets.github.io/assets\audios\viper.mp3" type="audio/mp3" />
  <source src="https://leakyfaucets.github.io/assets\audios\viper.ogg" type="audio/ogg" />
  <p>你的浏览器不支持该音频，可点击<a href="https://leakyfaucets.github.io/assets\audios\viper.mp3">此链接</a>收听。</p>
</audio>
```

#### 为媒体元素添加字幕

要让字幕与媒体元素一起显示，需要用`<track>`元素的`src`属性链接WebVTT文件（.vtt）。`<track>`元素需作为媒体元素的子元素，同时需要放在所有`<source>`子元素之后。使用`kind`属性来指明字幕的类别，可选的值包括：

- `subtitles`：提供媒体内容的翻译文本，主要面向能够听到音频但无法理解语言的用户。
- `captions`：提供音频内容的完整文字描述，不仅包含对话，还包含非对话信息（如音效、说话人标识等），主要面向听障人士或需要静音播放媒体的人。
- `chapters`：提供媒体内容的章节导航标题，允许用户在媒体播放过程中跳转到特定章节。
- `metadata`：供脚本或程序使用的隐藏数据轨道，不会直接显示给用户，通常用于同步广告、分析数据或其他自定义交互逻辑。

如果`kind`属性为`subtitles`，则必须定义`srclang`属性（值须为BCP 47语言标签）来告诉浏览器字幕的语言是什么。最后，建议添加`label`属性，以帮助浏览者识别字幕类别。

**注意**：浏览器会阻止媒体元素从本地文件系统加载VTT文件，需要将网页在HTTP服务器上打开。


```html
<video controls>
  <source src="../assets/videos/rabbit320.mp4" type="video/mp4" />
  <source src="../assets/videos/rabbit320.webm" type="video/webm" />
  <track kind="subtitles" src="../assets/vtt/test.vtt" srclang="zh" label="Chinese" />
</video>
```

### 表单

表单由`<form>`元素创建。最常用的两个属性是`action`和`method`。`action`指定了表单提交的URL；`method`指定了提交表单的方法，默认为`get`：表单数据会附加在`action`属性的URL中，并以?作为分隔符。

#### 表单结构化

可以在`<form>`元素中包含任意元素，用于组织表单控件本身，并为CSS样式提供可定位的容器，以便进行样式设置等操作。表单控件默认是行内的，因此需要使用元素将其分隔开，通常使用`<p>`。此外，可以使用`<fieldset>`对表单控件进行分组，并添加`<legend>`来提供对整组控件的描述。

#### 表单控件

`<input>`元素

`<input>`元素用于创建输入框，常用的属性包括：

- `type`：指定要创建的表单控件类型，常用的包括`text`、`number`、`email`、`tel`、`password`、`month`（年和月）、`date`（日期）、`datetime-local`（日期和时间）、`time`（时间）、`file`、`radio`（单选按钮，取名来自于只能按下一个按钮的老式收音机）、`checkbox`（复选框）和`range`（同时使用`min`和`max`来规定可接受值的范围）。
- `name`：为该数据项指定一个名称。当表单提交时，数据会以名值对（name/value pairs）的形式发送。对于`radio`类型，每组按钮的`name`值必须相同。如果`name`值不同，它们会被视为不同的组。
- `value`：对于`radio`类型，该值为按钮被选中时提交的值；对于`checkbox`，一般不需要设定此值，默认按钮选中时提交的值为`on`；对于其他类型，该值为表单控件在初次渲染完成时的预填值。
- `id`：用于将该表单控件与对应的`<label>`标签关联起来。
- `required`：指定该表单控件在提交表单前必须填写。
- `checked`：让按钮在页面初次加载时默认被选中。这意味着总会有一个选项被选中。
- `disabled`：禁用该表单控件。`<fieldset>`元素也可以接受`disabled`属性，这会导致其中的所有表单控件都被禁用。

`<label>`元素

`<label>`元素用于将标签文本和表单控件关联起来。标签与控件之间的关联方式是：给表单控件设置一个`id`属性，然后给 `<label>`设置`for`属性，其值与该控件的`id`相同。当视力障碍用户使用屏幕阅读器浏览和操作网页内容时，屏幕阅读器在遇到每个控件时，会朗读与之关联的标签文本，这能让他们更容易理解每个控件需要输入什么内容。

```html
<label for="name">姓名（必填）：</label>
<input type="text" name="name" id="name" required />
```

`<button>`元素

`<button>`元素用于创建一个可点击的按钮，其`type`属性默认值为`submit`，不需要显示声明。

`<select>`元素

该元素用于创建一个下拉菜单，其中的选项值由`<option>`给出。每个`<option>`元素可以带有`value`属性，指定如果该选项被选中时提交的值。如果未指定`value`，则使用`<option>`的内容作为提交值。如果想在页面加载时默认选中某个选项，可以在对应的选项上添加`selected`属性。`<select>`元素需要设置`id`属性，将控件与其标签关联起来，同时设置`name`属性，指定提交时数据项的名称。

`<textarea>`元素

该元素用于创建多行文本输入框。`rows`属性指定文本区域默认显示的行数，而`cols`属性指定文本区域默认显示的列数。如果未指定这两个属性，浏览器默认使用`cols="20"`和`rows="2"`。


```html
    <form action="./payment_page" method="get">
      <h2>报名参见见面会</h2>
      <fieldset>
        <legend>填写个人信息</legend>
        <p>
          <label for="name">姓名：</label>
          <input type="text" name="name" id="name" required />
        </p>
        <p>
          <label for="email">邮箱：</label>
          <input type="email" name="email" id="email" required />
        </p>
      </fieldset>
      <fieldset>
        <legend>选择酒店房型：</legend>
        <div>
          <input
            type="radio"
            id="hotelChoice1"
            name="hotel"
            value="economy"
            checked />
          <label for="hotelChoice1">经济型（+$0）</label>
          <input type="radio" id="hotelChoice2" name="hotel" value="superior" />
          <label for="hotelChoice2">高级型（+$50）</label>
          <input
            type="radio"
            id="hotelChoice3"
            name="hotel"
            value="penthouse"
            disabled />
          <label for="hotelChoice3">顶级套房（+$150）</label>
        </div>
      </fieldset>
      <fieldset>
        <legend>要参加的课程：</legend>
        <div>
          <input type="checkbox" id="yoga" name="yoga" />
          <label for="yoga">瑜伽（+$10）</label>
          <input type="checkbox" id="coffee" name="coffee" />
          <label for="coffee">咖啡烘焙（+$20）</label>
          <input type="checkbox" id="balloon" name="balloon" />
          <label for="balloon">气球动物艺术（+$5）</label>
        </div>
      </fieldset>
      <p>
        <label for="transport">出行方式：</label>
        <select name="transport" id="transport">
          <option value="">--请选择一项--</option>
          <option value="plane">乘坐飞机</option>
          <option value="bike">骑自行车</option>
          <option value="walk">徒步</option>
          <option value="bus">乘坐公交</option>
          <option value="train">搭乘火车</option>
          <option value="jetPack" selected>使用喷气背包</option>
        </select>
      </p>
      <p>
        <label for="comments">其他备注：</label>
        <textarea id="comments" name="comments" rows="5" cols="33"></textarea>
      </p>
      <p>
        <button>提交</button>
      </p>
    </form>
```

### 嵌入其他网页

可以通过`<iframe>`元素将其他页面嵌入到当前页面中，其属性包括：

- `width`：默认为300（像素）。
- `height`：默认为150（像素）。
- `src`：指向要嵌入的文档的 URL。
- `allow`：用于为`<iframe>`指定其权限策略，通过分号分隔不同权限策略。如`allow="fullscreen; picture-in-picture"`。
- `sandbox`：控制应用于嵌入在`<iframe>`中的内容的限制，建议始终启用该属性。该属性的值可以为空以应用所有限制，也可以为空格分隔的标记以解除特定的限制。
- `loading`：默认值为`eager`，即在页面加载时立即加载。可选为`lazy`来推迟加载，以改善性能表现。


```html
<iframe
  src="//player.bilibili.com/player.html?isOutside=true&aid=70594669&bvid=BV1gE411f7gw&cid=122468020&p=1"
  border="0"
  sandbox
  allow="fullscreen"
></iframe>
```

### 嵌入外部资源

`<object>`用于嵌入外部资源，当浏览器无法渲染指定资源时，会显示标签内部的子内容作为替代方案。常用的属性有：

- `data`：资源的URL。
- `type`：资源的MIME类型。
- `width`：无默认值。
- `height`：无默认值。


```html
<object data="../assets/files/mypdf.pdf" type="application/pdf" width="800" height="1200">
  <p>
    You don't have a PDF plugin, but you can <a href="my-pdf.pdf">download the PDF file. </a>
  </p>
</object>
```

## 文档结构

下面是一个简单HTML文档的结构：


```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <meta name="author" content="Chris Mills" />
    <meta name="description" content="This is an description." />
    <link rel="icon" href="../assets/images/avatar_FZ_32x32.png" />
    <title>我的测试页面</title>
  </head>
  <body>
    <p>这是我的页面</p>
  </body>
</html>
```

其中有：
- `<!doctype html>`：文档类型声明。目前已经成为历史遗留物，只是为了让其他一切正常工作而必须包含它。
- `<html>`元素：包裹了页面上的所有内容，有时被称为根元素。`lang`属性设定了页面的语言，有助于搜索引擎更有效地索引该网页，同时对于使用屏幕阅读器的视障人士也很有用。例如，法语和英语中都有“six”这个单词，但是发音却完全不同。
- `<head>`元素：这个元素充当一个容器，用于存放你想包含在HTML页面中但不向页面浏览者显示的内容。
    - `<meta>`元素：这个元素代表了不能由其他HTML元素表示的元数据。
        - `charset`属性将文档的字符编码指定为UTF-8。
        - `name`属性指定了`<meta>`元素的类型，而`content`属性指定了实际的元数据内容。`description`也被使用在搜索引擎显示的结果页中。
    - `<link>`元素：该元素最常用于链接样式表，此外也可以被用来创建站点图标，这些图标出现在浏览器每一个打开的标签页中以及书签面板中的书签页面旁边。
    - `<title>`元素：它设置了页面的标题，这个标题会出现在加载该页面的浏览器标签页中。当页面被收藏为书签时，页面标题也用于描述该页面。
- `<body>`元素：它包含了在页面上显示的所有内容。


### 格式化

HTML规范不强制要求对嵌套元素进行缩进。浏览器在解析HTML文档时，仅关注标签的结构、属性及文本内容。标签之间的空格、制表符或换行符通常会被视为单个空白字符处理，如下面两个代码片段是等效的：


```html
<p id="noWhitespace">狗狗很 呆 萌。</p>
<p id="whitespace">狗狗很
    呆
        萌。</p>
```

但为了保障代码的可维护性与专业性，强烈建议在所有常规开发场景中遵循统一的缩进规范（通常为2个空格）。

### 标题和段落

在HTML中，每个段落是通过`<p>`元素定义的，而标题是通过标题元素定义的。一共有六种标题元素标签：`<h1>`、`<h2>`、`<h3>`、`<h4>`、`<h5>`和`<h6>`。每个元素代表文档中不同级别的内容：`<h1>`表示一级标题，`<h2>`表示二级标题，`<h3>`表示三级标题，依此类推。

注意：
- 最好每个页面只有一个一级标题，所有其他标题位于层次结构中的下方。
- 在现有的六个标题层次中，除非觉得有必要，否则应该争取每页使用不超过三级标题。有很多层次的文件会变得笨重，难以浏览。在这种情况下建议将内容分散到多个页面。

### 应用CSS和JavaScript

CSS（Cascading Style Sheets，层叠样式表）是一种样式表语言，用来描述HTML或XML等文档的呈现方式。在HTML中通过`<link>`元素应用CSS。`<link>`元素经常位于文档的头部。它有2个属性：`rel="stylesheet"`表明这是文档的样式表，而`href`属性包含了样式表文件的路径。如：`<link rel="stylesheet" href="my-css-file.css" />`

JavaScript代码通过`<script>`元素应用，也应当放在文档的头部，并包含`src`属性来指向需要加载的JavaScript文件路径，同时最好加上`defer`以告诉浏览器在解析完成HTML后再加载JavaScript，这样可以防止JavaScript因试图访问页面上不存在的HTML元素而产生错误。如：`<script src="my-js-file.js" defer></script>`

## 文本格式

### 强调和强烈重要性

`<em>`（emphasis）元素通过强调部分内容来改变一个句子的意思，而`<strong>`（strong importance）用来对一个句子的部分内容增加重要性。浏览器默认将`<em>`元素的内容渲染为斜体，将`<strong>`元素的内容渲染为粗体，但可以通过应用CSS进行自定义，同时屏幕阅读器也能识别这些内容，将其配置为以不同的语音语调进行朗读。

如果单纯要获得斜体或粗体风格，应该使用`<i>`元素和`<b>`元素。

`<b>`、`<i>`和`<u>`元素出现于人们要在文本中使用粗体、斜体、下划线但CSS仍然不被完全支持的时期。像这样仅仅影响表象而且没有语义的元素，被称为表现元素（presentational element）并且**不应该再被使用**。因为正如我们在之前看到的，语义对无障碍、搜索引擎优化等非常重要。

**备注**：人们强烈地将下划线与超链接联系起来。因此，在网页中，最好只给链接加下划线。

### 超链接

通过将文本或其他内容包裹在`<a>`元素内，并给它一个`href`（超文本引用）属性来创建一个基本链接。

超链接除了可以链接到文档外，也可以链接到HTML文档的特定部分（被称为文档片段）。要做到这一点，必须先给要链接到的元素分配一个`id`属性，如`<h2 id="Mailing_address">邮寄地址</h2>`。为了链接到那个特定的`id`，要将它放在URL的末尾，并在前面包含井号（#），例如：


```html
<p>
  要提供意见和建议，请将信件邮寄至<a href="https://leakyfaucets.github.io/index.md#Welcome to leakyfaucets"
    >我们的地址</a
  >。
</p>
```

也可以链接到当前文档的另一部分：


```html
<p>本页面底部可以找到<a href="#引用">公司邮寄地址</a>。</p>
```

当链接到要下载的资源而不是在浏览器中打开时，可以使用`download`属性来提供一个默认的保存文件名。下面是一个Firefox的Windows最新版本下载链接的示例：


```html
<a
  href="https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=zh-CN"
  download="firefox-latest-64bit-installer.exe">
  下载最新的 Firefox 中文版 - Windows（64 位）
</a>
```

### 引用

#### 块级引用元素\<blockquote\>

浏览器的默认样式会将块引用元素渲染为**缩进**的段落。

**注意**：禁止反向嵌套：切勿将`<blockquote>`放在`<p>`标签内部。根据HTML规范，`<p>`是段落级元素，不允许包含其他块级元素。浏览器在解析时会自动关闭`<p>`，导致DOM结构异常。当引用内容包含一个或多个完整段落时，应当在`<blockquote>`内部使用`<p>`标签。


```html
<p>这是块引用：</p>
<blockquote
  cite="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/blockquote">
  <p>
    <strong>HTML <code>&lt;blockquote&gt;</code> 元素</strong>（或<em
      >HTML 块级引用元素</em
    >）表示所附文本为扩展引用。
  </p>
</blockquote>
```

#### 行内引用元素\<q\>

浏览器的默认样式会在行内引用元素的两边添加双引号。


```html
<p>
  引用元素 <code>&lt;q&gt;</code> 是<q
    cite="https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/q"
    >用于不需要段落分隔的短引用。</q
  >
</p>
```

### 引文元素\<cite\>

浏览器的默认样式会将引文元素的文本渲染为**斜体**。

`<a>`包裹`<cite>`是推荐做法，而`<cite>`包裹`<a>`虽然在HTML5中语法合法，但在语义和可访问性上通常不被推荐。因为`<cite>`默认包裹的是引文，将`<a>`放置其中会产生“超链接也是引文一部分”的歧义。


```html
<p>
  根据<a href="/zh-CN/docs/Web/HTML/Element/blockquote"><cite>MDN 块引用页</cite></a>：
</p>
```

### 缩写元素\<abbr\>

可以提供术语的完整扩展，作为`title`属性的值。


```html
<p>我们使用<abbr>HTML</abbr>超文本标记语言来组织网页文档。</p>
<p>
  第 33 届<abbr title="夏季奥林匹克运动会">奥运会</abbr>已于 2024 年 7
  月在法国巴黎举行。
</p>
```

### 联系人地址元素\<address\>

浏览器默认将其中的文本渲染为斜体。


```html
<address>Chris Mills, Manchester, The Grim North, UK</address>
```


### 上标和下标元素\<sup\>and\<sub\>


```html
<p>我的生日是在 2021 年 5 月 25 日（译者注：英文原文为 25<sup>th</sup>）</p>
<p>
  咖啡因的化学方程式是 C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>。
</p>
<p>如果 x<sup>2</sup> 的值为 9，那么 x 的值必为 3 或 -3。</p>
```

### 代码相关元素

- 行内代码元素`<code>`：用于标记计算机通用代码，默认情况下，内容文本使用用户代理默认的等宽字体显示。要表示多行代码，可在`<pre>`元素中封装`<code>`元素。`<code>`元素本身只能表示一段代码短语或一行代码。
- 预定义格式文本元素`<pre>`：在该元素中的文本通常按照原文件中的编排，以等宽字体的形式展现出来，文本中的空白符（比如空格和换行符）都会显示出来。
- 变量元素`<var>`：用于标记具体变量名，它通常使用当前字体的斜体版本来显示。
- 键盘输入元素`<kbd>`：用于标记电脑的键盘输入，它将产生一个行内元素，以浏览器的默认monospace字体显示。
- 样本输出元素`<samp>`：用于标记计算机程序的输出，通常使用浏览器的默认monotype字体。


```html
<pre><code>const para = document.querySelector('p');

para.onclick = function() {
  alert('噢，噢，噢，别点我了。');
}</code></pre>

<p>
  请不要使用 <code>&lt;font&gt;</code> 、
  <code>&lt;center&gt;</code> 等表现元素。
</p>

<p>在上述的 JavaScript 示例中，<var>para</var> 表示一个段落元素。</p>

<p>按 <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>A</kbd> 选择全部内容。</p>

<pre>$ <kbd>ping mozilla.org</kbd>
<samp>PING mozilla.org (63.245.215.20): 56 data bytes
64 bytes from 63.245.215.20: icmp_seq=0 ttl=40 time=158.233 ms</samp></pre>
```

### 时间元素\<time\>

时间元素用来表示一个特定的时间段。该元素可包含`datetime`属性，用于将日期转换为机器可读格式，从而获得更好的搜索引擎结果或自定义功能（如提醒）。


```html

<time datetime="2016-01-20">2016年1月20日</time>
```
