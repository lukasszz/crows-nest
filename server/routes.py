
import flask
from flask import request
from werkzeug.exceptions import abort

from server.models import Server, Report
from server import app, db


@app.route('/')
@app.route('/index')
def index():
    # s = Server(name='localhost', ip='127.0.0.1')
    # db.session.add(s)
    # db.session.commit()
    return "Hello, World!"


@app.route('/report', methods=['POST'])
def report():
    if not request.json:
        abort(400)

    body = request.json

    # ip = request.remote_addr
    # print(ip)
    # s = Server.query.filter(Server.ip == ip).first()
    # a = Agent.query.get(1)
    # id_server = s.id
    r = Report(agent=body.get('agent',''), status=body.get('status',''), desc=body.get('desc',''))
    db.session.add(r)
    db.session.commit()

    return "Report saved"
