#!/usr/bin/python
#coding:utf-8
#FileName:Client.py
import socket,time
socket.setdefaulttimeout(2)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IPLISTS = ['182.92.103.85','192.168.0.211']
IPVERSION = '0.0.1'
class UseServer:
    def Connect(port = 18702):
        for times in range(0,(len(IPLISTS))):
            try:
                print ('正在连接第 %i 台服务器'%(int(times)+1))
                ADDR = (IPLISTS[times],port)
                s.connect(ADDR)
            except(ConnectionRefusedError):
                print ('第 %i 台服务器连接失败'%(int(times)+1))
                continue
            except(OSError):
                print ('您的计算机可能无法正常连接网络，请检查')
                break
            else:
                print ('连接服务器 %s 成功'%IPLISTS[times])
                global ConnectStat
                ConnectStat = 'Success'
                break
        ConnectStat = 'Failed'
    def CheckIPUpdate():
        Version = IPLISTS[-1]
        if ConnectStat == 'Success':
            try:
                GetVersion = s.recv(5)
            except:
                print ('检查更新失败，跳过')
            else:
                GetVersion = GetVersion.decode('utf-8')
                if float(GetVersion) > float(IPVERSION):
                    VersionStat = 'old'
                    s.send(VersionStat.encode('utf-8'))
                else:
                    VersionStat = 'new'
                    s.send(VersionStat.encode('utf-8'))
        else:
            pass
    def Login():
        while True:
            LoginName = input("请输入您想作为在线的账号(可以使用中文，英文，数字)：")
            if len(LoginName) >= 15:
                print ('名称不可以过长哦，请重新输一个~')
            elif (len(LoginName)) == 0:
                    print ('名字是一定要有的~~没有就傻傻分不清楚')
            else:
                break
    def SendName():
        LoginName = LoginName.encode('utf-8')
        s.send(LoginName)
    def SendLoginUDP():
        udps = socket.socket(socket.AF_INIT,socket.SOCK_DGRAM)
def Surface():
    print (
    """
    无踪 v0.1.0 —— 新的没有GUI的安全聊天

    
    按下相对应的键选择功能：


    
              【1.查看说明】     【2.登陆】     【3.注册永久账号】

    

    建议您在使用之前看一下说明哦~~

                                         作者：guiqiqi187@gamil.com
    """)
    time.sleep(10.0)
Surface()
