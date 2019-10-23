class Config:
    """
    General configuration parent class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("SSQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dickson@localhost/pitch'
    SECRET_KEY =os.environ..get("SECRET_KEY")



class ProdConfig(Config):
    """
    Production configuration child class
    args:
        Config:The parent configuration class with general configuration settings
    """
    pass
class DevConfig(Config):
    """
    Development configuration class 
    args:
        Config:parent configuration class that contains general configuration settings
    """
    DEBUG = True

    config_options = {
        'development':DevConfig,
        'production':ProdConfig
    }