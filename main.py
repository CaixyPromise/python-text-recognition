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
    
    # from app.models import Admin
    # from config_message.Environment import ADMIN_USERNAME, ADMIN_PASSWORD, ADMIN_ID
    # try:
    #     admin_new = Admin(id = ADMIN_ID, username=ADMIN_USERNAME, password=ADMIN_PASSWORD, )
    #     db.session.add(admin_new)
    #     db.session.commit()
    #     print("初始化成功")
    # except:
    #     print("初始化失败")
    #     db.session.rollback()


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 6006), manager.app)
    server.serve_forever()