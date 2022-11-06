from django.contrib import admin

from .models import Entity, Project, Language

admin.site.register(Entity)
admin.site.register(Project)
admin.site.register(Language)
