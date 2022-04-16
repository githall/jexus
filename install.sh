#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#配置插件安装目录
install_path=/www/server/panel/plugin/Jexus/

#安装
Install()
{
	
	echo '正在安装...'

    sudo wget --no-check-certificate https://linuxdot.net/down/jexus-7.0.x-x64.tar.gz
    sudo tar -zxvf jexus-7.0.x-x64.tar.gz
    sudo mv jexus /www/server/jexus
    sudo rm -rf jexus-7.0.x-x64.tar.gz
    
    #设置程序可执行
    sudo chmod +x /www/server/jexus/jws
    
    #初始化
    sudo /www/server/jexus/jws init
    
    #设置开机启动
    sudo systemctl enable /www/server/jexus/jws.service
    
    #移动默认配置文件到jexus目录
    sudo mv /www/server/jexus/siteconf/default /www/server/jexus/

   
	echo '================================================'
	echo '安装完成'
}

#卸载
Uninstall()
{
	rm -rf $install_path
	rm -rf /www/server/jexus/
}

#操作判断
if [ "${1}" == 'install' ];then
	Install
elif [ "${1}" == 'uninstall' ];then
	Uninstall
else
	echo 'Error!';
fi
