from flask import Flask, Blueprint
from flask_cors import CORS
from inspect import getmembers

import api.views

# 工厂函数，插件注册，蓝图注册


def create_app(conf_obj="settings"):
    app = Flask(__name__.split(".")[0])
    app.config.from_object(conf_obj)
    CORS(app)
    register_blueprint(app)

    return app


def register_blueprint(app):
    for item in getmembers(api.views):
        if item[0].startswith("blueprint") and isinstance(item[1], Blueprint):
            app.register_blueprint(item[1])
