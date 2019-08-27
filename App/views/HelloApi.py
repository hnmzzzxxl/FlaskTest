from flask_restful import Resource


class Hello(Resource):

    def get(self):
        return {"msg": "get"}

    def post(self):
        return {"msg": "post"}

    def put(self):
        return {"msg": "put"}

    def delete(self):
        return {"msg": "delete"}
