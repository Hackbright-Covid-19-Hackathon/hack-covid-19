"""Models and database functions for covid19 hackathon project."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
#db createdb volunteerdb
# python3 -i model.py
 ## in python3 interactive db.createall()


##############################################################################
# Model definitions

class User(db.Model):
    """User of volunteer website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, 
                        nullable=False)
    user_full_name = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True)
    password_hash = db.Column(db.String(100), nullable=False)
    uzipcode = db.Column(db.String(15), nullable=True)
    is_asker = db.Column(db.Boolean(), nullable=True)
    is_vol = db.Column(db.Boolean(), nullable=True)
    trust_score = db.Column(db.String(15), nullable=True)
    
    # relationships
    # relationship in 'Trip' class
    # relationship in 'Relational' class


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} zipcode={self.uzipcode}>"

    def set_password(self, password):
        """Use werkzeug.security's password_hash to securely save password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if password given matches hashed password."""
        return check_password_hash(self.password_hash, password)


class Relational(db.Model):

    __tablename__ = "relations"

    relation_id = db.Column(db.Integer, autoincrement=True, primary_key=True, 
                        nullable = False)
    r_asker_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    r_vol_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable= True)
    r_trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), nullable= True)

    #relationships with the user table
    r_asker_id_rel = db.relationship('User', 
                                    foreign_keys="[Relational.r_asker_id]", 
                                    backref='relational_asker')

    r_vol_id_rel = db.relationship('User',
                                    foreign_keys="[Relational.r_vol_id]",
                                    backref='relational_volunteer')

class Trip(db.Model):
    """Items that a user requests"""

    __tablename__ = "trips"

    trip_id= db.Column(db.Integer, autoincrement=True, primary_key=True, 
                        nullable = False)
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

    wish_item_id = db.Column(db.Integer, autoincrement=True, primary_key=True, 
                                nullable = False)
    # wish_item_desc= db.Column(db.)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<Item ={self.wish_item_id}>"""


# Helper functions

def connect_to_db(app, db_uri='postgresql:///volunteerdb'):
    """Connect the database to Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    from server import app
    connect_to_db(app)