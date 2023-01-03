# 介绍
python3通过执行系统命令调用clamav对指定目录进行扫描，并输出其md5的值
- 环境
python3.6.8
- 系统
centos

# 安装
- Centos

Centos上安装的步骤可能多一丢丢，首先需要配置个网络源，然后执行这两条安装

```
yum install epel-release -y
yum install clamav clamav-update clamav-server clamav-server-systemd clamav-data clamav-filesystem clamav-scanner-systemd clamav-devel clamav-lib clamav-server-systemd clamav-update clamav-scanner-systemd -y
```

接着开启服务，以及开机自启动

```
systemctl start clamav-freshclam
systemctl enable clamav-freshclam

systemctl start clamav-daemon
systemctl enable clamav-daemon
```

（ps: start clamav-daemon的时候可能会报错，但是我环境中没有影响我的使用)

- Ubuntu

ubuntu就简单的多

```
apt install clamav
```



安装完成后，可以通过以下命令实现病毒库的更新

```
freshclam
```

ClamAV 还有许多其他的用法，例如在后台运行定期扫描、扫描特定的文件夹或文件等。可以使用 `man clamscan` 命令查看详细的用法。

# 使用方法
```
python3 scan.py
```
然后输入目录

效果如下：

