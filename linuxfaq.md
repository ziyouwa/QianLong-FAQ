## 1.盘中各种数据画线异常
中午或者收盘 替换realtime文件或者重新初始化(重新初始化会拉直线)
<code>opt/qianlong/sysdata/realtime/shase(sznse)/</code>
替换完成要赋权，赋权命令如下
```Bash
chmod -R 777 /opt/qianlong 
chown -R qianlong:qianlong /opt/qianlong
```
## 2.Linux服务器时间校准
Linux初始化时间未进行初始化，转码机状态显示初始化数据处理逻辑[1]
```Bash
date 　　　　　　　　//显示时间
date -s 20160301 　　　　//修改日志
date -s 9:30:00 　　　　//修改时间 
hwclock -w 　　　　//写进主板

```

## 3.涨跌停价格不对
中午替换realtime文件 方法见1
原因是因为初始化不对，可能原因卫星接收行情库晚，初始化早，或者点对点打开晚

## 4.补日K线方法

rttool 下载、Novell拷贝、官网下载

上海日线位置```opt/qianlong/sysdata/realtime/shase/day```

深圳日线位置```opt/qianlong/sysdata/realtime/sznse/day```

港股通日线位置```opt/qianlong/sysdata/history/hk2sh/kday```

期货日线位置```opt/qianlong/sysdata/history/cnfol/day```

股份转让日线位置```opt/qianlong/sysdata/history/neeq```

替换完成要赋权，赋权命令如下
```
chmod -R 777 /opt/qianlong 
chown -R qianlong:qianlong /opt/qianlong
```
## 5.Linux自选股不保存
修复自选股软连接
```
cd /opt/qianlong/client/lonld
rm –rf usrcfg
ln –s /tmp/usrcfg usrcfg
rm –rf data
ln –s /tmp/data data
```