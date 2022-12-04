# sam

SAM is an toolbox for people dealing with various type of documents in different languages.
Specifications are mainly edicted by my beloved wife, but feel free make suggestions.

## Principle

### Document manager

The atomic element of the system is the `Document`, basicly a file, that can receive transformations, such as automatic translation, Optical character recognition, Speech-To-Text, ...

Document are handled by a file manager, wich organise documents by `Entities` (can be client or Business Unit) and by `Project`.

## Dependencies

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
