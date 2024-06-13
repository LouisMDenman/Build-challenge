from flask import Blueprint, jsonify, request, abort
from main import db
from models.actors import Actor
from schemas.actor_schema import actor_schema, actors_schema

actors = Blueprint('actors', __name__, url_prefix="/actors")


@actors.route("/", methods=["GET"])
def get_actors():
    stmt = db.select(Actor)
    actors = db.session.scalars(stmt)
    return actors_schema.dump(actors)


@actors.route("/add", methods=["POST"])
#Decorator to make sure the jwt is included in the request
#@jwt_required()
def actor_create():
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
    actor_fields = actor_schema.load(request.json)

    new_actor = Actor()
    new_actor.first_name = actor_fields["first_name"]
    new_actor.last_name = actor_fields["last_name"]
    new_actor.gender = actor_fields["gender"]
    new_actor.country = actor_fields["country"]
    # add to the database and commit
    db.session.add(new_actor)
    db.session.commit()
    #return the card in the response
    return jsonify(actor_schema.dump(new_actor))


#add the id to let the server know the card we want to delete
@actors.route("/<int:id>", methods=["DELETE"])
#@jwt_required()
#Includes the id parameter
def actor_delete(id):
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
    stmt = db.select(Actor).filter_by(id=id)
    actor = db.session.scalar(stmt)
    #return an error if the card doesn't exist
    if not Actor:
        return abort(400, description= "Actor doesn't exist")
    #Delete the card from the database and commit
    db.session.delete(actor)
    db.session.commit()
    #return the card in the response
    return jsonify(actor_schema.dump(actor))