##补数据教程

### 补数据需求 **<font color=#87CEFA size=3 >(可以理解为官方只支持补日线数据)</font>**
**<font color=#996600 size=3 > 补当日或者前几日 分时／实时 数据</font>** 推荐使用 **[方法四](#ff4)、[方法二](#方法二、Novell与Linux互相拷贝)**  
**<font color=#996600 size=3 > 补当日k线数据</font>** 推荐使用 **[方法三](#ff3)、[方法四](#ff4)、[方法二](#方法二、Novell与Linux互相拷贝)  
**<font color=#996600 size=3 > 补当日分钟线、月线、全息资料</font>** 推荐使用 **[方法四](#ff4)、[方法二](#方法二、Novell与Linux互相拷贝)**  
**<font color=#996600 size=3 > 补区个股或市场区间k线</font>** 推荐使用 **[方法一](#方法一、rt服务器下载)、[方法四](#ff4)、[方法二](#方法二、Novell与Linux互相拷贝)**  
**<font color=#996600 size=3 > 补历史全部资料</font>** 推荐使用 **[方法四](#ff4)、[方法二](#方法二、Novell与Linux互相拷贝)** 和 **[方法五](#ff5)**  
**<font color=#996600 size=3 > 补龙讯F10、全息资料</font>** 推荐使用 **[方法五](#方法五、龙讯F10官网下载)**  

## 关于补数据的方法

#### 方法一、rt服务器下载

rt服务器地址: **电信线路1: 122.226.188.39  |  电信线路2: 58.56.9.66  |  联通线路: 60.217.231.66**  
**<font color=#ff9900 size=2 >⚠ rt服务器只能补日线！</font>**
```
说明：关于rt服务器指的就是daydown下载工具所连接的服务器ip，Novell与Linux通用。
```
#### 方法二、Novell与Linux互相拷贝

**<font color=#cc3300 size=3 >Novell与Linux 沪深期货数据通用（ 港股通、股转不通用 ）</font>**  
**<font color=#ff9900 size=2 >⚠ Novell向Linux拷贝数据，注意要转换小写！ </font>**    
转小写批处理下载链接： [微云](http://share.weiyun.com/10acfe290b54c23e783e1b0edf2ee920)/[百度云](http://pan.baidu.com/s/1mhHwsoK)  
使用方法：将批处理放到需要转换大小写文件夹的同目录，直接执行即可，会将通目录和子目录一并转换小写。
```

```

#### 方法三、官网下载
[linux wmanager补数据方法](Lwmamager.md) 工具下载地址: http://www.qianlong.com.cn/soft/download_data.aspx
**<font color=#ff9900 size=2 >  ⚠ 官方只能补日线！当日k线17点更新</font>**  

#### 方法四、其他营业部、其他服务器拷贝 <span id="ff4"></span>
从其他来源复制完整数据到本地服务器，该方法可以补日线、分钟线和实时数据，方法是一样的。下面以上海市场日线数据举例，步骤如下，其他数据以此类推：  
**<font color=#ff9900 size=2 >收盘过程中请勿执行以下操作</font>**
###### Linux系统补日线的操作步骤<span id="cpdaymin"><span>
1. 从其他来源拿到完整数据，一般是压缩文件，里面是day目录，day下面是上海市场日线文件。
2. qianlong用户登录服务器，复制压缩文件到服务器上<code>/opt/qianlong/sysdata/history/shase</code>目录下
3. 根据压缩文件后缀名，选择以下命令执行：
针对 *.zip
```
unzip -o *.zip
```
针对 *.tar.gz
```
tar xvf *.tar.gz
```
针对 *.rar
```
unrar x *.rar
```
###### Linux系统补实时数据的操作步骤<span id="cprealtime"><span>
**<font color=#ff9900 size=2 >中午或者收市后进行，盘中请勿执行以下操作</font>**：
1. 从其他地方取得正确的行情数据。
2. web上停止转码和服务平台程序。
3. 确认"程序设置->l2dcd设置->基本路径"处的"上海行情库"和"非交易文件路径"设置正确，其中
    * "上海行情库"：指向服务器上mktdt00.txt文件所在的路径，包括文件名。
    * "非交易文件路径"： 指向jfyYYYYMMDD.txt文件所在路径，比如今天我这是
        <code>/opt/qianlong/sysdata/remote/msg/fjy20161028.txt</code>
4. 在"钱龙Linux控制台->L2DCD"处下拉框选"重做全市场初始化"、"重做上海市场初始化"或"重做深圳市场初始化"，根据市场选择，然后开启转码。
5. 重启客户端连接这台服务器，观察最后一笔数据(之前的走势都是直线，暂时不用理会)。如果正常了就进入下一步，否则请从第二步开始检查。
6. 关闭转码机。
7. 登录服务器替换realtime目录下当天日期的文件(!一定是qianlong用户!)，目录为：
<code>/opt/qianlong/sysdata/realtime/shase(sznse)/</code>
8. 在"钱龙Linux控制台->L2DCD"处下拉框选"正常模式"，开启转码和服务平台。

4. 重启服务平台
5. 如果是收盘完毕之后进行操作，那么还需要重启转码，它会重新收一次当天的日线，确保数据完整。

#### 方法五、龙讯F10官网下载
**<font color=#ff9900 size=2 >  ⚠ 每周五更新 信龙官网 [xlinfo.cn](http://www.xlinfo.cn/)   首页>技术支持>数据下载</font>**

----------

## Linux 数据对应目录

### 补分时（实时）数据
```
当日（实时）分时

上海分时数据位置opt/qianlong/sysdata/realtime/shase/修改日期为当日的文件

深圳分时数据位置opt/qianlong/sysdata/realtime/sznse/修改日期为当日的文件

港股通分时数据位置opt/qianlong/sysdata/realtime/hk2sh/修改日期为当日的文件

期货分时数据位置opt/qianlong/sysdata/realtime/cnfol/修改日期为当日的文件

股份转让分时数据位置opt/qianlong/sysdata/realtime/neeq/修改日期为当日的文件

--------------
前几天的分时

上海日线位置opt/qianlong/sysdata/realtime/shase/年月日.dat 的文件夹

深圳日线位置opt/qianlong/sysdata/realtime/sznse/年月日.dat 的文件夹

港股通日线位置opt/qianlong/sysdata/realtime/hk2sh/年月日.dat 的文件夹

期货日线位置opt/qianlong/sysdata/realtime/cnfol/年月日.dat 的文件夹

股份转让日线位置opt/qianlong/sysdata/realtime/年月日.dat 的文件夹
```


### 补历史数据
```
日线

上海日线位置opt/qianlong/sysdata/history/shase/day

深圳日线位置opt/qianlong/sysdata/history/sznse/day

港股通日线位置opt/qianlong/sysdata/history/hk2sh/kday

期货日线位置opt/qianlong/sysdata/history/cnfol/day

股份转让日线位置opt/qianlong/sysdata/history/neeq/day

-------------
月线

港股通月线位置opt/qianlong/sysdata/history/hk2sh/kmon

股份转让月线位置opt/qianlong/sysdata/history/kmon

-------------
分钟线

上海一分钟线位置opt/qianlong/sysdata/history/shase/1mn

上海五分钟线位置opt/qianlong/sysdata/history/shase/min

深圳一分钟线位置opt/qianlong/sysdata/history/sznse/1mn

深圳五分钟线位置opt/qianlong/sysdata/history/sznse/min

港股通一分钟线位置opt/qianlong/sysdata/history/hk2sh/kmn1

港股通十五分钟线位置opt/qianlong/sysdata/history/hk2sh/km15

期货一分钟线位置opt/qianlong/sysdata/history/cnfol/1mn

期货五分钟线位置opt/qianlong/sysdata/history/cnfol/min

股份转让一分钟线位置opt/qianlong/sysdata/history/kmn1

股份转让十五分钟线位置opt/qianlong/sysdata/history/km15
```
-------------
权息资料
```
上海日线位置opt/qianlong/sysdata/history/shase/weight

深圳日线位置opt/qianlong/sysdata/history/sznse/weight

港股通日线位置opt/qianlong/sysdata/history/hk2sh/weight

期货日线位置opt/qianlong/sysdata/history/cnfol/weight

股份转让日线位置opt/qianlong/sysdata/history/neeq/weight
```

**Linux操作系统下，以上所有文件操作请使用qianlong用户执行，操作完成后无需执行赋权命令！**

-------------

## Novell 数据对应目录

### 补分时（实时）数据
```
当日（实时）分时

上海分时数据位置ml45/sysdata/realtime/shase/修改日期为当日的文件

深圳分时数据位置ml45/sysdata/realtime/sznse/修改日期为当日的文件

港股通分时数据位置ml45/sysdata/realtime/hk2sh/修改日期为当日的文件

期货分时数据位置ml45/sysdata/realtime/cnfol/修改日期为当日的文件

股份转让分时数据位置ml45/sysdata/realtime/neeq/修改日期为当日的文件

--------------
前几天的分时

上海日线位置ml45/sysdata/realtime/shase/年月日.dat 的文件夹

深圳日线位置ml45/sysdata/realtime/sznse/年月日.dat 的文件夹

港股通日线位置ml45/sysdata/realtime/hk2sh/年月日.dat 的文件夹

期货日线位置ml45/sysdata/realtime/cnfol/年月日.dat 的文件夹

股份转让日线位置ml45/sysdata/realtime/年月日.dat 的文件夹
```

### 补历史数据
```
日线

上海日线位置ml45/sysdata/history/shase/day

深圳日线位置ml45/sysdata/history/sznse/day

港股通日线位置ml45/sysdata/history/hk2sh/day

期货日线位置ml45/sysdata/history/cnfol/day

股份转让日线位置ml45/sysdata/history/neeq/day

-------------
月线

港股通月线位置ml45/sysdata/history/hk2sh/kmon

股份转让月线位置ml45/sysdata/history/kmon

-------------
分钟线

上海一分钟线位置ml45/sysdata/history/shase/1mn

上海五分钟线位置ml45/sysdata/history/shase/min

深圳一分钟线位置ml45/sysdata/history/sznse/1mn

深圳五分钟线位置ml45/sysdata/history/sznse/min

港股通一分钟线位置ml45/sysdata/history/hk2sh/kmn1

港股通十五分钟线位置ml45/sysdata/history/hk2sh/km15

期货一分钟线位置ml45/sysdata/history/cnfol/1mn

期货五分钟线位置ml45/sysdata/history/cnfol/min

股份转让一分钟线位置ml45/sysdata/history/kmn1

股份转让十五分钟线位置ml45/sysdata/history/km15
```
-------------
权息资料
```
上海日线位置ml45/sysdata/realtime/shase/weight

深圳日线位置ml45/sysdata/realtime/sznse/weight

港股通日线位置ml45/sysdata/history/hk2sh/weight

期货日线位置ml45/sysdata/history/cnfol/weight

股份转让日线位置ml45/sysdata/history/neeq/weight
```

## 龙讯F10

### linux 龙讯F10

 信龙官网 [xlinfo.cn](http://www.xlinfo.cn/)  **首页>技术支持>数据下载**

|历史咨询| 下载地址|备注|
| ------ |:----------:|:----------:|
|LINUX版龙讯C系列F10完整历史数据|[Go to download](http://www.xlinfo.cn/server/server10.html)|(每周五更新)|
|龙讯权息weight历史数据包|[Go to download](http://www.xlinfo.cn/server/server10.html)|(每周五更新)|
