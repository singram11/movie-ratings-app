""" CRUD operations """

from model import db, User, Movie, Rating, connect_to_db

from datetime import datetime


def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def show_all_movies():
    """returns a list of ALL the movies. ever. (in your db)"""

    Movie.query.finish_this_stuff_cool

    #WE LEFT OFF: Your Task (task 1 ): ) in part 3. 
    # is this whole thing even completeable in 4 sessions?


def create_rating(score, user, movie):
    """Create and return a new rating.
    user and movie should be objects."""

    rating = Rating(score=score, user=user, movie=movie)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
