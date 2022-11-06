import hashlib
from os import path
import uuid
from django.conf import settings


def store_file(f):
    name = uuid.uuid4()
    root_dir = settings.MEDIA_ROOT
    fullpath = path.join(root_dir, str(name))
    with open(fullpath, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    with open(fullpath, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")

    filesize = path.getsize(fullpath)

    return {"name": name, "footprint": digest.hexdigest(), "size": filesize}
