from hicityserver.weather import app, db


def run_production():
    # init database
    db.create_all()
    # start hicity server
    from gevent import monkey
    monkey.patch_all()

    from gevent.pywsgi import WSGIServer
    WSGIServer(('127.0.0.1', 8080), app).serve_forever()


if __name__ == '__main__':
    run_production()
