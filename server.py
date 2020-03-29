"""Covid19 Hackathon"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Relational, Trip, Wishlist
from queryuser import add_wishlist, get_wishlist, update_status

app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.secret_key= "ABC"


# def check_logged_in():
#     if session.get("user_id") == None:
#         flash("You're not currently logged in!")
#         return redirect("/login")



@app.route("/")
def homepage():
    """Show the homepage."""

    return render_template("index.html")


@app.route("/user")
def display_user_type():
    """Show a transit page for user to choose to be volunteer or create wishlist."""

    return render_template("user.html")


@app.route("/login", methods=["POST"])
def login_page():
    """Log in user and return to homepage."""

    email = request.form.get("email")
    print(f'\n\nemail: {email}')
    password = request.form.get("password")
    print(f'\n\npassword: {password}')
    
    # import ipdb; ipdb.set_trace()

    user = User.query.filter_by(email=email).first()
    # db.session.query((User.user_full_name),\ 
    #                         .filter(User.email == email)).first
    #                          #
    if user:
        if user.check_password(password): #updated variable name from password to password_hash
            session["user_id"] = user.user_id
            flash("Successfully logged in!")
            return redirect("/user")

        else:
            flash("Incorrect password, please try again.")
            return redirect("/")
    else:
        flash("No user found with that username. Please register for an account.")
        return redirect("/register")


@app.route("/register")
def show_registration_page():
    """Show page for use to register for an account."""

    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_user():
    """Create account for user by adding them to database."""

    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    zipcode = request.form.get("zipcode")
    
    if not User.query.filter_by(user_full_name=username).all():
        new_user = User(email=email, 
                        user_full_name=username, 
                        uzipcode=zipcode)

        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.user_id
        flash("Successfully created an account!")

        return redirect("/user")

    else:
        flash("User already exists! Try logging in instead.")
        return redirect("/login")


@app.route("/logout")
def logout_user():
    """Log user out of current session."""

    if session.get("user_id") != None:
        del session["user_id"]
        flash("Successfully logged out!")
        return redirect("/")
    else:
        flash("You're not currently logged in!")
        return redirect("/")


# @app.route("/user-homepage")
# def show_user_homepage():
#     """ Show user homepage."""

#     return render_template("volunteer.html")

@app.route("/asker-homepage")
def show_asker_homepage():
    """Show homepage for asker."""
    
    return render_template("asker.html")


# @app.route("/volunteer-homepage")
# def show_volunteer_homepage():
#     """Show homepage for volunteer."""
# <<<<<<< HEAD
#     # Page should show active orders they signed up for
#     # Page should link to form for volunteer to enter their zipcode
#     return render_template("volunteer-homepage.html")


# @app.route("/volunteer-signup")
# def show_volunteer_signup():
#     """Show form for volunteer to enter zipcode"""
#     # Page should have volunteer enter their zipcode
#     return render_template("volunteer-signup.html")


# # For these routes, not sure how to write since I don't know how
# # Backend team plans to implement these?
# @app.route("/volunteer-signup", methods=["POST"])
# def show_volunteer_options():
#     """Show order options for volunteer to sign up for."""
#     # Page should have a checkbox list of orders volunteers can sign up for
#     return render_template("")


@app.route("/create", methods=["POST"])
def create_wishlist():
    """Get asker's wishlist and zipcode to save in database."""

    new_wishlist = request.args.get('wishlist')
    zipcode = request.args.get('zipcode')
    asker = session.get("user_id")
    status = "incomplete"

    # if not Trip.query.filter_by(trip=username).all():
    new_trip = Trip(user_id=asker, 
                    wishlist=new_wishlist, 
                    trip_zipcode=zipcode,
                    item_progress=status)

    db.session.add(new_trip)
    db.session.commit()
    session["trip_id"] = new_trip.trip_id
    flash("Successfully created a wishlist!")

    print("200")

    return redirect("/asker-homepage")
    

@app.route("/incomplete")
def view_wishlist():
    """Display wishlist."""

    asker = session.get("user_id")

    incomplete_order = get_wishlist(asker)

    return jsonify(incomplete_order)


@app.route("/inprogress")
def status_in_progress():
    """Update wishlist status to in progress."""
    
    asker = session.get("user_id")

    new_status = update_status(asker)

    return new_status


@app.route("/completed")
def status_completed():
    """Update wishlist status to completed."""

    asker = session.get("user_id")

    new_status = update_status(asker)

    return new_status


@app.route('/trips.json')
def trip_info():

    trip = Trip.query.filter_by(session.user_id).first()

    tripList = []

    if trip:

        tripList.append({
            'trip_id': trip.trip_id,
            'trip_progress': trip.item_progress
        })

        return jsonify(tripList)

    else:
        tripList.append({
            'trip_id': None,
            'trip_progress': None
        })

    return jsonify(tripList)


@app.route("/about")
def about():
    """about page"""

    return render_template("about.html")


if __name__ == "__main__": 

    app.debug = True #pragma: no cover
    connect_to_db(app) #pragma: no cover
    DebugToolbarExtension(app) #pragma: no cover
    app.run(host="0.0.0.0") #pragma: no cover

