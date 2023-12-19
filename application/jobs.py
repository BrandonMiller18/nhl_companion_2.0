from flask_apscheduler import APScheduler
from application.models import *
import requests

scheduler = APScheduler()

BASE_URL = 'https://api.nhle.com/'

@scheduler.task('interval', id='job1', seconds=86400)
def update_teams():
    """scheduled job to update teams in the DB"""

    # get data from API
    r = requests.get(BASE_URL + 'stats/rest/en/team')
    data = r.json()
    
    from wsgi import app
    with app.app_context():
        for team in data['data']:
            # check if team already exists, only add new teams
            if not bool(teams.query.filter_by(team_name=team['fullName']).first()):
                row = teams(team_name=team['fullName'], team_abbreviation=team['triCode'])
                db.session.add(row)
                db.session.commit()
    
print('Teams table updated.', flush=True)