from weather import app, db

if __name__ == '__main__':
    # init database
    db.create_all()
    # start server
    from gevent.pywsgi import WSGIServer

    WSGIServer(('127.0.0.1', 8080), app).serve_forever()
