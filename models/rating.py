from init import db, ma
from marshmallow import fields

# model needs to be class, extends from the model class in SQLAlchemy
class Rating(db.Model):
    __tablename__ = "rating"

    # structure of table, each column
    rating_id = db.Column(db.Integer, primary_key=True)
    rating_date = db.Column(db.Date) # Date the rating was made
    user_rating = db.Column(db.Integer(0, 101), nullable=False)
    
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    user = db.relationship('User', back_populates='rating')
    movie = db.relationship('Movies', back_populates='rating')

    # user schema, also class, using schema class provided by marshmallow
class RatingSchema(ma.Schema):
    # Nested tells marshmallow it is relationship field rather than its own field
    user = fields.Nested('UserSchema', only = ['name', 'email'])
    movie = fields.Nested('MovieSchema', only = ['movie_id', 'avg_rating'])
    class Meta:
        fields = ('rating_id', 'rating_date', 'user_rating', 'user', 'movie')

    # create schema for handling one user, and schema for handling many users
rating_schema = RatingSchema()  # {} this will serialise one dictionary of all fields
ratings_schema = RatingsSchema(many=True) # [{}, {}, {}] # This will serialise a list of dictionaries each with all fields