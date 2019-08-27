from flask_restful import Api

from App.views.HelloApi import Hello

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(Hello, '/', methods=["GET", "POST", "PUT", "DELETE"])
