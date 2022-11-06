import hashlib
from os import path
import uuid
from django.conf import settings


def store_file(f):
    name = uuid.uuid4()
    root_dir = settings.ROOT_DOCUMENTS
    fullpath = path.join(root_dir, str(name))
    with open(fullpath, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    with open(fullpath, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")

    return (name, digest.hexdigest())
