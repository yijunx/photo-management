from flask import Blueprint


photo_bq = Blueprint("photo_bq", __name__)


@photo_bq.route("", methods=["GET"])
def list_photos():
    return "nihao"


@photo_bq.route("", methods=["POST"])
def post_photos():
    return "nihao"


@photo_bq.route("/<photo_id>", methods=["GET"])
def get_photo(photo_id: str):
    return "nihao"


@photo_bq.route("/<photo_id>", methods=["PATCH"])
def update_photo(photo_id: str):
    return "nihao"


@photo_bq.route("/<photo_id>", methods=["DELETE"])
def delete_photo(photo_id: str):
    return "nihao"
