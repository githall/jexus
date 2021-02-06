#!/usr/bin/python
# coding: utf-8

#+--------------------------------------------------------------------
#|   Version:1.0
#+--------------------------------------------------------------------
import sys,os,json,base64
import re,psutil,requests

#设置运行目录
os.chdir("/www/server/panel")

#添加包引用位置并引用公共包
sys.path.append("class/")
import public


#在非命令行模式下引用面板缓存和session对象
if __name__ != '__main__':
    from BTPanel import cache,session

class Jexus_main:
    __plugin_path = "/www/server/panel/plugin/Jexus/"
    __config = None

    #构造方法
    def  __init__(self):

        if not os.path.exists(self.__plugin_path + 'config/'):
            os.mkdir(self.__plugin_path + 'config/')
            os.mkdir(self.__plugin_path + 'config/Site/')
            os.mkdir(self.__plugin_path + 'config/Info/')
            self.sys_config('')
        if not os.path.exists(self.__plugin_path + 'logs/'):
            os.mkdir(self.__plugin_path + 'logs/')
            self.sys_config('')
        pass

    #检查当前是否已经安装mono 环境
    def sys_version(self,args):
        shell=os.popen('sudo -i /www/server/jexus/jws -v')
        info = shell.readline()
        if re.findall(r'-bash: /www/server/jexus/jws: No such file or directory', info):
            return json.dumps({'status': 'uninstall', 'mono': '0.0.0.0', 'jexus': '0.0.0.0'})
        else:
            info = shell.readlines()
            mono = info[3].split(' ')[0].split('/')[1]
            jexus = info[0].split(' ')[0].split('/')[1]
            return json.dumps({'status': 'install', 'mono': mono , 'jexus': jexus})

    #配置Jexus 的设置信息
    def sys_config(self,args):
        if not hasattr(args,'process'):
            config={'logs': self.__plugin_path + 'logs/', 'siteconf': self.__plugin_path + 'config/Site', 'http_process': 2, 'http_MaxMemory': 0, 'http_MaxCpuTime': 7200, 'http_MaxConnIp': 0 }
        else:
            config={'logs': self.__plugin_path + 'logs/', 'siteconf': self.__plugin_path + 'config/Site', 'http_process': args.process, 'http_MaxMemory': args.Memory, 'http_MaxCpuTime': args.CpuTime, 'http_MaxConnIp': args.ConnIp}
        #将config 写入sys.config 文件
        public.WriteFile(self.__plugin_path + 'config/sys.config',json.dumps(config))
        config = json.loads(public.readFile(self.__plugin_path + 'config/sys.config'))
        #将config 数组按照指定格式写入 /jws.conf
        Jws='''
        SiteLogDir=%s
        SiteConfigDir=%s
      
        httpd.processes=%s          #: 1-24. (0 is auto)
        httpd.MaxTotalMemory=%s     #: In megabytes. Set to 0 for auto.
        httpd.MaxCpuTime=%s         #: In seconds. Set to 0 for unlimited.
        httpd.MaxConnPerIp=%s       #: 0 is unlimited
	  
	    # httpd.User=www-data
        # php-fcgi.set=/usr/bin/php-cgi,8

        # HTTPS/SSL Global default configuration
        ##########################################

        # CertificateFile    = /xxxx/xx.crt
        # CertificateKeyFile = /xxxx/xx.key
        # SSL_TLS_Version    = TLSv1.1 TLSv1.2   #  TLSv1.0  TLSv1.1  TLSv1.2, default is SSLv23
        # SSL_Ciphers        = ECDHE-RSA-AES256-GCM-SHA384:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4:!DH:!DHE
      '''%(config['logs'],config['siteconf'],config['http_process'],config['http_MaxMemory'],config['http_MaxCpuTime'],config['http_MaxConnIp'])
        public.WriteFile('/www/server/jexus/jws.conf',Jws)
        if not self.sys_status():
            self.Site_SetDefault()
            os.popen('sudo -i /www/server/jexus/jws start')
        os.popen('sudo -i /www/server/jexus/jws restart')
        self.Site_ConfigAllStart()
        return json.dumps({'status':'Success','mes':'Set Jexus Gobal Config Success!'})

    #控制jexus的启动、停止、重启
    def sys_control(self,args):
        cmd='sudo -i /www/server/jexus/jws '+args.cmd
        os.popen(cmd)
        if args.cmd != "stop":
            self.Site_ConfigAllStart()
        return json.dumps({'status': 'Success', 'mes': args.cmd+'Jexus Service Success!'})

    #读取当前系统的详细信息:
    def sys_info(self,args):
        if self.sys_status():
            status='run'
        else:
            status='stop'
        config=json.loads(public.readFile(self.__plugin_path + 'config/sys.config'))
        autorun=self.sys_autorun()
        res={'status':"Success", 'service': status, 'process': config['http_process'], 'Memory': config['http_MaxMemory'], 'CpuTime': config['http_MaxCpuTime'], 'ConnIp': config['http_MaxConnIp'], 'AutoRun': autorun}
        return json.dumps(res)



    #判断系统的运行状态
    def sys_status(self):
        shell=os.popen('sudo -i /www/server/jexus/jws status')
        info = shell.readline()
        if re.findall('Jexus has stopped.',info):
            return False
        else:
            return True

    # 查看当前系统开机启动命令的状态
    def sys_autorun(self):
        chk = os.popen('chkconfig --list BT_Jexus')
        info = chk.readlines()
        if not info:
            return 'off'
        else:
            return 'on'

    # 设置系统的开机启动命令
    def sys_SetAutorun(self,args):
        status=self.sys_autorun()
        if status == 'on':
            #关闭开机启动
            osys = system_info()
            System = osys.GetSystemVersion()
            if re.findall(r'CentOS', System):
                os.popen('chkconfig --del BT_Jexus')
            elif re.findall(r"Debian", System) or re.findall(r'Ubuntu', System):
                os.open('sudo update-rc.d -f BT_Jexus remove')
            os.popen('rm -rf /etc/rc.d/init.d/BT_Jexus')
        else:
            #启动开机启动
            self.WGetDownload("https://gitee.com/githall/jexus/blob/master/BT_Jexus","/www/server/panel/plugin/Jexus/BT_Jexus")
            os.popen('cp ' + self.__plugin_path + 'BT_Jexus /etc/init.d/BT_Jexus')
            osys = system_info()
            System = osys.GetSystemVersion()
            if re.findall(r'CentOS', System):
                # 注册开机启动
                os.popen('chkconfig --add BT_Jexus')
            elif re.findall(r"Debian", System) or re.findall(r'Ubuntu', System):
                os.open('sudo update-rc.d BT_Jexus defaults')
            else:
                return json.dumps({'status': 'Failed', 'msg': '错误!Jexus暂时不兼容您的系统开机启动'})
        return json.dumps({'status': 'Success'})


    #读取系统日志信息
    def sys_log(self,args):
        if not hasattr(args, 'Site'):
            log='jws.log'
        else:
            log=args.Site
        if not os.path.exists(self.__plugin_path+'logs/'+log):
            response={'status':'Failed', 'msg': '日志文件不存在'}
            return json.dumps(response)
        content=public.readFile(self.__plugin_path+'logs/'+log)
        response = {'status': 'Success', 'msg': '','body':content}
        return json.dumps(response)

    #添加默认站点 localhost
    def Site_SetDefault(self):
        Default='''
        port=2333
        root=/ /www/server/panel/plugin/Jexus/config/DefaultSite/
        indexs=index.aspx
        host=*
        nofile= /404.html
        nolog=no 
        '''
        public.WriteFile('/www/server/panel/plugin/Jexus/config/Site/Default',Default)
        #下载默认站点文件
        self.WGetDownload("https://gitee.com/githall/jexus/raw/master/DefaultSite.tar.gz",self.__plugin_path+'DefaultSite.tar.gz')
        os.popen("cd "+self.__plugin_path+" && tar -zxvf "+self.__plugin_path+'DefaultSite.tar.gz')
        os.popen("mv "+self.__plugin_path+"DefaultSite "+self.__plugin_path+'config/')
        os.popen("rm -rf "+self.__plugin_path+'DefaultSite.tar.gz')

    #添加新的站点
    def Site_add(self,args):
        if os.path.exists(self.__plugin_path + 'config/Info/' + args.Name+'.json'):
            return json.dumps({'status': 'Failed', 'msg': '添加新站点失败，已经存在同名站点'})
        else:
            Info = json.dumps({'SiteName': args.Name, 'SitePath': args.Path, 'SiteDomain': args.Domain, 'SiteStatus': 'new', 'SiteId': ''})
             # 写入到Info文件夹
            public.WriteFile(self.__plugin_path + 'config/Info/' + args.Name + '.json', Info)
            domian = args.Domain.split('\n')
            Domain = ''
            list = []
            num = 0
            for _domain in domian:
                if Domain=="":
                    Domain=_domain
                else :
                    Domain = Domain + ',' + _domain
                    if not num == 0:
                        list.append(_domain)
                num = num + 1
        # 写入到Jexus的网站配置文件夹
            Config = '''
        port=2333
        root=/ %s
        indexs=index.aspx
        host=%s 
        nofile= /404.html
        nolog=no 
        ''' % (args.Path, Domain)
            public.WriteFile(self.__plugin_path + 'config/Site/' + args.Name, Config)
            count = num - 1
            webname = {'domain': domian[0], "domainlist": list, "count": count}
            return json.dumps({'status': 'Success', 'msg': '添加新站点成功', 'webname': webname, 'sitename': domian[0]})

    #启动指定的站点
    def Site_Start(self,args):
        SiteName = args.sitename.strip()
        # 读取站点的配置
        config = json.loads(public.readFile(self.__plugin_path + "config/Info/" + SiteName+'.json'))
        if config['SiteStatus'] == "new":
            # 下载并解压默认网站文件
            os.popen("rm -rf " + config['SitePath'] + "/*")
            self.WGetDownload("https://gitee.com/githall/jexus/raw/master/NewSite.tar.gz", config['SitePath'] + '/NewSite.tar.gz')
            os.popen("cd " + config['SitePath'] + "  && tar -zxvf NewSite.tar.gz")
            os.popen("sudo -i && rm -rf " + config['SitePath'] + "/NewSite.tar.gz")
            config['SiteId'] = args.id
        config['SiteStatus'] = 'start'
        public.WriteFile(self.__plugin_path + "config/Info/" + SiteName+'.json', json.dumps(config))
        os.popen("/www/server/jexus/jws start " + SiteName)
        return json.dumps({'status': 'Success', 'msg': '启动站点成功'})




    #停止指定的站点
    def Site_Stop(self,args,):
        SiteName=args.sitename.strip()

        config = json.loads(public.readFile(self.__plugin_path + "config/Info/" + SiteName + '.json'))
        config['SiteStatus'] = 'stop'
        public.WriteFile(self.__plugin_path + "config/Info/" + SiteName + '.json', json.dumps(config))
        os.popen("/www/server/jexus/jws stop " + SiteName)
        return json.dumps({'status': 'Success', 'msg': '停止站点成功'})


    #删除指定的站点
    def Site_Del(self,args):
        SiteName = args.sitename.strip()
        #停用指定的站点
        self.Site_Stop(args)
        config = json.loads(public.readFile(self.__plugin_path + "config/Info/" + SiteName + '.json'))
        SiteId=config['SiteId']
        domain = config['SiteDomain'].split('\n')[0]
        #删除配置文件
        os.popen("cd " + self.__plugin_path + "config/Info/  && rm -rf " + SiteName + ".json")
        os.popen("cd " + self.__plugin_path + "config/Site/  && rm -rf " + SiteName)
        return json.dumps({'status': 'Success', 'msg': '删除站点成功', 'domain': domain, 'siteid': SiteId})

    #重启指定的站点
    def Site_Restart(self,args):
        self.Site_Stop(args)
        self.Site_Start(args)
        return json.dumps({'status': 'Success', 'msg': '重启站点成功'})

    #获取指定站点的配置信息
    def Site_Info(self,args):
        SiteName = args.sitename.strip()
        config = json.loads(public.readFile(self.__plugin_path + "config/Info/" + SiteName + '.json'))
        return json.dumps({'status': 'Success', 'info':config})



    #配置指定的站点
    def Site_Config(self,args):
        SiteName = args.sitename.strip()
        # 停用指定的站点
        self.Site_Stop(args)
        config = json.loads(public.readFile(self.__plugin_path + "config/Info/" + SiteName + '.json'))
        #更新配置
        config['SiteName'] = SiteName
        config['SitePath'] = args.path
        config['SiteDomain'] = args.domain
        config['SiteStatus'] = 'start'
        public.WriteFile(self.__plugin_path + "config/Info/" + SiteName + '.json', json.dumps(config))
        domian = config['SiteDomain'].split('\n')
        Domain = ''
        for _domain in domian:
            if Domain == "":
                Domain = _domain
            else:
                Domain = Domain + ',' + _domain
        # 写入到Jexus的网站配置文件夹
        Config = '''
               port=2333
               root=/ %s
               indexs=index.aspx
               host=%s   
               nofile= /404.html
               nolog=no 
               ''' % (args.path, Domain)
        public.WriteFile(self.__plugin_path + 'config/Site/' + SiteName, Config)
        self.Site_Start(args)
        return json.dumps({'status': 'Success', 'msg': '配置站点成功'})



    #获取当前的站点列表
    def Site_List(self,args):
        list=[]
        num=0
        for file in os.walk(self.__plugin_path + "config/Info/"):
            files = file[2]
        for SiteName in files:
            config = public.readFile(self.__plugin_path + "config/Info/" + SiteName)
            list.append(config)
            num=num+1
        return  json.dumps({'status': 'Success', 'list': list ,'num': num})

    #变更所有站点的状态为start
    def Site_ConfigAllStart(self):
        for file in os.walk(self.__plugin_path + "config/Info/"):
            files = file[2]
        for SiteName in files:
            config = json.loads(public.readFile(self.__plugin_path + "config/Info/" + SiteName))
            config['SiteStatus'] = 'start'
            public.WriteFile(self.__plugin_path + "config/Info/" + SiteName, json.dumps(config))


    def WGetDownload(self,url,filename):
        os.popen('rm -rf '+filename+' && wget -O '+filename+'  --no-check-certificate '+url)
