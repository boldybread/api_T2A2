from flask import Blueprint
# in order to create or seed the db we import it from init where sqlalchemy was initialised. bcrypt to generate hashed passwords
from init import db, bcrypt
# folder name . file name - to import models/tables
from models.user import User

db_commands = Blueprint('db', __name__)


@db_commands.cli.command('create')
# These functions are built into SQLAlchemy
def create_tables():
    db.create_all()
    print("Tables created")

@db_commands.cli.command('drop')
def drop_tables():
    db.drop_all()
    print("Tables dropped")

@db_commands.cli.command('seed')
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8'),
            is_admin=True
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash('123456').decode('utf-8')
        )
    ]

    # A session represents the connection between an application and the relational database that stores its persistent objects
    # we add list of users to the session; add_all for multiple users, add for singular
    db.session.add_all(users)

    db.session.commit()

    print("Tables seeded")