from flask import Flask, jsonify, render_template
from model import connect_to_db, # OTHER ROUTE NAMES


app = Flask(__name__)


def check_logged_in():
    if session.get("user_id") == None:
        flash("You're not currently logged in!")
        return redirect("/login")


@app.route("/")
def homepage():
    """Show the homepage."""

    return render_template("index.html")


@app.route("/login")
def show_login_page():
    """Show page for user to log in."""

    if session.get("user_id") != None:
        user_id = session["user_id"]
        return redirect(f"/my-homepage/{user_id}")
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_page():
    """Log in user and return to homepage."""
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username).first()
    if user:
        if user.check_password(password):
            session["user_id"] = user.user_id
            flash("Successfully logged in!")
            return redirect(f"/my-homepage/{user_id}")
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
        return redirect(f"/my-homepage/{user_id}")

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





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)