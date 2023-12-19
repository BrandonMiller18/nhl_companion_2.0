from flask import Flask

def init_app():
    """Iniitialize the core application"""
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    with app.app_context():
        # initialize plugins
        from application.models import db
        db.init_app(app)
        from application.jobs import scheduler
        scheduler.init_app(app)
        scheduler.start()

        from . import routes
        from . import models

    return app