from flask_cors import CORS
from flask import Flask, g

# Using a factory and making the app modular
def create_app(app_name='ONBOARD_COMPUTER_API'):
    app = Flask(app_name)
    app.config.from_object('onboard_computer_api.config.BaseConfig')

    with app.app_context():
        from onboard_computer_api.routes import api
        app.register_blueprint(api, url_prefix="/api")

    cors = CORS(app, resources={r"/api/*": {"origins": app.config['CORS_ORIGINS']}})

    from . import controller
    controller.init_app(app)

    return app