from hicityserver.weather import db


def init_database():
    db.drop_all()
    db.create_all()
    print("Database initialized.")


if __name__ == '__main__':
    init_database()
