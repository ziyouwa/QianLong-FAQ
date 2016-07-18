# 补数据教程

## Linux 补数据

### 补分时（实时）数据

当日（实时）分时

上海日线位置opt/qianlong/sysdata/realtime/shase/除文件夹以外的其他文件

深圳日线位置opt/qianlong/sysdata/realtime/sznse/除文件夹以外的其他文件

港股通日线位置opt/qianlong/sysdata/realtime/hk2sh/除文件夹以外的其他文件

期货日线位置opt/qianlong/sysdata/realtime/cnfol/除文件夹以外的其他文件

股份转让日线位置opt/qianlong/sysdata/realtime/neeq/除文件夹以外的其他文件

--------------
前几天的分时 

上海日线位置opt/qianlong/sysdata/realtime/shase/年月日.dat 的文件夹

深圳日线位置opt/qianlong/sysdata/realtime/sznse/年月日.dat 的文件夹

港股通日线位置opt/qianlong/sysdata/realtime/hk2sh/年月日.dat 的文件夹

期货日线位置opt/qianlong/sysdata/realtime/cnfol/年月日.dat 的文件夹

股份转让日线位置opt/qianlong/sysdata/realtime/年月日.dat 的文件夹



### 补历史数据

日线

上海日线位置opt/qianlong/sysdata/history/shase/day

深圳日线位置opt/qianlong/sysdata/history/sznse/day

港股通日线位置opt/qianlong/sysdata/history/hk2sh/kday

期货日线位置opt/qianlong/sysdata/history/cnfol/day

股份转让日线位置opt/qianlong/sysdata/history/neeq

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

-------------
全息资料

上海日线位置opt/qianlong/sysdata/realtime/shase/weight

深圳日线位置opt/qianlong/sysdata/realtime/sznse/weight

港股通日线位置opt/qianlong/sysdata/history/hk2sh/weight

期货日线位置opt/qianlong/sysdata/history/cnfol/weight

股份转让日线位置opt/qianlong/sysdata/history/weight

**以上所有文件操作，操作完成均执行赋权命令**

```
chmod -R 777 /opt/qianlong

chown -R qianlong:qianlong /opt/qianlong
```

-------------
龙讯F10

 信龙官网 [xlinfo.cn](http://www.xlinfo.cn/)  **首页>技术支持>数据下载** 

|历史咨询| 下载地址|备注|
| ------ |:----------:|:----------:|
|LINUX版龙讯C系列F10完整历史数据|[Go to download](http://www.xlinfo.cn/server/server10.html)|(每周五更新)|
|龙讯权息weight历史数据包|[Go to download](http://www.xlinfo.cn/server/server10.html)|(每周五更新)|

## Novell 补数据