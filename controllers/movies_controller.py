from flask import Blueprint, jsonify, request
from main import db
from models.movies import Movie

movies = Blueprint('movies', __name__, url_prefix="/movies")


@movies.route("/", methods=["GET"])
def get_movies():
    #stmt = db.select(Movie)
    #movies = db.session.scalars(stmt)
    #return movies_schema.dump(movies)
    return "List of movies"


@movies.route("/add", methods=["POST"])
#Decorator to make sure the jwt is included in the request
#@jwt_required()
def movie_create():
    #get the user id invoking get_jwt_identity
    #user_id = get_jwt_identity()
    #Find it in the db
    #stmt = db.select(User).filter_by(id=user_id)
    #user = db.session.scalar(stmt)
    #Make sure it is in the database
    # Stop the request if the user is not an admin
    #if not user.admin:
        #return abort(401, description="Unauthorised user")
    #Create a new card
    #movie_fields = movie_schema.load(request.json)

    #new_movie = Movie()
    #new_movie.title = movie_fields["title"]
    #new_movie.genre = movie_fields["genre"]
    #new_movie.length = movie_fields["length"]
    #new_movie.year = movie_fields["year"]
    # add to the database and commit
    #db.session.add(new_movie)
    #db.session.commit()
    #return the card in the response
    #return jsonify(movie_schema.dump(new_movie))
    return "Movie added"


#add the id to let the server know the card we want to delete
@movies.route("/<int:id>", methods=["DELETE"])
#@jwt_required()
#Includes the id parameter
def movie_delete(id):
    #get the user id invoking get_jwt_identity
    #user_id = get_jwt_identity()
    #Find it in the db
    #stmt = db.select(User).filter_by(id=user_id)
    #user = db.session.scalar(stmt)
    #Make sure it is in the database
    #if not user:
        #return abort(401, description="Invalid user")
    # Stop the request if the user is not an admin
    #if not user.admin:
        #return abort(401, description="Unauthorised user")
    # find the card
    #stmt = db.select(Movie).filter_by(id=id)
    #movie = db.session.scalar(stmt)
    #return an error if the card doesn't exist
    #if not Movie:
        #return abort(400, description= "Movie doesn't exist")
    #Delete the card from the database and commit
    #db.session.delete(movie)
    #db.session.commit()
    #return the card in the response
    #return jsonify(movie_schema.dump(movie))
    return "Movie deleted"