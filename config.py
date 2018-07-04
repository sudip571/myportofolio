
class BasicConfig(object):

    DEBUG = False
    TESTING = False

class DevelopmentConfig(BasicConfig):

    DEBUG = True
    #TESTING = True
    SQLALCHEMY_ECHO = True
    DEVELOPMENT = True
    ENV = 'Development'

class ProductionConfig(BasicConfig):

    DEBUG = False
    TESTING = False
    ENV = 'Production'


app_config = {
    
    'dev':DevelopmentConfig,
    'pro': ProductionConfig,
    'default' : DevelopmentConfig
    
    }

