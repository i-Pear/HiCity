from weather import db

db.drop_all()
db.create_all()
print("Database initialized.")
