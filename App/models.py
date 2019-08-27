from App.ext import db


class Team(db.Model):
    __table__name = 'team'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    t_name = db.Column(db.String(64), unique=True)
    t_leader = db.Column(db.String(64), unique=True)


class User(db.Model):
    __table__name__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account = db.Column(db.String(64), unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)
    team_role = db.Column(db.Integer, default=0)
