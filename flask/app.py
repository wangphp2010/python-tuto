from flask import Flask , render_template
""" from flask_bootstrap import Bootstrap
 """

from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
""" bootstrap = Bootstrap(app) """

db = SQLAlchemy(app)
app.config.from_object(Config)
 
@app.route('/')
def index():
    title = "Flask web app"
    pp = 'i love pp flask'
    paragraphs = [
        'Section 1 ',
        'Section 1 ',
        'Section 1 ',
    ]
    return render_template('index.html' , title = title , pp = pp , paragraphs=paragraphs    )

@app.route('/contact')
def contact():
    
     
    return  '<h1>contact page </h1>'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)