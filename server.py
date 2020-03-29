"""Covid19 Hackathon"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User



app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.secret_key= "ABC"


def check_logged_in():
    if session.get("user_id") == None:
        flash("You're not currently logged in!")
        return redirect("/login")


@app.route("/")
def homepage():
    """Show the homepage."""

    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login_page():
    """Log in user and return to homepage."""

    username = request.form.get("username")
    password = request.form.get("password")

    user_type = session["user_type"]

    user = User.query.filter_by(username=username).first()
    if user:
        if user.check_password(password):
            session["user_id"] = user.user_id
            flash("Successfully logged in!")
            return redirect(f"/user-homepage/{user_id}")

        else:
            flash("Incorrect password, please try again.")
            return redirect("/login")
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

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    form_phone = request.form.get("phone")
    if form_phone:
        phone_parts = form_phone.split("-")
        phone = "+1" + phone_parts[0] + phone_parts[1] + phone_parts[2]
    else:
        phone = None
    username = request.form.get("username")
    password = request.form.get("password")
    if not User.query.filter_by(username=username).all():
        new_user = User(fname=fname, lname=lname, phone=phone, username=username)
        # This is a method Amber set in her model.py to hash passwords
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.user_id
        flash("Successfully created an account!")

        return redirect(f"/user/{user_id}")


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


@app.route("/user-homepage")
def show_user_homepage():
    """ Show user homepage."""

    return render_template("user.html")

@app.route("/asker-homepage")
def show_asker_homepage():
    """Show homepage for asker."""
    
    return render_template("asker.html")


@app.route("/create")
def show_order_form():
    """Show order form."""

    return redirect("/asker-homepage")


@app.route("/create", methods=["POST"])
def save_order():
    """Save order from form inputs."""

    return redirect("/asker-homepage")


@app.route("/volunteer-homepage")
def show_volunteer_homepage():
    """Show homepage for volunteer."""
    
    return render_template("volunteer.html")



if __name__ == "__main__": 

    app.debug = True #pragma: no cover
    connect_to_db(app) #pragma: no cover
    DebugToolbarExtension(app) #pragma: no cover
    app.run(host="0.0.0.0") #pragma: no cover

