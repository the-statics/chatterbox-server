from Global import API, app
import views.session

if __name__ == '__main__':
    API.run(app, port=5051, host='0.0.0.0')