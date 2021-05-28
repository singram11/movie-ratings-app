"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key ="dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def render_index():
    """Opens the homepage"""

    return render_template('homepage.html')

@app.route('/users', methods = ['POST'])
def create_login():

    user_email = request.form['user_email']
    user_password = request.form['password']

    user = crud.get_user_by_email(user_email)

    if user != None:
        flash('This user already exists')   
    else:
        flash('Account created!')

    # WE LEFT OFF HERE: num3 in part 4 of the lab - haven't made a way for this thing
    # to create a user in the else part of the above thing. 
    return redirect('/')

@app.route("/movies")
def show_movies():

    all_movies = crud.show_all_movies()

    return render_template('all_movies.html', movies=all_movies)

@app.route("/user/<user_id>")
def show_user_profile(user_id):

    user = crud.show_user_by_id(user_id)

    return render_template ('user_details.html', user=user) 

@app.route("/movie/<int:movie_id>")
def show_movies_by_id(movie_id):
    """Show movie details by ID"""

    movie = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html', movie=movie)

@app.route("/users")
def show_all_users():
    """Show a list of all users emails and link to their profiles"""

    users = crud.show_all_users()

    return render_template('all_users.html', users=users)




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
