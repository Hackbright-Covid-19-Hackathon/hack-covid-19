from model import connect_to_db, db, User, Wishlist,Trip, Relational

def get_user_email(user_id):
    """Query database for user email.

    Examples:
        >>> get_user_email('johnsonamanda@hotmail.com')
        1
        >>> get_user_email('msdaiyichen@gmail.com')
        48
    """

    # Get user email via its id
    user = User.query.filter_by(user_id=user_id).first()
    
    return user.email


def get_user_zipcode(user_id):
    """Query database for user zipcode.

    Examples:
        >>> get_user_id('johnsonamanda@hotmail.com')
        1
        >>> get_user_id('msdaiyichen@gmail.com')
        48
    """

    # Get user email via its id
    user = User.query.filter_by(user_id=user_id).first()
    
    return user.uzipcode


############################################################################
if __name__ == "__main__":

  from server import app
  import doctest

  connect_to_db(app)
  print("Connected to DB.")
  
  if doctest.testmod().failed == 0:
      print("\n*** ALL TESTS PASSED. YOU CAUGHT ALL THE STRAY PARENS!\n")