
## 创建 requirements.txt

...
flask
...

安装 

```
pip install -r requirements.txt
// or
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
//  app.run() 
// 写app.run(debug=True) 时修改完代码刷新页面就行,否则需要重新启动app.py再刷新页面
// 只有设为host='0.0.0.0'时其他机器才可以访问到


```

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


navbar.html

```html

<h3><a href="/">home</a></h3>
<hr>

```



base.html

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

index.html

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
https://www.youtube.com/watch?v=FenI_wYBfJs&list=PLDFBYdF-BxV1G4FBpG1EMyFtbsbZuJOvD&index=6




