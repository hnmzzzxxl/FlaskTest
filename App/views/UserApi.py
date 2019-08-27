from flask_restful import Resource, reqparse, fields, marshal_with

### 请求参数
from App.ext import db
from App.models import User

user_fields = {
    "id": fields.Integer,
    "account": fields.String,
    "t_id": fields.Integer(attribute='team_id'),
    "t_role": fields.Integer(attribute='team_role'),
    "url": fields.Url("userresource", absolute=True)
}

res_user_fields = {
    "msg": fields.String,
    "status": fields.String,
    "data": fields.Nested(user_fields)
}

parse = reqparse.RequestParser()
parse.add_argument("account", required=True, help="must supply account")


class UserResource(Resource):

    def get(self):
        pass

    @marshal_with(res_user_fields)
    def post(self):
        user = User()

        parser = parse.parse_args()

        account = parser.get("account")

        user.account = account

        db.session.add(user)

        db.session.commit()

        data = {
            "msg": "ok",
            "status": "200",
            "data": user
        }

        return data

    def put(self):
        pass

    def delete(self):
        pass
