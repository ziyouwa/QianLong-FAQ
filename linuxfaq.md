# 钱龙Linux FAQ 集 

> 文档过长建议使用浏览器搜索"Ctrl + F"进行页内关键词搜索

## 1.盘中各种数据画线异常
中午或者收盘 替换realtime文件或者重新初始化(重新初始化会拉直线)
<code>opt/qianlong/sysdata/realtime/shase(sznse)/</code>
替换完成要赋权，赋权命令如下
```
chmod -R 777 /opt/qianlong 
chown -R qianlong:qianlong /opt/qianlong
```
## 2.Linux服务器时间校准
Linux初始化时间未进行初始化，转码机状态显示初始化数据处理逻辑[1]
```
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
## 6.Linux DHCP地址池重新分配
适用于redhat6.2/redhat7.0
```Setup_config```

## 7.Linux 服务平台启动不起来
看系统状态里的转码状态是否正常，流驱动 沪盘中、深盘中？读库 还是 初始化 查看日志 转码机系统日志 、行情传输日志 、数据中心  服务平台启动不起来 一般就是初始化没完成

## 8.上证领先指标中白线和黄线的含义
白线是上证指数走势图，黄线是不含加权的上证领先指数走势图。 黄线的算法不同，有的软件是使用均价的方式计算的。我们是使用算术平均方式来计算的，本质上还是指数加权的算法。只是权重都是一样了。 因上证指数是以各上市公司的总股本为加权计算出来的，故盘子大的股票较能左右上证指数的走势，如马钢、石化等。而黄线表示的是不含加权的上证指数，各股票的权数都相等，所以价格变动较大的股票对黄线的影响要大一些。这样，当上证指数上涨时，如白线在黄线的上方，它说明大盘股的影响较大，盘子大的股票涨幅比盘子小的股票要大；反之，如黄线在白线的上方，就是小盘股的涨幅比大盘股要大。而当上证指数下跌时，如黄线在白线的下方，它表示大盘股的下跌幅度较小而小盘股的股票跌幅较大；反之，如白铁在黄线的下方，它表示大盘股的跌幅比较大。

## 9.Linux融资融券 前面没有R A B Q 或者标志不对
```opt\qianlong\syscfg\commark.ini``` 需要更新 找龙讯 或者其他营业部拷贝

## 10.大盘均为红色
![](image/dph.png)






























