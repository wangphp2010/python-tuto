import configparser as cp 

# 配置文件路径

filename = './config.ini'

# 配置文件读入

inifile = cp.ConfigParser()
inifile.read(filename,'UTF-8')

# 读取 db部分

print( "db.ip = " , inifile.get("db","ip") )
print( "db.port = " , inifile.get("db","port") )
print( "db.uid = " , inifile.get("db","uid") )
print( "db.pwd = " , inifile.get("db","pwd") )


# 读取 web部分
print( "web.uid = " , inifile.get("web","uid") )
print( "web.pwd = " , inifile.get("web","pwd") )

#另一张读取方式
print( "web.pwd = " , inifile["web"]["pwd"] )

#设置新内容 
#设置新内容 
inifile["web"]["ip"] = "192.168.1.2"
with open(filename,'w') as configfile:
    inifile.write(configfile)

print( "web.ip = " , inifile["web"]["ip"] )


