# 钱龙Linux的安装教程

## 拓扑图
![](image/Linux3.png)

## 安装环境准备
| 主/备服务器 | 数据中心/点对点服务器 |钱龙网关 |USB代理线/代理PC|无盘站|授权文件|
| ------ |:----------:|:----------:|:----------:|:----------:|:----------:|
| **操作系统** ：乾隆公司提供 Redhat/Cetos| **操作系统**：WINDOWS 2003 SERVER/XP|**操作系统**：WINDOWS 2003 SERVER/XP|**操作系统**：WINDOWS 2003 SERVER/XP|/|授权文件：ql4、ql6文件|
|**CPU处理器**：P4 Xeon 2.4G*2 内存: 4G及以上|**CPU处理器**：INTEL 或AMD处理器2.0GHz以上内存: 2GB及以上|**CPU处理器**：INTEL 或AMD处理器2.0GHz以上内存: 2GB及以上|**CPU处理器**：INTEL 或AMD处理器2.0GHz以上内存: 2GB及以上|**CPU处理器**：INTEL 或AMD处理器1.2GHz以上||
|**硬盘空间**: 50G可用空间、raid5阵列 阵列卡缓存512M（含）|**硬盘空间**: 10G可用空间|**硬盘空间**: 10G可用空间|**硬盘空间**: 10G可用空间|**内存**: 512MB及以上 VGA彩显 ||
|**推荐型号**: IBM X3650 M5系列、HP DL380 G9系列、DELL R730系列|**推荐型号**: 双网卡|**推荐型号**: 双网卡|**推荐型号**: 双网卡|**推荐型号**: 8139型号的PXE网卡||
|**安装方式**：光盘安装/USB安装||||||
|**服务器系统兼容查询**: [查询地址](https://access.redhat.com/ecosystem/search/#/ecosystem/Red%20Hat%20Enterprise%20Linux?category=Server) |||||　|

## 系统&程序下载

| 系统版本|文件名| 下载地址|MD5 |文件大小|备注|
| ------ |:----------:|:----------:|:----------:|:----------:|:----------:|
|Linux(redhat) 6.2|rhel-6.2-i386-custom.iso| [Go to download](http://share.weiyun.com/0c7ec2e5abf74e843d97c18122bb5090)|C182C551654E6DBEFE3AE42076E26D32|524 MB (549,732,352 bytes)|旧服务器光盘安装的系统版本
|Linux（redhat）7.0|rhel-7.0-x86_64-custom.iso|[Go to download](http://share.weiyun.com/7982e6981ebb0379498d0f686a5106a0)|645553C297D1FB96A938AD05E02DB8DD|905 MB (949,043,200 bytes)|光盘安装系统镜像
|Linux（centos）7.2|QL_LINUX7-x86_64-20160612.iso|[Go to download](http://share.weiyun.com/7e4a2a26e59c9b12f5bcfa6341ab47ea)|1B6DB1FE46B352379893A6A123CDA61F|1,003 MB (1,051,963,392 bytes)|U盘安装镜像(内置4月27日app&diskless)

---------------
|Diskless & APP| 下载地址|MD5 |文件大小|备注|
| ------ |:----------:|:----------:|:----------:|:----------:|
|qianlong_diskless_iso_2016_04_27.iso|[Go to download](http://share.weiyun.com/48255e336153e4555686a2e4b61eee36)|0F8B9AEB8E851847203BA80EF95814B2|168 MB (175,788,032 bytes)||
|qianlong_app_iso_2016_04_27.iso|[Go to download](http://share.weiyun.com/6b5b2a5a9fbe920cdf3086c7ad7579eb)|5931011030507BD9CF2CD56DCC5B810F|19.5 MB (20,453,376 bytes)|　|

---------------
|点对点服务端 & Serviceconfig| 下载地址|MD5 |文件大小|备注|
| ------ |:----------:|:----------:|:----------:|:----------:|
|点对点服务端 140|[Go to downloa](http://share.weiyun.com/4f4b45ca52be53b9daff6719f73247d0)|3A5452B58F9B44265C226405DD23FBCC|808 KB (827,279 bytes)||
|Serviceconfig服务配置工具2016-01-21|[Go to downloa](http://share.weiyun.com/fd728273d090c6f6db3b40a1531e275d)|BC130640AA1B59D22AE0EA6F82A1BC50|23.9 MB (25,097,825 bytes)|[官网下载地址](http://www.qianlong.com.cn/soft/download_wl.asp)|
---------------
|周边工具| 下载地址|备注|
| ------ |:----------:|:----------:|
|Winscp|[Go to download](http://share.weiyun.com/3873742e957dd38e626a4ca8a4a53bc9)|SSH工具|
|Putty|[Go to download](http://share.weiyun.com/98b42da89378027ef479e16540d228cd)|推荐与winscp一起安装使用|
|转小写批处理|[Go to download](http://share.weiyun.com/10acfe290b54c23e783e1b0edf2ee920)|Novell 拷贝日线转小写到Linux|
|U盘烧录软件|[Go to download](http://share.weiyun.com/77a15702b9d1670c8e3fdf7ca45f9899)|[官网地址](http://cn.ezbsystems.com/ultraiso/download.htm)|
|子网掩码计算器|[Go to download](http://share.weiyun.com/f17524a33950e8b01b5c2cdaff775edb)|营业部无盘站超过一个子网计算时用|
|浏览器||推荐 谷歌、火狐|

## 历史数据下载 

> 补历史数据详细教程参考 [补数据](sysdata.md)

> 信龙官网 [xlinfo.cn](http://www.xlinfo.cn/)  **首页>技术支持>数据下载** 

|历史咨询| 下载地址|备注|
| ------ |:----------:|:----------:|
|LINUX版龙讯C系列F10完整历史数据|[Go to download](http://www.xlinfo.cn/server/server10.html)|(每周五更新)|
|龙讯权息weight历史数据包|[Go to download](http://www.xlinfo.cn/server/server10.html)|(每周五更新)|

## 系统安装 (光盘安装/USB安装)

> 视频下载地址：[Go to download](http://share.weiyun.com/18551de8e5a243f29baab81c2873fa0a)

<cten>**光盘安装(Redhat版本)**
<video id="video"  width="630" height="360" controls="controls" preload="none" poster="/image/Linux(redhat).jpg">
      <source id="mp4" src="http://o77zzwbm6.bkt.clouddn.com/qianlong-linux-setup1.mp4" type="video/mp4">
      <p>Your user agent does not support the HTML5 Video element.</p>
</video> 


**U盘安装(Centos版本)**
<video id="video"  width="630" height="360" controls="controls" preload="none" poster="/image/linux (Centos).jpg">
      <source id="mp4" src="http://o77zzwbm6.bkt.clouddn.com/usblinux2.mp4" type="video/mp4">
      <p>Your user agent does not support the HTML5 Video element.</p>
</video>

**沪深5档配置**
<video id="video"  width="630" height="360" controls="controls" preload="none" poster="/image/5dang.jpg">
      <source id="mp4" src="http://o77zzwbm6.bkt.clouddn.com/5dang2.mp4" type="video/mp4">
      <p>Your user agent does not support the HTML5 Video element.</p>
</video>

**沪深10档、期货、股转、港股通配置**
<video id="video"  width="630" height="360" controls="controls" preload="none" poster="/image/other10.jpg">
      <source id="mp4" src="http://o77zzwbm6.bkt.clouddn.com/10dang.mp4" type="video/mp4">
      <p>Your user agent does not support the HTML5 Video element.</p>
</video>


## 文档下载

[钱龙场内Novell向linux改造解决方案.doc](http://share.weiyun.com/548dfada946b7792cf7c958b3ea8a5c2)

[钱龙Linux（7.2版）网络版系统管理员手册.doc](http://share.weiyun.com/e8ead4a898f6eacc9dd611569443eb6d)

### 服务器安装Linux说明文档

[HP ProLiant DL380-Gen9 安装说明.doc](http://share.weiyun.com/02457f63d763e12db01e46a7191e8cb1)

[hp388G9 raid5.doc](http://share.weiyun.com/200dccdb5309cf6f0dc9cfde75ff2f60)

[Dell PowerEdge R730 安装说明.doc](http://share.weiyun.com/4791c8d290f09348146c392e006212b6)

[Lenovo(IBM) System x3550 M5 安装说明.doc](http://share.weiyun.com/e48d9416d2ac43ed18eac414c603a10c)

