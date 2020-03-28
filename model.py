"""Models and database functions for covid19 hackathon project."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#db createdb volunteerdb
# python3 -i model.py
 ## in python3 interactive db.createall()


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
    # trip = db.relationship("Trip",
    #                        backref=db.backref("relations", 
    #                        order_by=user_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"<User user_id={self.user_id} zipcode={self.uzipcode}>"

class Relational(db.Model):

    __tablename__= "relations"

    relation_id= db.Column(db.Integer, autoincrement=True, primary_key=True)
    r_asker_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), index=True)
    r_vol_id= db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable= True)
    r_trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), nullable= True)

#     # #relationships with the user table
#     # r_asker_id_rel = db.relationship('User', 
#     #                                 foreign_keys="[User.user_id]", 
#     #                                 backref='relational_asker')

#     # r_vol_id_rel = db.relationship('User', 
#     #                                 foreign_keys="[User.user_id]", 
#     #                                 backref='relational_volunteer')

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

# # db.create_all()


# c1 = User(
# user_full_name= "Faker Fakey",
# email = "fake@gmail.com",
# password = "123",
# uzipcode = "94805",
# is_asker= True,
# is_vol= False
# )

    # c2 = User(
    # user_full_name= "Faker RE Fakey",
    # email = "@gmail.com",
    # password = "1235",
    # uzipcode = "94121",
    # is_asker= False,
    # is_vol= True
    # )

    # r1 = Relational(
    # r_asker_id= 1,
    # r_vol_id_rel= 1,
    # r_asker_id_rel= 1
    # # r_vol_id= 2, 
    # # r_trip_id = 1
    # )

    # t1 = Trip(
    # trip_zipcode= "94805",
    # user_id= 1,
    # wishlist = "I want a kitten",
    # item_progress= "En Route"
    # ) 

    # w1= Wishlist(
    #     )


## To add data to the db:

# example_data()
# db.session.add_all([c1, c2, r1, t1, w1])
# db.session.commit()

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