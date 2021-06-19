from contextlib import contextmanager
from werkzeug.datastructures import FileStorage
from app.db.database import SessionLocal
from app.schemas.photo import (
    Photo,
    PhotoCreate,
    PhotoQuery,
    PhotoPatch,
    PhotoWithPagination,
)
from app.repo import photo as photoRepo
from app.util.photo_manager import PhotoManager

pm = PhotoManager()


@contextmanager
def get_db_session():

    session = SessionLocal()

    try:
        yield session
        session.commit()
    except:
        # also need to remove the data in the
        # data storage if possible
        session.rollback()
        raise
    finally:
        session.close()


def list_items(item_query: PhotoQuery) -> PhotoWithPagination:
    with get_db_session() as db:
        item_with_paging = photoRepo.get_all()
    return item_with_paging


def create_item(item_create: PhotoCreate, file: FileStorage) -> Photo:
    with get_db_session() as db:
        db_item = photoRepo.create(db=db, item_create=item_create)
        item = Photo.from_orm(db_item)
        # if upload fails, session will rollback
        # if session db.add() fails, upload will not happen
        pm.upload_file(file=file, key=item.id)
    return item


def delete_item(item_id: str) -> None:
    with get_db_session() as db:
        photoRepo.delete(db=db, item_id=item_id)
        # if above failed, raise error, delete file will not happen
    # if delete fails, it is an orphan file
    # will need some service to clean up if there is..
    # https://www.slsmk.com/use-boto3-to-recover-deleted-files-in-aws-s3-bucket/
    # the essence is that, need to enable versioning
    pm.delete_file(key=item_id)


def patch_item(item_id: str, item_patch: PhotoPatch) -> Photo:
    with get_db_session() as db:
        db_item = photoRepo.patch(db=db, item_id=item_id, item_patch=item_patch)
        item = Photo.from_orm(db_item)
    return item
