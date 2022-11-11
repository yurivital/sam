import uuid
import pathlib

from colorfield.fields import ColorField
from django.db import models


class Entity(models.Model):
    """Root of content hierarchy"""

    name = models.CharField(max_length=150, unique=True)
    color = ColorField(default="#FFFFFF")

    class Meta:
        ordering = ["color"]

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    """Container for documents forming an coherent ensemble"""

    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=150)

    class Meta:
        constraints = [models.UniqueConstraint(fields=["entity_id", "name"], name="Unique project name per entity")]

    def __str__(self) -> str:
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=15)
    codeAlpha3 = models.CharField(max_length=3)
    codeAlpha2 = models.CharField(max_length=2)

    def __str__(self) -> str:
        return self.name


class Document(models.Model):
    """Represent an traductable content"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="documents")
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING, null=True, related_name="languages")

    name = models.CharField(max_length=255)
    stored_id = models.UUIDField(default=uuid.uuid4())
    footprint = models.CharField(max_length=255, default="")
    size = models.BigIntegerField(default=0)

    @property
    def public_name(self):
        return "{}{}".format(self.stored_id, pathlib.PurePath(self.name).suffix)

    def __str__(self) -> str:
        return self.name
