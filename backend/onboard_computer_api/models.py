# from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()

class Route():
    # __tablename__ = 'ROUTES'
    # ORIGIN = db.Column(db.Text)
    # DESTINATION = db.Column(db.Text)
    # TRAVEL_TIME = db.Column(db.Integer)
    def __init__(self, origin, destination, travel_time):
        self.origin = origin
        self.destination = destination
        self.travel_time = travel_time
        self.link = [origin, destination]

    def to_dict(self):
        return dict(origin=self.origin,
                    destination=self.destination,
                    travel_time=self.travel_time,
                    link=[self.origin, self.destination])
