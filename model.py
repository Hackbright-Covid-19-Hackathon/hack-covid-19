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


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} zipcode={self.zipcode}>"

class Volunteer(db.Model):
    """Volunteers"""

    __tablename__ = "volunteers"

    volunteer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    volunteer_full_name= db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    vzipcode = db.Column(db.String(15))
    trip_id = db.Column(db.Integer)
    trust_score= db.Column(db.String(15), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<Volunteer Name={self.volunteer_full_name} zipcode={self.vzipcode}>"


class Item(db.Model):
    """Items that a user requests"""

    __tablename__ = "items"


    trip_id= db.Column(db.Integer, autoincrement=True, nullable=True, primary_key=True)
    item_id = db.Column(db.Integer)
    trip_zipcode= db.Column(db.String(15))
    user_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    volunteer_id= db.Column(db.Integer, db.ForeignKey('volunteers.volunteer_id'), nullable=True)
    item_description = db.Column(db.String(200))
    item_progress= db.Column(db.String(15))

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("users", order_by=user_id))

    # Define relationship to volunteer
    volunteer = db.relationship("Volunteer",
                            backref=db.backref("volunteers", order_by=volunteer_id))





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