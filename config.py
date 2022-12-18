import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))


# This class is created to prepare configs
class Config:
    # Email Server configurations are imported from environment variables below.
    SECRET_KEY = "dbc738ry489n4hkujerhgbjktrbgjrtkt584976fn4896tsws"
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_SUPPRESS_SEND = False
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = '2052456472@qq.com'
    MAIL_PASSWORD = 'yoxubsmwvmiybjff'
    FLASKY_MAIL_SUBJECT_PREFIX = '[MUSIC ZONE]'
    FLASKY_MAIL_SENDER = '2052456472@qq.com'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POST_PER_PAGE = 9
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Language
    LANGUAGES = ['en', 'zh']

    # directory config, for storing resources within the project
    app_direct = os.path.join(basedir, 'app')
    static_direct = os.path.join(app_direct, 'static')
    avatar_direct = os.path.join(basedir, 'app/static/storage', 'avatars')
    product_direct = os.path.join(basedir, 'app/static/storage', 'products')
    blog_direct = os.path.join(basedir, 'app/static/img', 'blog')

    @staticmethod
    def init_app(app):
        pass


# Development Database URL is configured here.
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # WTF_CSRF_ENABLED = False
    # Handle with browser not updating automatically
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=2)


# Testing Database URL is configured here.
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'


# Production Database URL is configured here.
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')


# config dictionary registered different environments(use development as default)
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
