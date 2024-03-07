from init import db, ma

# model needs to be class, extends from the model class in SQLAlchemy
class User(db.Model):
    __tablename__ = "users"

    # structure of table, each column
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # email needs to be unique and cannot be null
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    # by default users are not an admin user
    is_admin = db.Column(db.Boolean, default=False)


    # user schema, also class, using schema class provided by marshmallow
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

    # create schema for handling one user, and schema for handling many users
user_schema = UserSchema(exclude=['password'])  # {} this will serialise one dictionary of all fields
users_schema = UserSchema(many=True, exclude=['password']) # [{}, {}, {}] # This will serialise a list of dictionaries each with all fields