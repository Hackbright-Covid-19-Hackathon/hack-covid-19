from model import connect_to_db, db, User, Wishlist,Trip, Relational

def get_user_email(user_id):
    """Query database for user id.

    Examples:
        >>> get_user_id('johnsonamanda@hotmail.com')
        1
        >>> get_user_id('msdaiyichen@gmail.com')
        48
    """

    # Get user email via its id
    user = User.query.filter_by(user_id=user_id).first()
    
    return user.email


if __name__ == "__main__":

  from server import app
  
  connect_to_db(app)
  
  print("Connected to DB.")