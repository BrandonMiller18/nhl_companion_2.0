# SQLAlchemy config
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/nhlcompanion'

# app config
SECRET_KEY = 'dev'

# cron config
SCHEDULER_API_ENABLED = True