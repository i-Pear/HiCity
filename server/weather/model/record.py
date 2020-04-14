from weather import db


class WeatherRecord(db.Model):
    __tablename__ = 'weather'
    time = db.Column(db.String(100), primary_key=True, nullable=False)
    data = db.Column(db.String(5000), nullable=False)
