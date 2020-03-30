"""Covid19 Hackathon"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Relational, Trip, Wishlist
from queryuser import add_wishlist, get_wishlist, update_status, get_wishlists
from query_volunteer import vol_update_status


app = Flask(__name__)

app.jinja_env.undefined = StrictUndefined
app.secret_key= "ABC"


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

    user = User.query.filter_by(email=email).first()

    if user:
        if user.check_password(password): 
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


@app.route("/asker-homepage")
def show_asker_homepage():
    """Show homepage for asker."""
    
    return render_template("asker.html")


@app.route("/create", methods=["POST"])
def create_wishlist():
    """Get asker's wishlist and zipcode to save in database."""
    print('000')
    new_wishlist = request.form.get('wishlist')
    print(new_wishlist)
    zipcode = request.form.get('zipcode')
    asker = session.get("user_id")
    status = "incomplete"

    new_trip = Trip(user_id=asker, 
                    wishlist=new_wishlist, 
                    trip_zipcode=zipcode,
                    item_progress=status)
    print(new_trip)
    db.session.add(new_trip)
    db.session.commit()
    session["trip_id"] = new_trip.trip_id
    flash("Successfully created a wishlist!")

    print("200")

    return redirect("/asker-homepage")
    

@app.route("/incomplete")
def asker_view_wishlist():
    """Display wishlist."""
    
    asker = session.get("user_id")
    print(asker)
    incomplete_order = get_wishlists(asker)
    print(incomplete_order)
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


@app.route("/volunteer-homepage")
def show_volunteer_homepage():
    """Show homepage for volunteer and displays active orders."""

    return render_template("volunteer.html")


@app.route('/trips.json')
def trip_info():
    """Retrieving status of asker's wishlist"""

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


@app.route('/volunteer-all-wishlist')
def display_asker_wishlists():
    """Displays all avaliable wishlists"""

    return render_template("wishlists.html")


@app.route('/wishlistInfo.json')
def viewwishlists():
    """ """
    trip = Trip.query.filter_by(session.uzipcode, item_progress='incomplete').all()

    wishlistList = []
    if trip:
        wishlistList.append({
            'wishlist_id': trip.trip_id,
            'wishlist_progress': trip.item_progress,
            'wishlist': trip.wishlist
        })

        return jsonify(wishlistList)

    else:
        wishlistList.append({
            'wishlist_id': None,
            'Wishlist_progress': None,
            'wishlist': None
        })

    return jsonify(wishlistList)


@app.route('/volunteer-wishlist/<int:trip_id>')
def display_asker_single_wishlist():
    """Displays selected wishlist (single)"""

    return render_template("single_wishlist.html")


@app.route("/single_wishlist.json")
def vol_view_wishlist():
    """Display a single selected wishlist"""

    trip = Trip.query.filter_by(trip_id).first()

    session['wishlist_id'] = trip.trip_id

    trip_info = {
        'wishlist_id': trip.trip_id,
        'wishlist_progress': trip.item_progress,
        'wishlist': trip.wishlist
        }

    return jsonify(trip_info)


@app.route("/inprogress", methods=["POST"])
def vol_status_in_progress():
    """Update wishlist status to in progress."""
    
    volunteer = session.get("wishlist_id")
    
    current_status = 'In Progress'
    
    trip = Trip.query.filter_by(trip_id).first()
    
    trip.item_progress = current_status
    
    new_status = vol_update_status(volunteer)

    db.session.commit()
    
    return new_status


@app.route("/completed", methods=["POST"])
def vol_status_completed():
    """Update wishlist status to completed."""
    
    volunteer = session.get("wishlist_id")
    
    current_status = 'Completed!'
    
    trip = Trip.query.filter_by(trip_id).first()
    
    trip.item_progress = current_status
    
    new_status = vol_update_status(volunteer)
    
    db.session.commit()
    
    return new_status


@app.route("/about")
def about():
    """about page"""

    return render_template("about.html")


if __name__ == "__main__": 

    app.debug = False #pragma: no cover
    connect_to_db(app) #pragma: no cover
    DebugToolbarExtension(app) #pragma: no cover
    app.run(host="0.0.0.0") #pragma: no cover

