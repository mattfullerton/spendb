import os
get = os.environ.get

DEBUG = False
ASSETS_DEBUG = False
CELERY_ALWAYS_EAGER = False
CACHE = True

SECRET_KEY = get('SECRET')

SQLALCHEMY_DATABASE_URI = get('DATABASE_URL')
CELERY_BROKER_URL = get('CLOUDAMQP_URL')

MAIL_SERVER = 'smtp.mandrillapp.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = False
MAIL_USERNAME = get('MANDRILL_USERNAME')
MAIL_PASSWORD = get('MANDRILL_PASSWORD')

MAIL_DEFAULT_SENDER = 'SpenDB <info@mapthemoney.org>'

AWS_KEY_ID = get('AWS_KEY_ID')
AWS_SECRET = get('AWS_SECRET')
AWS_DATA_BUCKET = get('AWS_DATA_BUCKET')