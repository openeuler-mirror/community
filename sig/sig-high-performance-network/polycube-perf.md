# 性能测试

## iptables/nftables性能测试比较

1. 测试环境

   ```
   软件版本：
   polycubenetwork/polycube v0.9.0-rc de2aeeb0bff2        43 hours ago        2.41GB
   
   运行
   sudo docker run  -it --rm --privileged -v /lib/modules:/lib/modules:ro -v /usr/src:/usr/src:ro -v /etc/localtime:/etc/localtime:ro polycubenetwork/polycube:v0.9.0-rc /bin/bash -c 'polycubed -d && /bin/bash'
   
   OS版本
   root@fe93e1fb60dc:/# uname -a
   Linux fe93e1fb60dc 4.15.0-74-generic #84-Ubuntu SMP Thu Dec 19 08:06:28 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
   root@fe93e1fb60dc:/#
   
   
   ```

   

2. 测试数据

```


容器内：

===> 未添加任何规则的数据
guodeqing@ubuntu1804:~$ sudo iperf -c 172.17.0.3 -p 6666
------------------------------------------------------------
Client connecting to 172.17.0.3, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 172.17.0.1 port 38204 connected with 172.17.0.3 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  36.8 GBytes  31.6 Gbits/sec

===> 添加iptables1000条规则的数据
iperf -c 172.17.0.3 -p 6666
------------------------------------------------------------
Client connecting to 172.17.0.3, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 172.17.0.1 port 42480 connected with 172.17.0.3 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  18.2 GBytes  15.7 Gbits/sec

===> 添加pcn-iptables1000条规则的数据
iperf -c 172.17.0.3 -p 6666
------------------------------------------------------------
Client connecting to 172.17.0.3, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 172.17.0.1 port 46886 connected with 172.17.0.3 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  32.7 GBytes  28.1 Gbits/sec


```

