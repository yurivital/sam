from django.db import models


class Entity(models.Model):
    """Root of content hierarchy"""
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    """Container for documents forming an coherent ensemble"""
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Document(models.Model):
    """Represent an traductable content"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name
