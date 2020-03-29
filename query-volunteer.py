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
