from model import connect_to_db, db, User, Wishlist,Trip, Relational


def vol_update_status(trip_id):
    """Query database for new status."""

    trip = Trip.query.filter_by(trip_id=trip_id).first()

    status = trip.item_progress

    return {'status': status}
