from pathlib import PurePath
from django import template
from django.urls import reverse
from django.template.loader import get_template

register = template.Library()


def display_actions(document):
    actions = []
    extentions = PurePath(document.name).suffix
    print(extentions)
    match extentions:
        case item if item in [".png", ".jpg", ".tiff", ".gif"]:
            actions.append(
                {"text": "Convert to PDF", "url": reverse("manager:perform-action", args=("ocr", document.id))}
            )
        case item if item in [".txt", ".pdf", ".doc", ".docx"]:
            actions.append(
                {"text": "Translate", "url": reverse("manager:perform-action", args=("translate", document.id))}
            )
    print(actions)
    return {"actions": actions, "document": document}


users_template = get_template("action.html")
register.inclusion_tag(users_template)(display_actions)
