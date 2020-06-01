import datetime

from server.models import Report, Status
from server import app, db


def monitor():
    reports = get_last_reports()


    check_expected_agents(reports)

    update_last_agent_status(reports)
    db.session.commit()


def update_last_agent_status(reports):
    # Agent last status
    agent_last_status = {}
    for r in reports:
        try:
            agent_last_status[r.agent] = r.status
        except KeyError:
            agent_last_status.update({r.agent: r.status})

    for a, ls in agent_last_status.items():
        update_agent_status(a, ls)
    # errors = [a for a, s in agent_last_status.items() if s == 'Error']
    # print(f'Last status: {agent_last_status}')
    # print(f'[ALERT]: Error status for agents: {errors}')


def update_agent_status(agent, new_status):

    s = Status.query.filter(Status.agent == agent).first()

    if s is None:
        s = Status(agent=agent, status=new_status)
    elif s.status != new_status:
        if new_status == 'Error' or new_status == 'None':
            print(f'[ALERT] Error form agent {agent} ')
        if s.status == 'Error' or s.status == 'None':
            print(f'[INFO] New status for {agent}: {new_status} ')
        s.status = new_status
    db.session.add(s)


def check_expected_agents(reports):
    agents_expected = ['df', 'psql']
    for r in reports:
        try:
            agents_expected.remove(r.agent)
        except ValueError:
            pass

    for e in agents_expected:
        update_agent_status(e, 'None')
        # s = Status.query.filter(Status.agent==e).first()
        # if s is None:
        #     s = Status(agent=e, status='None')
        # elif s.status != 'None':
        #     s.status = 'None'
        #     print(f'[ALERT] No reports form agent {e} ')
        # db.session.add(s)

# def empty_reports(reports):
#     s = Status.query.filter(Status.agent == e).first()
#
#     if 0 == len(reports):
#         print('[ALERT] No reports form the server. Is it alive?')


def get_last_reports():
    minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=5)
    reports = Report.query.filter(Report.tms > minutes_ago).order_by(Report.tms).all()
    # for r in reports:
    #     print(r)
    return reports


if '__main__' == __name__:
    monitor()



