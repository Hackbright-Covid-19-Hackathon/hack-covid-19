"""Models and database functions for covid19 hackathon project."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
    """User of volunteer website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_full_name= db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    uzipcode = db.Column(db.String(15), nullable=True)
    is_asker= db.Column(db.Boolean(), nullable= True)
    is_vol= db.Column(db.Boolean(), nullable= True)
    trust_score= db.Column(db.String(15), nullable=True)
    trip = db.relationship("Trip",
                           backref=db.backref("relations", 
                           order_by=user_id))


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} zipcode={self.zipcode}>"

class Relational(db.Model):

    __tablename__= "relations"

    relation_id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    r_asker_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    r_vol_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    r_trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), index=True)

    #relationships with the user table
    r_asker_id_rel = db.relationship('User', 
                                    foreign_keys="[User.user_id]", 
                                    backref='relational_asker')

    r_vol_id_rel = db.relationship('User', 
                                    foreign_keys="[User.user_id]", 
                                    backref='relational_volunteer')

class Trip(db.Model):
    """Items that a user requests"""

    __tablename__ = "trips"

    trip_id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_zipcode= db.Column(db.String(15))
    user_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    wishlist = db.Column(db.Text(), nullable=True)
    item_progress= db.Column(db.String(15))

    # Define relationship to user
    user = db.relationship("Relational",
                           backref=db.backref("relations", 
                            order_by=user_id))


class Wishlist(db.Model):
    """Items that a user requests"""

    __tablename__ = "wishlist"

    wish_item_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # wish_item_desc= db.Column(db.)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<Item ={self.item_description}>"""

##############################################################################
# Helper functions

def connect_to_db(app, db_uri='postgresql:///volunteerdb'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


# db.create_all()

if __name__ == "__main__":
    from server import app
    connect_to_db(app)