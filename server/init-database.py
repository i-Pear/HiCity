from weather import db


def init_db():
    db.drop_all()
    db.create_all()
    print("Database initialized.")


if __name__ == '__main__':
    init_db()
