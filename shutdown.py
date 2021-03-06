# -*- coding: utf-8 -*-


def sendmail():
    """发送邮件提示"""
    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header
    
    import config
    
    # 第三方 SMTP 服务
    mail_host = config.mail_host    # 服务器
    mail_user = config.mail_user    # 用户名
    mail_pass = config.mail_pass    # 口令 
    mail_port = config.mail_port    # 端口
    
    sender = '1137813060@qq.com'        # 由此用户代发
    receivers = ['1137813060@qq.com']   # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
    message = MIMEText('您的主机状态良好，继续运行中...', 'plain', 'utf-8')
    message['From'] = Header("您的主机", 'utf-8')       # 发送者
    message['To'] =  Header("主人", 'utf-8')            # 接收者

    subject = '正常运行提示(程序自动发送)-SYF'
    message['Subject'] = Header(subject, 'utf-8')
    
    try:
        smtpObj = smtplib.SMTP(mail_host, mail_port)    # mail_port 为 SMTP 端口号
        smtpObj.starttls()
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


import os
import time

import status

if __name__=='__main__':
    while True:
        time.sleep(1800)        # 半个小时(1800秒)运行一次
        shutdowns = status.network_status()
        if(shutdowns == 1):
            print("五分钟后自动关机")
            os.system('shutdown -a')                    # 取消关机
            os.system('shutdown -s -t {}'.format(300))  # 五分钟后关机
            break
        else:
            print("状态正常，继续运行")
            sendmail()      # 发送邮件提示