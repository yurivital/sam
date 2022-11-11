import pytesseract
import os

from .models import Document
from .files import create_storage, get_path, hash_file


def perfom_ocr(document):
    pdf_bytes = pytesseract.image_to_pdf_or_hocr(
        get_path(document), lang=document.language.codeAlpha3.lower(), extension="pdf"
    )
    user_file_name = "{0}.pdf".format(document.name)
    storage = create_storage(user_file_name)
    with open(storage["fullpath"], "w+b") as f:
        f.write(pdf_bytes)
    Document.objects.create(
        name=user_file_name,
        stored_id=storage["storage_id"],
        footprint=hash_file(storage["fullpath"]),
        size=os.path.getsize(storage["fullpath"]),
        project=document.project,
        language=document.language,
    )
