import uuid
from django.db import models
from colorfield.fields import ColorField


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


class Document(models.Model):
    """Represent an traductable content"""

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="documents")
    name = models.CharField(max_length=255)
    stored_id = models.UUIDField(default=uuid.uuid4())
    footprint = models.CharField(max_length=255, default="NO-FOOTPRINT")

    def __str__(self) -> str:
        return self.name
