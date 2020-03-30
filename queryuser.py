from model import connect_to_db, db, User, Wishlist,Trip, Relational

def get_user_email(user_id):
    """Query database for user email.

    Examples:
        >>> get_user_email('1')
        msdaiyichen@gmail.com
        >>> get_user_email('2')
        jessica@gmail.com
    """
    # Get user email via its id
    user = User.query.filter_by(user_id=user_id).first()
    # print(user.email)
    return user.email


def get_user_zipcode(user_id):
    """Query database for user zipcode.

    Examples:
        >>> get_user_zipcode('1')
        'ca 94014'
        >>> get_user_zipcode('2')
        'ca 94134'
    """
    # Get user email via its id
    user = User.query.filter_by(user_id=user_id).first()
    # print(user.uzipcode)
    return user.uzipcode


def add_wishlist(new_wishlist, zipcode, asker):
    pass
#     """Send asker's wishlist to the database."""

#     this_trip = Trip.query.filter_by(user_id=asker).first()
#     print("before update", this_trip)
#     this_trip.wishlist = new_wishlist

#     this_trip.uzipcode = zipcode
    
#     db.session.commit()
#     print("After update", this_user)
#     return 'New wishlist created.'


def get_wishlist(user_id):
    """Query database for wishlist and status."""

    this_trip = Trip.query.filter_by(user_id=user_id).first()

    wishlist = this_trip.wishlist
    # print(wishlist)
    status = this_trip.item_progress
    # print(status)
    return {'wishlist': wishlist, 'status': status}
    

def update_status(user_id):
    """Query database for new status."""

    this_user = User.query.filter_by(user_id=asker).first()

    status = this_user.item_progress

    return {'status': status}


############################################################################
if __name__ == "__main__":

  from server import app
  import doctest

  connect_to_db(app)
  print("Connected to DB.")
  
  if doctest.testmod().failed == 0:
      print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")