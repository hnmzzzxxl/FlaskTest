from flask import Flask
from App.ext import init_ext
from App.settings import envs
from App.views import init_api


def create_app(env):
    app = Flask(__name__)

    # 初始化App
    app.config.from_object(envs.get(env))

    # 初始化Api资源
    init_api(app=app)

    # 初始化扩展库
    init_ext(app=app)

    return app
