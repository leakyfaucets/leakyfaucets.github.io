---
layout: post
title: "Github Pages最小创建指南"
categories: [Website]
author:
- Frank Zhang
comments: true
modified_date: 2026-06-11
---

本文通过预设主题实现了以最少的文件来创建`Github`页面，同时给出了进一步定制页面和添加其他功能的方法，适合想从0开始搭建自己`Github`页面的新手用户。

## 引言

本文为新手教程，目的是基于预设主题实现以最少文件创建个人`Github Pages`。目前已有教程大多基于`Theme Chooser`选项来选择预设主题，但该选项似乎已被移除，因此需要手动添加配置文件和主页。如果想快速基于`minima`主题的最新版本来创建`Github`页面，可参考下面的[快速流程](#快速流程)。后面对各步骤进行了说明，并给出了创建文章和基于添加评论功能的教程，适合想进一步深入的用户。

## 快速流程

1. 创建名为`<username>.github.io`的公开仓库，其中`<username>`为你的`Github`用户名。
2. 在仓库根目录创建`_config.yml`文件，内容为：
```
remote_theme: "jekyll/minima@4de3223"
title: Your awesome title
```
3. 在仓库根目录创建`index.md`文件，内容为：
```
---
layout: home
title: Home
---
```
4. 保存上述文件并提交，约一分钟后访问`https://<username>.github.io`即可查看网站，其中`<username>`为你的`Github`用户名。

## 步骤说明

### 创建仓库

对于免费用户，必须将仓库可见性设为公开，具体可参考[Github的计划](https://docs.github.com/zh/get-started/learning-about-github/githubs-plans)。添加`README.md`是可选的。如果添加的话，需要在仓库根目录添加`index.md`或`index.html`文件以区别仓库说明（`README.md`）和网站主页（`index.md`）。如果没有`index.md`，将基于`README.md`创建主页。

### 修改配置

下面是更丰富的配置选项：
```
remote_theme: "jekyll/minima@4de3223"
title: Your awesome title
author:
  name: your-name
  email: your-email@domain.com
description: >
  Write an awesome description for your new site here.
  It will appear in your document head meta and in your feed.xml site description.
minima:
  skin: auto
  nav_pages:
    - index.md
  date_format: "%Y-%m-%d"
  show_excerpts: true
  social_links:
    - title: GitHub profile
      icon: github
      url: "https://github.com/<username>"
```
其中，`minima`参数中的配置为`minima`主题独有的，且不同`minima`版本的特有参数也有不同，这里展示的是3.0版本的参数。具体说明及使用方法请参考[官方文档](https://github.com/jekyll/minima/tree/master#usage)。

`theme`、`title`、`author`、`description`为通用的配置选项，各个主题应该都支持。其中`theme`为页面主题，预设主题请参阅[支持的主题](https://docs.github.com/zh/pages/setting-up-a-github-pages-site-with-jekyll/adding-a-theme-to-your-github-pages-site-using-jekyll#supported-themes)。大多数主题遵循`jekyll-theme-NAME`命名约定，如`jekyll-theme-minimal`。但我发现`minima`主题的命名直接为`minima`，使用时要注意区分。同时，也可使用在`GitHub`上托管的任何其他`Jekyll`主题，键入`remote_theme: THEME-NAME`即可。

我们这里以`minima`主题为例。<mark>注意</mark>：如果使用`theme: minima`，使用的`minima`版本将为2.5.1。但目前的最新版本为3.0，其中大多数参数都发生了变化，因此官方仓库的说明并不适用于该版本，需要参考[2.5版本的说明](https://github.com/jekyll/minima/blob/v2.5.0/README.md)。为了使用新版本的特性（如皮肤、评论功能等），我们这里使用最新版本。

由于3.0版本仍在开发，官方建议指定git引用以避免更新导致的问题。因此，我们使用`remote_theme: jekyll/minima@<ref>`来指定版本。查看[历史提交](https://github.com/jekyll/minima/commits/master/)页面以获取最新版本的引用。这里，我们以文章发布时的最新提交`jekyll/minima@4de3223`为例进行创建。

### 创建主页

`index.md`文件中`layout`指定了该页面的样式为主页，`title`为该页面的标题。第二个`---`后面的内容会展示在文章之前，遵循`markdown`语法。建议从二级标题（##）开始写，因为默认`title`为一级标题。

### 查看网站

保存并提交文件后需要等待自动构建，可以在仓库主页查看构建状态。

## 发布文章

创建名为`_posts`的文件夹，用于存放文章。文章文件命名遵循`年-月-日-名称.md`的规则，如`2026-06-10-github-pages.md`。

文章文件内容示例如下：
```
---
layout: post
title: "Your awesome title"
categories: [1, 2]
author:
- author1
- author2
comments: true
modified_date: 2026-06-10
---

Excerpt

## Content

This is an example.
```
其中，`layout`指定了文章的布局为`post`，`title`为文章的标题，这两个是必需的。`categories`是对文章的分类，`author`可添加多个作者。`comments`控制了评论功能的开关，默认为`true`。`modified_date`会增加一个更新时间（Updated）。第二个`---`后面便是文章的正文了，同样遵循`markdown`语法。`minima`主题会将文章显示在首页，默认首行内容为文章的节选，如果设置了`show_excerpts: true`，会随文章一同展示在首页。

## 添加评论功能

我这里使用的是`giscus`。我曾尝试了`gitalk`，但它会在前端暴露`GitHub Application Client`密码，且长时间无人维护，因此不太推荐。

首先需要在仓库的设置-General-Features中打开`Discussion`功能，然后安装[giscus app](https://github.com/apps/giscus)。访问[`giscus`主页](https://giscus.app/zh-CN)，根据页面提示填写仓库名。映射关系建议选择“Discussion的标题包含页面的`pathname`”，因为文章的`pathname`具有全局唯一性且永久不变。同时建议使用严格的标题匹配，以避免评论串台。选择好其他特性后页面会生成对应参数，如下面的例子：
```
<script src="https://giscus.app/client.js"
        data-repo="[repo_name]"
        data-repo-id="[repo_id]"
        data-category="Announcements"
        data-category-id="[category-id]"
        data-mapping="pathname"
        data-strict="1"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-input-position="top"
        data-theme="preferred_color_scheme"
        data-lang="zh-CN"
        data-loading="lazy"
        crossorigin="anonymous"
        async>
</script>
```
只需要新建`_includes/comments.html`文件，并将上述内容复制到该文件中保存提交即可。添加`comments.html`后，默认开启评论功能，如需关闭，需要在文章开头添加`comments: false`。

<mark>请注意</mark>：以上操作只适用于`minima`3.0版本，旧版本不支持通过`comments.html`文件导入评论功能。

## 总结

本文基于预设主题`minima`创建个人页面，适合想要从0开始、基于最少的文件来创建`Github Pages`的新手用户。通过使用`minima`主题，本文无需更改模板文件便可引入评论区功能。此外，也可以通过fork现有的仓库来快速创建，具体操作可参考其他教程。如果想进一步定制自己的网站，可以参考[官方文档](https://docs.github.com/zh/pages)。