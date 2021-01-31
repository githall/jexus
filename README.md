### 希望
希望有能力的高手能将jexus开发成宝塔面板默认的与LAMP和LNMP环境平行的LJMP环境。


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
#### 
#### 
#### 

