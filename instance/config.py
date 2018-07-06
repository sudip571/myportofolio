import os

# grab the folder of the top-level directory of this project
# BASEDIR=C:\Users\aitss\source\repos\Portofolio\Portofolio\instance
# TOP_LEVEL_DIR=C:\Users\aitss\source\repos\Portofolio\Portofolio
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)


SECRET_KEY = '\xfa\x93\x882\xff\x1a"\xf5L\x9a0xy\xfd\x88\x13\x018\xc6\xa3'
if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:aits567$@localhost/merodb'
else:
    # for production
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:aits567$@localhost/merodb'

# Uploads
UPLOADS_DEFAULT_DEST= TOP_LEVEL_DIR +'/Portofolio/static/projectimage/'

# Mail sending configuration
#MAIL_SERVER = 'smtp.googlemail.com'
#MAIL_PORT = 465
#MAIL_USE_TLS = False
#MAIL_USE_SSL = True
#MAIL_USERNAME = 'srbportofolio.gmail.com'
#MAIL_PASSWORD = 'aits567$'
#MAIL_DEFAULT_SENDER = 'srbportofolio.gmail.com'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'srbportofolio.gmail.com'
MAIL_PASSWORD = 'aits567$'
MAIL_DEFAULT_SENDER = 'srbportofolio.gmail.com'

# Mail Receiver
EMAIL_RECEIVER='aits.sudip.ranabhat@gmail.com'

# Set session time
#PERMANENT_SESSION_LIFETIME=10