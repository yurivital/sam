from ast import Assert
from unicodedata import name
from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Entity, Project

# Create your tests here.


class HierarchyModelTest(TestCase):
    def test_entity_should_be_unique(self):
        t1 = Entity.objects.create(name="Entity1")
        t1.save()
        with self.assertRaises(IntegrityError):
            Entity.objects.create(name=t1.name)

    def test_entity_can_contain_project(self):
        t1 = Entity.objects.create(name="Entity1")
        t1.save()
        p1 = Project.objects.create(name="Project1", entity_id=t1.id)
        p1.save()

    def test_project_name_is_unique_entity(self):
        t1 = Entity.objects.create(name="Entity1")
        t1.save()
        p1 = Project.objects.create(name="Project1", entity_id=t1.id)
        with self.assertRaises(IntegrityError):
            p2 = Project.objects.create(name="Project1", entity_id=t1.id)

    def test_project_name_is_not_unique_globaly(self):
        t1 = Entity.objects.create(name="Entity1")
        t2 = Entity.objects.create(name="Entity2")
        t1.save()
        t2.save()
        p1 = Project.objects.create(name="Project1", entity_id=t1.id)
        p2 = Project.objects.create(name="Project1", entity_id=t2.id)
        p1.save()
        p2.save()
        self.assertEqual(p1.name, p2.name)
        self.assertNotEqual(p1.id, p2.id)
