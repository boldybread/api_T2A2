from init import db, ma
from marshmallow import fields

# model needs to be class, extends from the model class in SQLAlchemy
class Watchlist(db.Model):
    __tablename__ = "watchlist"

    # structure of table, each column
    watchlist_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'), nullable=False) #FK
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) #FK

    user = db.relationship('User', back_populates='watchlist')
    movie = db.relationship('Movies', back_populates='watchlist')

    # user schema, also class, using schema class provided by marshmallow
class WatchlistSchema(ma.Schema):
    # Nested tells marshmallow it is relationship field rather than its own field
    user = fields.Nested('UserSchema', only = ['name', 'email'])
    movie = fields.Nested('UserSchema', only = ['movie_id', 'avg_rating'])
    class Meta:
        fields = ('rating_id', 'rating_date', 'user_rating', 'user', 'movie')

    # create schema for handling one user, and schema for handling many users
watchlist_schema = WatchlistSchema()  # {} this will serialise one dictionary of all fields
watchlists_schema = WatchlistsSchema(many=True) # [{}, {}, {}] # This will serialise a list of dictionaries each with all fields