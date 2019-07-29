
## 创建 requirements.txt

...
flask
...

安装 

```python
pip install -r requirements.txt
# or
pip install flask

```

## 第一个 Hello World 程序

### 创建 app.py

```python
from flask import Flask

app = Flask(__name__ )


@app.route('/')

def index():
    return 'hello world'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000) 
#  app.run() 
# 写app.run(debug=True) 时修改完代码刷新页面就行,否则需要重新启动app.py再刷新页面
# 只有设为host='0.0.0.0'时其他机器才可以访问到



```
### 问题
本机打不开 0.0.0.0:3000
需要找到本机的本地ip 才能打开 198.162.0.11:3000 



## 利用 render_template 渲染界面 

app.py
```python
def index():
    return '<h1>hello world</h1><p>i love flask </p>'

```

创建 templates/index.html 

文件夹名一定要是templates

```html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{title}}</title>
</head>
<body>

        <h1>hello world</h1><p>i love flask </p>
    
</body>
</html>

```

修改 app.py

```python

from flask import Flask ,render_template

...
def index():
    title = "Flask web app"
    return render_template('index.html' , title = title )

```


## 利用循环和判断语句控制 template 的渲染 

app.py

```python
def index():
    paragraphs = [
        'Section 1 ',
        'Section 1 ',
        'Section 1 ',
    ]
    return render_template('index.html' , title = title , paragraphs=paragraphs )


```

index.html 里用的 是和 twig 相似的语法 

```html

{% if   title    %}

    {% else %}
        {% set title = 'this is default title '%}
    {% endif %}
<title>{{ title }}</title>

```


## 模板继承和引用


templates/navbar.html

```html

<h3><a href="/">home</a></h3>
<hr>

```



templates/base.html

```html

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    {% if   title    %}

    {% else %}
    {% set title = 'this is default title '%}
    {% endif %}
    <title>{{ title }}</title>
</head>

<body>
    {% block body %}
        {% include 'navbar.html' %}

        {% block content %}
              <p> parent content block </p>
         {% endblock %}
    {% endblock %}

   


</body>

</html>

```

templates/index.html

```html
{% extends 'base.html' %}

{% block body %}
    {{ super() }}
    <h1 style="color:red">hello world</h1>
    <p>i love flask </p>
    <p>{{pp}}</p>

    {% for p in  paragraphs %}
        <p>{{p}}</p>
    {% endfor %}

{% endblock %}

```




## 利用 flask bootstrap 来优化布局 

requirements.txt 

...
    +flask-bootstrap
...

app.py
...
    +from flask_bootstrap import Bootstrap
    +bootstrap = Bootstrap(app)
...

base.hml
...
{% extends 'bootstrap/base.html' %}
...

或者直接载入
 <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">


 

## flask-sqlalchemy 简介和创建用户模型

requirements.txt
```txt
    +flask-sqlalchemy

```

```bash
$ pip install flask-sqlalchemy
```

app.py

```python
    +from flask_sqlalchemy import SQLAlchemy
    +from config import Config
    +db = SQLAlchemy(app)
    +app.config.from_object(Config)
```

config.py

```python
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Database configuration
    # os.environ.get('DATABASE_URL') 从环境变量里获取DATABASE_URL 如果没有 则: 'sqlite:///' + os.path.join(basedir , 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir , 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


```

models.py
```python
from app import db 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120),    nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```

### 测试一下

```bash
$ python

>>>
    from models import db
    db.reate_all()
    from models import User
    User.query.all()#查找所有user 返回[]
    user = User(username='Jack', password='pwd' , email="example@example.com") # 准备数据

    #插入数据
    db.session.add(user)
    db.session.commit() # 加commit 确认操作

    #查看数据
    User.query.all() # [<User 'Jack'>]

    u = User.query.all()
    u = u[0]
    u.username
    u.email
    u.password

    User.query.delete() #清空数据
    User.query.all()
    db.session.commit()

```


## 利用 Flask WTF 来创建用户注册表单

https://www.youtube.com/watch?v=6XPxQKdBySU&list=PLDFBYdF-BxV1G4FBpG1EMyFtbsbZuJOvD&index=8


