from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Route(db.Model):
    __tablename__ = 'ROUTES'

    ORIGIN = db.Column(db.Text)
    DESTINATION = db.Column(db.Text)
    TRAVEL_TIME = db.Column(db.Integer)

    def to_dict(self):
        return dict(origin=self.origin,
                    destination=self.destination,
                    travel_time=self.travel_time,
                    link=[self.origin, self.destination])
