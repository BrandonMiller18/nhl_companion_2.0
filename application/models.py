from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# create model
class teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(45), nullable=False, unique=True)
    team_abbreviation = db.Column(db.String(4))

    #create a string
    def __repr__(self):
        return '<Name %r>' % self.name