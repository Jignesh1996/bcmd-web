import os, sys
from flask import Flask, render_template
import flask
import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
import flask_restful
from flask_pymongo import PyMongo
from flask_restful import Api
from flask_basicauth import BasicAuth
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# print("Environment is {}".format(os.environ['APP_SETTINGS']))
mongo = PyMongo(app)

# Local module import
from app.gui.api import ModelInfo, DemandCreator, RunModel, RunDefault, api, CompileModel, AvailableModels, AvailableModelDefs, RunSteadyState


# Add API route for getting models.
api.add_resource(AvailableModels, '/api/getmodels')
api.add_resource(AvailableModelDefs, '/api/getmodeldefs')
api.add_resource(ModelInfo, '/api/modelinfo')
api.add_resource(DemandCreator, '/api/demandcreation')
api.add_resource(RunModel, '/api/runmodel')
api.add_resource(RunDefault, '/api/rundefault')
api.add_resource(CompileModel, '/api/compilemodel')
api.add_resource(RunSteadyState, '/api/steadystate')
# Sample HTTP error handling


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Admin Section
basic_auth = BasicAuth(app)


@app.route('/admin')
@basic_auth.required
def admin():
    return render_template('admin.html')


@app.route('/')
def index():
    return render_template("index.html")
