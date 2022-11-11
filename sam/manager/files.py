import hashlib
from os import path
import pathlib
import uuid
from django.conf import settings


def get_path(document):
    root_dir = settings.MEDIA_ROOT
    suffix = pathlib.PurePath(document.name).suffix
    fullpath = path.join(root_dir, "{0}{1}".format(str(document.stored_id), suffix))
    return fullpath


def hash_file(fullpath):
    with open(fullpath, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
    return digest.hexdigest()


def create_storage(file_name):
    storage_id = uuid.uuid4()
    root_dir = settings.MEDIA_ROOT
    suffix = pathlib.PurePath(str(file_name)).suffix
    fullpath = path.join(root_dir, "{0}{1}".format(str(storage_id), suffix))
    return {"storage_id": storage_id, "fullpath": fullpath}
