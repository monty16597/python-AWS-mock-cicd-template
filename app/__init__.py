from flask import Flask
from app.config import AppConfig


def create_app(config=AppConfig):
    app = Flask(__name__)

    # Configuration setup
    app.config.from_object(config)
    app.app_context().push()

    # Blueprint registration
    from .blueprints.pdf import main_bp
    from .blueprints.system import system_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(system_bp)

    # Other setup (extensions, middleware, etc.) can go here

    return app
