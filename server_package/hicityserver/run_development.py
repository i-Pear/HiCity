from hicityserver.weather import app


def run_development():
    app.static_folder = 'static'
    app.run(port=8080, debug=True, processes=True)


if __name__ == '__main__':
    run_development()
