from flask import Flask
from .routes.auth import auth_bp
from .routes.customer import customer_bp
from .routes.vendor import vendor_bp

def create_app():
    app = Flask(__name__)

    app.register_blueprint(auth_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(vendor_bp)

    return app
