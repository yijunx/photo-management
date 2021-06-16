from flask import Blueprint


photo_bq = Blueprint("photo_bq", url_prefix="/api/photos")


@photo_bq.route("", methods="GET")
def list_photos():
    return


@photo_bq.route("", methods="POST")
def post_photos():
    return


@photo_bq.route("/<photo_id>", methods="GET")
def get_photo():
    return



@photo_bq.route("/<photo_id>", methods="PATCH")
def update_photo():
    return


@photo_bq.route("/<photo_id>", methods="DELETE")
def delete_photo():
    return
    


