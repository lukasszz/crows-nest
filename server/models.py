from datetime import datetime

from server import db


class Server(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tms = db.Column(db.DateTime, index=True, default=datetime.now)
    name = db.Column(db.String(64), index=True, unique=True)
    ip = db.Column(db.String(64), index=True, unique=True)


# class Agent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     tms = db.Column(db.DateTime, index=True, default=datetime.now)
#     name = db.Column(db.String(64), index=True, unique=True)


# class ServerAgents(db.Model):
#     """ What should be reported by the server"""
#     id = db.Column(db.Integer, primary_key=True)
#     tms = db.Column(db.DateTime, index=True, default=datetime.now)
#     id_server = db.Column(db.Integer, db.ForeignKey('server.id'))
#     id_agent = db.Column(db.Integer, db.ForeignKey('agent.id'))


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tms = db.Column(db.DateTime, index=True, default=datetime.now)
    id_server = db.Column(db.Integer, db.ForeignKey('server.id'))
    # id_agent = db.Column(db.Integer, db.ForeignKey('agent.id'))
    agent = db.Column(db.String(50))
    status = db.Column(db.String(20))
    desc = db.Column(db.String())

    def __repr__(self):
        return f'<Report {self.agent} {self.status} {self.tms} >'


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tms = db.Column(db.DateTime, index=True, default=datetime.now)
    # tms_upd = db.Column(db.DateTime, index=True)
    id_server = db.Column(db.Integer, db.ForeignKey('server.id'))
    agent = db.Column(db.String(50))
    status = db.Column(db.String(20))

    def __repr__(self):
        return f'<Status {self.agent} {self.status}>'