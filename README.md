# iot-app

* [APP LINK](https://iot-app-course.herokuapp.com/)
* https://iot-app-course.herokuapp.com/

## Setup Heroku

```
Procfile: web: gunicorn app:app --log-file=-
Procfile: web: web: gunicorn -k eventlet  -w 1 --log-file=- websocketApp:app
```

* [Flas-SocketIO ](https://flask-socketio.readthedocs.io/en/latest/)
* [Flask Quick Start](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Plotly figure reference](https://plotly.com/python/reference/)
