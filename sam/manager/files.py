import hashlib
from os import path
import pathlib
import uuid
import magic

from django.conf import settings
from django.core.files.uploadedfile import UploadedFile
from .models import Document


def get_path(document):
    """Return storage absolute path of a document"""
    root_dir = settings.MEDIA_ROOT
    suffix = pathlib.PurePath(document.name).suffix
    fullpath = path.join(root_dir, "{0}{1}".format(str(document.stored_id), suffix))
    return fullpath


def add_document(user_file_name, file_content, project, language):
    """Store file content and create a document record"""
    storage_id = uuid.uuid4()
    root_dir = settings.MEDIA_ROOT
    suffix = pathlib.PurePath(str(user_file_name)).suffix
    fullpath = path.join(root_dir, "{0}{1}".format(str(storage_id), suffix))

    if isinstance(file_content, UploadedFile):
        with open(fullpath, "wb+") as destination:
            for chunk in file_content.chunks():
                destination.write(chunk)
    elif isinstance(file_content, bytes):
        with open(fullpath, "w+b") as f:
            f.write(file_content)
    else:
        raise NotImplementedError('File content format "{}" not handled '.format(type(file_content)))

    with magic.Magic(flags=magic.MAGIC_MIME_TYPE) as m:
        mime_type = m.id_filename(fullpath)

    with open(fullpath, "rb") as f:
        digest = hashlib.file_digest(f, "sha256")
        hash = digest.hexdigest()

    return Document.objects.create(
        name=user_file_name,
        stored_id=storage_id,
        project=project,
        language=language,
        footprint=hash,
        size=path.getsize(fullpath),
        mime_type=mime_type,
    )
