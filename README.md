# A Simple AtCoder-ID Crawler

## 引言

众所周知，AtCoder 的内部是没有题号的，这在做题及一些统计中也许会比较麻烦。

而 vjudge 和 luogu 上爬取的 AtCoder 题目都有对应的题号，且它们的题号是统一的。

~~(我猜应该是 luogu 爬 vjudge 的，因为 vjudge 的题目更三年通常比 luogu 早)~~

于是就写了这么一个小脚本用来爬 AtCoder 的题号，目前是在 vjudge 上爬取。

这个脚本目前也是更新 [OI-transit](https://github.com/yhx-12243/OI-transit) 中 AtCoder 题目跳转链接的来源。

## 需求

* Node.js
* Python3 及其 requests, aiohttp 模块
* Linux 或 Bash 运行环境

## 用法

一键使用：`./atcoder.sh <num>`，其中 num 表示一次的爬取量，不宜太大也不宜太小，取 50 ~ 100 左右为宜。

爬取题目列表但不爬取跳转链接：`./atcoder.list.py`

通过列表更新链接：`./atcoder_crawler.py <num>`

初步压缩获得的结果：`./atcoder_compress.py`

进一步压缩获得的结果以及打包成 base64：`./final_compress.js`

注意文件 `result.txt` 是用来记忆化的，这样每次 AtCoder 更新后只需爬取增加的题目编号即可。

## 解码脚本

具体参见 [OI-transit 中的 basic.js](https://github.com/yhx-12243/OI-transit/blob/master/additional_files/js/basic.js)，列举代码如下：

> https://github.com/yhx-12243/OI-transit/blob/45834e3a4777988418a5a9dfc793c91ddacf6201/additional_files/js/basic.js#L258-L266
