from flask import Flask
from config import config_map
from flask_session import Session
# from flask_wtf import CSRFProtect

# 创建redis
redis_store = None


# 工厂模式
def create_app(config_name):
    """
    创建flask的应用对象
    :param config_name: str  配置模式的模式的名字 ("develop",  "product")
    :return:
    """
    app = Flask(__name__, static_url_path='/static',
                static_folder='static',
                template_folder='templates')
    

    # 根据配置模式的名字获取配置参数的类
    config_class = config_map.get(config_name)
    app.config.from_object(config_class)

    # 初始化redis

    # 利用flask-session，将session数据保存到redis中
    Session(app)
    # flask-csrf防护
    # CSRFProtect(app)

    # 注册
    from app import public
    app.register_blueprint(public.public, url_prefix = '/')

    return app
