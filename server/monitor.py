import datetime

from server.models import Report, Status, Server
from server import app, db


def monitor():
    check_expected_reports()
    db.session.commit()


def update_agent_status(server: Server, agent, new_status):
    s = Status.query.filter(Status.agent == agent, Status.id_server == server.id).first()

    if s is None:
        s = Status(agent=agent, status=new_status, id_server=server.id)
    elif s.status != new_status:
        if new_status == 'Error' or new_status == 'None' or s.status == 'Error' or s.status == 'None':
            print(f'{new_status}: {server.name}.{agent} ')
        s.status = new_status
    db.session.add(s)


def check_expected_reports():
    expected_report_interval = 1
    servers = Server.query.all()
    for s in servers:
        minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=expected_report_interval)
        reports = Report.query.filter(Report.tms > minutes_ago, Report.id_server == s.id).order_by(Report.tms).all()

        agents_expected = ['df', 'psql']
        for r in reports:
            try:
                agents_expected.remove(r.agent)
            except ValueError:
                pass

        for e in agents_expected:
            update_agent_status(s, e, 'None')


if '__main__' == __name__:
    monitor()
