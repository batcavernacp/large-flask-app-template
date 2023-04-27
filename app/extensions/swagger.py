from flask import Flask
from flask_apispec.extension import FlaskApiSpec
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from app.routes.posts import Posts

def setup_swagger(app: Flask):
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='My API1',
            version='1.0.0',
            openapi_version='3.0.2',
            plugins=[MarshmallowPlugin()],
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
    })

    docs = FlaskApiSpec(app)
    docs.register_existing_resources()
