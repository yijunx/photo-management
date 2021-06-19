from gevent import monkey

monkey.patch_all()

from app.apis.app import app
