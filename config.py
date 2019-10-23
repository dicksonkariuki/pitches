class Config:
    """
    General configuration parent class
    """
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