from model import connect_to_db, db, User, Wishlist, Trip, Relational

"""
Volunteer Page Route Plan
    -enter zipcode (GET, POST)
        - list of users i.e. user_1, user_2, user_3 (GET, POST)
            -volunteer confirmed items (POST) 
                -reveals asker's phone/email
                    - <contact each other>
                      -mark order completed
"""      


# @app.route("/volunteer-homepage")
def get_zipcode:

    same_zip = Relational.query.filter_by(zipcode=r_asker_id.uzipcode).all()

    return same_zip


# def get_asker_wishlist:

#     user_wish = Trip.query.filter_by(user_id=wishlist).first()

#     return user_wish


def get_asker_contact:

    asker_email = User.query.get(email)

    return asker_contact


# #Yichen's template

# @app.route("/inprogress", methods=["POST"]) ## Make AJAX Request?

# def volunteer_confirm_task():
#     """Sends in progress status to database"""
#     # includes a button to change status to "in progress"



# @app.route("/inprogress")

# def status_in_progress():
#     """Routes to in progress page"""

#     # displays a page that shows in progress?
#     return render_template("asker-wishlist-inprogress.html")


# @app.route("/completed", methods=["POST"]) ## Make AJAX Request?
# def grocery_delivered():
#     """Sends completed wishlist status to database"""

#     return redirect("/")


# @app.route("/completed") ## Make AJAX Request?
# def status_complete():
#     """routes to completed page"""
#     # volunteer confirms items -- another button

#     return render_template("asker-wishlist-completed.html")




if __name__ == "__main__":

  from server import app
  
  connect_to_db(app)
  
  print("Connected to DB.")










