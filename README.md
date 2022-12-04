# SAM

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

[![SAM CI](https://github.com/yurivital/sam/actions/workflows/github-actions-main.yml/badge.svg)](https://github.com/yurivital/sam/actions/workflows/github-actions-main.yml)

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
- Tesseract OCR 4.1 for Image-to-Text transformation
- Whisper for Speech-To-Text transcriptions whih rely on :
  - ffmpeg

## Developpment

```python
poetry install
poetry run sam/manage.py migrate
poetry run sam/manage.py runserver
```
