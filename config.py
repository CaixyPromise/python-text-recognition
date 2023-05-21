from config_message.Environment import (ACCESS_KEY, PERMANENT_SESSION_LIFETIME, PHOTO_TIMEOUT)


class Config:
    ACCESS_KEY = ACCESS_KEY
    PERMANENT_SESSION_LIFETIME = PERMANENT_SESSION_LIFETIME
    PHOTO_TIMEOUT = PHOTO_TIMEOUT

class DevelopmentConfig(Config):
    """开发模式的配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """生产环境配置信息"""
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}