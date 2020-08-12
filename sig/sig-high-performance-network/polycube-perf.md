# 性能测试

## iptables/nftables性能测试比较

1. 测试环境
2. 测试数据

```
guodeqing@ubuntu1804:~/ebpf-test/net$ iperf -c 9.9.9.9 -p 6666
------------------------------------------------------------
Client connecting to 9.9.9.9, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 9.9.9.99 port 54490 connected with 9.9.9.9 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec   375 MBytes   314 Mbits/sec

guodeqing@ubuntu1804:~/ebpf-test/net$ iperf -c 9.9.9.9 -p 6666
------------------------------------------------------------
Client connecting to 9.9.9.9, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 9.9.9.99 port 54520 connected with 9.9.9.9 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  2.76 GBytes  2.37 Gbits/sec

guodeqing@ubuntu1804:~/ebpf-test/net$ iperf -c 9.9.9.9 -p 6666
------------------------------------------------------------
Client connecting to 9.9.9.9, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 9.9.9.99 port 54526 connected with 9.9.9.9 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  2.71 GBytes  2.33 Gbits/sec

guodeqing@ubuntu1804:~/ebpf-test/net$ iperf -c 9.9.9.9 -p 6666
------------------------------------------------------------
Client connecting to 9.9.9.9, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 9.9.9.99 port 54548 connected with 9.9.9.9 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec   276 MBytes   231 Mbits/sec


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

guodeqing@ubuntu1804:~$ sudo iperf -c 172.17.0.3 -p 6666
------------------------------------------------------------
Client connecting to 172.17.0.3, TCP port 6666
TCP window size: 85.0 KByte (default)
------------------------------------------------------------
[  3] local 172.17.0.1 port 38238 connected with 172.17.0.3 port 6666
[ ID] Interval       Transfer     Bandwidth
[  3]  0.0-10.0 sec  2.65 GBytes  2.28 Gbits/sec

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

