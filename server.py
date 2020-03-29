"""Covid19 Hackathon"""

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User
# , Relational, Trip, Wishlist


app = Flask(__name__)


if __name__ == "__main__": 

    app.debug = True #pragma: no cover
    connect_to_db(app) #pragma: no cover
    DebugToolbarExtension(app) #pragma: no cover
    app.run(host="0.0.0.0") #pragma: no cover

