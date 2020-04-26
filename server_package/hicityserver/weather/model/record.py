from hicityserver.weather import db


class WeatherRecord(db.Model):
    __tablename__ = 'weather'
    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id = db.Column(db.Integer, nullable=False, index=True)
    time = db.Column(db.String(100), nullable=False, index=True)
    data = db.Column(db.String(5000), nullable=False)
