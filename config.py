# -*- coding: utf-8 -*-
 
import configparser


# 调用读取配置模块中的类
config = configparser.ConfigParser()
config.read("SMTP.ini", encoding="utf-8")

# 调用get方法，然后获取配置的数据
mail_host = config.get("email_qq","mail_host")
mail_user = config.get("email_qq","mail_user")
mail_pass = config.get("email_qq","mail_pass")
mail_port = config.get("email_qq","mail_port")