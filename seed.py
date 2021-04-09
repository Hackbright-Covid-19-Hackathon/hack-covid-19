"""Utility file to seed volunteerdb.

This is 'faker' data for test and demo purposes."""

import csv
from model import User, Relational, Trip, Wishlist
from model import connect_to_db, db
from server import app

################################################################################
# functions

def clear_tables():
    """Delete data from all tables in the database. 
    Delete in dependancy reverse-order to avoid errors related to foreign key relationships."""

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()
    Relational.query.delete()
    Trip.query.delete()
    Wishlist.query.delete()

    print('ALL TABLES HAVE BEEN CLEARED OF THEIR DATA')


def inform_tables_loaded():
    """indicate that all functions ran"""

    print('ALL TABLES HAVE BEEN LOADED WITH DATA')


def add_users():
    """add users to the user table."""

    # c1 = User(
    #         user_full_name = "Ada Lovelace",
    #         email = "Ada@gmail.com",
    #         password = "123",
    #         uzipcode = "94805",
    #         is_asker= True,
    #         is_vol= False
    #         )
    # db.session.add(c1)

    # # print(f'{c1.user_full_name, c1.is_vol}')

    # c2 = User(
    #         user_full_name= "Grace Hopper",
    #         email = "Grace@gmail.com",
    #         password = "1235",
    #         uzipcode = "94121",
    #         is_asker= False,
    #         is_vol= True
    #         )
    
    """Load user information from seed file into the database.
    working code.
    """
    print("users")

    # opening seed file with the csv library and csv reader. 
    with open('seed_files/User_seed_v1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                asker_seed = row[5]
                if asker_seed == "TRUE":
                    asker_seed = True
                elif asker_seed == "":
                    asker_seed = False
                
                vol_seed = row[6]
                if vol_seed == "TRUE":
                        vol_seed = True
                elif vol_seed == "":
                    vol_seed = False


                user = User(
                        user_full_name = row[1],
                        email = row[2],
                        # password_hash = row[3],
                        uzipcode = row[4],
                        is_asker= asker_seed,
                        is_vol= vol_seed,
                        trust_score = row[7]
                        )

                user.set_password(row[3])

                db.session.add(user)
                line_count += 1

        db.session.commit()
        print(f'created {line_count} users')


def add_relationals():
    """add relationship data to the relational table."""

    # r1 = Relational(
    #     r_asker_id= 1,
    #     r_vol_id = 2,
    #     r_trip_id = 1
    #     # r_vol_id= 2, 
    #     # r_trip_id = 1
    #     )

    # # print(f'{r1.r_trip_id}')

    # db.session.add(r1)

    # db.session.commit()
    # print(f'created relationals {r1}')

    """Load relationship information from seed file into the database.
    working code.
    """
    print("trips")

    # opening seed file with the csv library and csv reader. 
    with open('seed_files/Relational_seed_v1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:

                relation = Relational(
                            r_asker_id= int(row[1]),
                            r_vol_id = int(row[2]),
                            r_trip_id = int(row[3])
                            )

                db.session.add(relation)
                line_count += 1

        db.session.commit()
        print(f'created {line_count} relationals')


def add_trips():
    """Add trip data to the trips table."""

    # t1 = Trip(
    #         trip_zipcode= "94805",
    #         user_id= 1,
    #         wishlist = "Apples, berries, sweet potatoes",
    #         item_progress= "En Route"
    #         ) 

    # db.session.add(t1)
    # db.session.commit() 
    # print(f'created trips {t1}')

    """Load trip information from seed file into the database.
    working code.
    """
    print("trips")

    # opening seed file with the csv library and csv reader. 
    with open('seed_files/Trip_seed_v1.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            
            else:
                trip = Trip(
                        trip_zipcode= row[1],
                        user_id= int(row[2]),
                        wishlist = row[3],
                        item_progress= row[4]
                        ) 

                db.session.add(trip)
                line_count += 1

        db.session.commit()
        print(f'created {line_count} trips')

def add_wishlist():
    """Add wishlist data to the wishlist class."""

    w1 = Wishlist(
            ) 

    db.session.add(w1)
    db.session.commit() 
    print(f'created trips {w1}')   


################################################################################
# helper functions for seeding the model

if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Run functions
    # clear_tables()

    #load functions
    add_users()
    add_trips()
    add_relationals()

    inform_tables_loaded()

    print(f'\n\nusers table: {User.query.all()}')
    print(f'\n\ntrips table: {Trip.query.all()}')
    print(f'\n\nrelationals table: {Relational.query.all()}')
    print(f'\n\nwishlist table: {Wishlist.query.all()}')