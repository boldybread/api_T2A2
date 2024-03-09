from init import db, ma
from marshmallow import fields

# model needs to be class, extends from the model class in SQLAlchemy
class Movies(db.Model):
    __tablename__ = "movies"

    # structure of table, each column
    movie_id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    genre = db.Column(db.String, nullable=False)
    view_platform = db.Column(db.String)
    avg_rating = db.Column(db.Integer)

    rating = db.relationship('Rating', back_populates='movies', cascade='all, delete')
    watchlist = db.relationship('Watchlist', back_populates='movies', cascade='all, delete')

    # movie schema, also class, using schema class provided by marshmallow
class MovieSchema(ma.Schema):
    rating = fields.List(fields.Nested('RatingSchema', exclude=['movies']))
    watchlist = fields.List(fields.Nested('WatchlistSchema', exclude=['movies']))
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'watchlist', 'rating')

    # create schema for handling one user, and schema for handling many users
movie_schema = MovieSchema(exclude=['password'])  # {} this will serialise one dictionary of all fields
movies_schema = MoviesSchema(many=True, exclude=['password']) # [{}, {}, {}] # This will serialise a list of dictionaries each with all fields