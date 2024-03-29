import pytesseract

from .models import Document
from .files import add_document, get_path


def perfom_ocr(document):
    """Extract text content from image and store into pdf file. Based on Tesseract OCR"""
    pdf_bytes = pytesseract.image_to_pdf_or_hocr(
        get_path(document), lang=document.language.codeAlpha3.lower(), extension="pdf"
    )
    user_file_name = "{0}.pdf".format(document.name)
    add_document(user_file_name, pdf_bytes, document.project, document.language)
