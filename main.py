from app import create_app
from flask_script import Manager
from flask_migrate import Migrate
from gevent import pywsgi

app = create_app("develop")
manager = Manager(app)
Migrate(app)


# 初始化管理员账号数据
@manager.command
def create_admin():
    pass

if __name__ == '__main__':
    server_port = 6006
    server = pywsgi.WSGIServer(('0.0.0.0', server_port), manager.app)
    print(f"Server is running on port {server_port}")  # 输出当前接口端口号
    server.serve_forever()