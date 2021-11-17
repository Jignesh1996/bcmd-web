from app import app
import pprint
import flask.scaffold
import flask
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful

if __name__ == '__main__':
    try:
        app.run(host=app.config['HOST'])
    except KeyError:
        app.run()
