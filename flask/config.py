import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Database configuration
    # os.environ.get('DATABASE_URL') 从环境变量里获取DATABASE_URL 如果没有 则: 'sqlite:///' + os.path.join(basedir , 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir , 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 

