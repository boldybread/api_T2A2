import os
from flask import Flask
from init import db, ma, bcrypt, jwt

# Create instance of Flask app
def create_app():
    app = Flask(__name__)

    # Define configurations
    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URI")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    # connect this instance of flask app with our different libraries
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import blueprint from commands
    from controllers.cli_controller import db_commands
    # register blueprint in flask instance
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    return app