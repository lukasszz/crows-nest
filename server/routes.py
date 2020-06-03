import flask
from flask import request, render_template
from werkzeug.exceptions import abort

from server.monitor import update_agent_status
from server.models import Server, Report
from server import app, db


@app.route('/')
@app.route('/index')
def index():
    # s = Server(name='localhost', ip='127.0.0.1')
    # db.session.add(s)
    # db.session.commit()
    servers = Server.query.all()

    return render_template('index.html', servers=servers)


@app.route('/report', methods=['POST'])
def report():
    if not request.json:
        abort(400)

    body = request.json

    ip = request.remote_addr
    s = Server.query.filter(Server.ip == ip, Server.name == body.get('server_name', '')).first()
    if s is None:
        return
    r = Report(agent=body.get('agent', ''), status=body.get('status', ''), desc=body.get('desc', ''), id_server=s.id)
    db.session.add(r)
    update_agent_status(s, r.agent, r.status)
    db.session.commit()

    return "Report saved"
