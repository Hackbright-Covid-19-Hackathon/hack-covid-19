from model import connect_to_db, db, User, Wishlist, Trip, Relational

"""
Volunteer Page Route Plan
    -enter zipcode (GET, POST)
        - list of users/orders & checkbox orders (A, B, C) (GET, POST)
            -volunteer confirmed items (POST) 
                -reveals asker's phone/email
                    - <contact each other>
                        -purchased confirm (POST) -status change
                                                                           -asker's address reveals (GET, POST) / <contact each other> REMOVED all communication for 
"""                                                                                   -mark order completed / delete from db
@app.route("/volunteer-signup")
def show_volunteer_signup():
    """Show form for volunteer to enter zipcode"""

    # Page should have volunteer enter their zipcode
    zipcode = request.args("zipcode_input")

    return render_template("volunteer-signup.html", zipcode=zipcode)

@app.route("/volunteer-signup", methods=["GET","POST"])
def show_volunteer_options(zipcode): # value from show_volunteer_signup
     """Show order options for volunteer to sign up for."""

    ## zipcode = request.args("zipcode_input")

    # query into the database for users with the same zipcode
    # going through relational table, then user zipcode
    same_zip = Relational.query.filter_by(zipcode=r_asker_id.uzipcode).all()

    return jsonify(same_zip) # to populate options on the page

@app.route("/volunteer/<int:user_id>")
def display_user_wishlist():
    """Display individual user's wishlist"""

    user_wish = Trip.query.filter_by(user_id=wishlist).first()

    # includes a button to change status to "in progress"
    # volunteer confirms items -- another button
    # reveals asker's phone/email
    asker_phone = User.query.get(email)

    return render_template("asker-wishlist.html")
