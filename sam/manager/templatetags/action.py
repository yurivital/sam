from pathlib import PurePath
from django import template
from django.urls import reverse
from django.template.loader import get_template

import logging

logger = logging.getLogger(__name__)

register = template.Library()


def display_actions(document):
    actions = []
    match document.mime_type:
        case item if item in ["image/png", "image/jpeg", "image/tiff", "image/gif"]:
            actions.append(
                {"text": "Convert to PDF", "url": reverse("manager:perform-action", args=("ocr", document.id))}
            )
        case item if item in ["audio/mpeg", "audio/flac"]:
            actions.append(
                {
                    "text": "Transcribe to text",
                    "url": reverse("manager:perform-action", args=("transcribe", document.id)),
                }
            )
    return {"actions": actions, "document": document}


users_template = get_template("action.html")
register.inclusion_tag(users_template)(display_actions)
