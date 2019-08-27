from flask_restful import Api

from App.views.HelloApi import Hello
from App.views.UserApi import UserResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(Hello, '/', methods=["GET", "POST", "PUT", "DELETE"])

# api.add_resource(UserResource, '/users/', methods=["GET", "POST", "PUT", "DELETE"])

api.add_resource(UserResource, '/users/', methods=["GET", "POST", "PUT", "DELETE"])
