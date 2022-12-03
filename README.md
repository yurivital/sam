# sam

## Dependecies

- Python 3.11+
- Django 4+
- libmagic for file type detection
- Tesseract OCR 4.1 for image to text transformation

## Developpment

```python
poetry install
poetry run sam/manage.py migrate
poetry run sam/manage.py runserver
```
