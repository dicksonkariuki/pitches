class Config:
    """
    General configuration parent class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dickson@localhost/pitch'


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