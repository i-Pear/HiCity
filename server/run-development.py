from weather import app


def run_develpoment():
    app.static_folder = 'static'
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    run_develpoment()
