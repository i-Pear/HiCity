from weather import db
from weather.model import WeatherRecord

db.drop_all()
db.create_all()
print("Database initialized.")
