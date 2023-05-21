from flask import Blueprint

# 创建蓝图对象
public = Blueprint("public", __name__)

from . import views

