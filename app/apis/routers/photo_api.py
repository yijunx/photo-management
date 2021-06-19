from flask import Blueprint
from app.service import photo as photoService
from app.schemas.photo import PhotoPatch, PhotoQuery
from flask_pydantic import validate


photo_bq = Blueprint("photo_bq", __name__)


@photo_bq.route("", methods=["GET"])
@validate(query=PhotoQuery)
def list_photos():

    try:
        photos = photoService.list_items()
    except:
        raise
    return photos


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
