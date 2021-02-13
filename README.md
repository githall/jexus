### 希望
希望有能力的高手能将jexus开发成宝塔面板默认的与LAMP和LNMP环境平行的LJMP环境。

### 安装要求：
内存：512M以上，推荐768M以上（纯面板约占系统60M内存）
硬盘：300M以上可用硬盘空间（纯面板约占20M磁盘空间）
系统：CentOS 7.1+ (Ubuntu16.04+.、Debian9.0+)，确保是干净的操作系统，没有安装过其它环境带的Apache/Nginx/php/MySQL/pgsql/gitlab/java（已有环境不可安装）
架构：x86_64（主流服务器均是此架构），ARM不完整兼容（面板环境安装慢，部分软件可能安装不上）

宝塔Linux面板7.5.1版本是基于Centos/Debian/Ubuntu开发的，为了最好的兼容性，请使用以上系统
系统兼容性顺序：
Centos7.x > Debian10 > Ubuntu 20.04 > Cenots8.x > Ubuntu 18.04 > 其它系统
提示：Centos官方已宣布在2020年停止对Centos6的维护更新，各大软件开发商也逐渐停止对Centos6的兼容，新服务器不建议使用Centos6


以下主机商必看（开端口教程，不开不能用）：
腾讯云：https://www.bt.cn/bbs/thread-1229-1-1.html  腾讯云2折起
阿里云：https://www.bt.cn/bbs/thread-2897-1-1.html  阿里云2折起
华为云：https://www.bt.cn/bbs/thread-3923-1-1.html  华为云1折起

推荐先安装 堡塔SSH客户端 (免费/简单/中文/多屏)

Linux面板7.5.1安装命令：（推荐使用价格厚道，高性能v4的尊云zun.comKVM云服务器安装）使用SSH 连接工具（查看使用方法），挂载磁盘后（查看），根据系统执行框内命令开始安装（大约2分钟完成面板安装）
Centos安装命令：
yum install -y wget && wget -O install.sh http://download.bt.cn/install/install_6.0.sh && sh install.sh
复制代码

试验性Centos/Ubuntu/Debian安装命令 独立运行环境（py3.7） 可能存在少量兼容性问题 不断优化中  
curl -sSO http://download.bt.cn/install/install_panel.sh && bash install_panel.sh
复制代码

Ubuntu/Deepin安装命令：
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && sudo bash install.sh
复制代码
Debian安装命令：
wget -O install.sh http://download.bt.cn/install/install-ubuntu_6.0.sh && bash install.sh
复制代码
Fedora安装命令:
wget -O install.sh http://download.bt.cn/install/install_6.0.sh && bash install.sh
复制代码

Linux面板7.5.1升级命令：
curl http://download.bt.cn/install/update6.sh|bash
复制代码


以上节点无法使用的情况下，请使用下面的备用节点：

备用节点【江苏】：（宝塔推荐使用4核8G 100G BGP高防的尊云zun.com云服务器安装）
yum install -y wget && wget -O install.sh http://180.101.160.68:5880/install/install_6.0.sh && sh install.sh
复制代码

备用节点【香港】：（宝塔推荐使用CN2 双程GIA高品质，免备案的尊云zun.com香港云服务器安装）
yum install -y wget && wget -O install.sh http://103.224.251.67:5880/install/install_6.0.sh && sh install.sh
复制代码

备用节点【美国】：（宝塔推荐使用价格厚道，高性能v4的尊云zun.comKVM云服务器安装）
yum install -y wget && wget -O install.sh http://128.1.164.196:5880/install/install_6.0.sh && sh install.sh
复制代码

若点击更新后没生效，请尝试重启面板服务：
bt restart
复制代码
面板特色功能：
一键配置服务器环境（LAMP/LNMP）
一键安全重启
一键创建管理网站、ftp、数据库
一键部署SSL证书
一键部署源码（discuz、wordpress、dedecms、z-blog、微擎等等）
一键配置（定期备份、数据导入、伪静态、301、SSL、子目录、反向代理、切换PHP版本）
一键安装常用PHP扩展(fileinfo、intl、opcache、imap、memcache、apc、redis、ioncube、imagick)
数据库一键导入导出
系统监控（CPU、内存、磁盘IO、网络IO）
防火墙端口放行
SSH开启与关闭及SSH端口更改
禁PING开启或关闭
方便高效的文件管理器（上传、下载、压缩、解压、查看、编辑等等）
计划任务（定期备份、日志切割、shell脚本）
软件管理（一键安装、卸载、版本切换）

面板管理常用命令：https://www.bt.cn/btcode.html

#### [宝塔Linux面板ASP.NET管理器插件的使用视频教程](https://www.bilibili.com/video/BV14h411R7sd/) 建议先看视频。

### JexusWebAdmin

####  介绍
##### 应用名称：宝塔Linux面板ASP.NET 管理器插件
##### 价格：      ￥5.99
##### 作者：       IW3C
##### 功能介绍：在Linux 服务器上运行 ASP.NET 网站 并兼容Nginx 和 Apache
##### 支持版本：Centos / Ubuntu 64位 (不兼容32位)
##### 需要宝塔面板安装 Nginx 或者 Apache
##### 暂时只在 Python 2.7.5 环境下通过测试
##### 安装方法：下载 宝塔Linux版插件-ASP.NET 管理器V1.1 下的zip的安装包 , 然后在宝塔面板 -> 软件商店 -> 第三方应用 -> 导入插件 中导入安装包

项目维护QQ群： 427901182

### Jexus最新版7.0的安装
#### Jexus的手工安装或更新步骤（以Jexus v7.0为例）：
#### 1、获取：cd /tmp && wget https://linuxdot.net/down/jexus-7.0.x-x64.tar.gz
#### 2、解压：sudo tar -zxvf jexus-7.0.x-x64.tar.gz
#### 3、移动：sudo mv jexus /usr/
#### 4、初始：cd /usr/jexus && sudo ./jws init
#### 强调：如果之前安装有其它版本的Jexus，在安装新版前应该停止旧版Jexus运行，并将 /usr/jexus 文件夹更名备份。

### 关于Jexus的系统服务操作要点
之前，Jexus开机自启动的实现是在 /etc/rc.local 中添加 “/usr/Jexus/jws start” 启动命令实现的，为了更符合当代linux操作习惯，新版Jexus添加了systemd 服务脚本（jws.service），以方便大家将Jexus作为系统服务进行管理。

#### 一、有关操作：

1，服务安装：sudo systemctl enable /usr/jexus/jws.service

2，服务卸载：sudo systemctl disable jws.service

3，服务启动：sudo systemctl start jws

4，服务重启：sudo systemctl restart jws

5，服务停止：sudo systemctl stop jws
####  二、要点：

1、服务安装前一定要注意：

1）查看 /usr/jexus文件夹中是否存在jws.service 文件，如果没有这个文件，请重新安装Jexus。

2）一定要运行一次初始化命令：sudo /usr/Jexus/jws init

2、安装为服务后，下列命令不要再使用：

sudo /usr/Jexus/jws start

sudo /usr/Jexus/jws stop

sudo /usr/Jexus/jws restart

### 无图无真相
![输入图片说明](https://images.gitee.com/uploads/images/2020/0927/213539_cdd7a1f9_1204490.jpeg "1.jpg")

![输入图片说明](https://images.gitee.com/uploads/images/2020/0927/213551_d6f7ebf4_1204490.jpeg "2.jpg")

![输入图片说明](https://images.gitee.com/uploads/images/2020/0927/213603_e99b958b_1204490.jpeg "3.jpg")

### Jexus使用相关教学视频

#### 
#### 
#### 
#### 
#### 


