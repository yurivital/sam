from django.test import TestCase
from django.db.utils import IntegrityError

from .models import Entity, Project, Language, Document
from .files import add_document


fixture_dumb_image_with_text = "./sam/manager/fixtures/dumb_image.png"


class HierarchyModelTest(TestCase):
    def test_entity_should_be_unique(self):
        t1 = Entity.objects.create(name="Entity1")
        with self.assertRaises(IntegrityError):
            Entity.objects.create(name=t1.name)

    def test_entity_can_contain_project(self):
        t1 = Entity.objects.create(name="Entity1")
        Project.objects.create(name="Project1", entity_id=t1.id)

    def test_project_name_is_unique_entity(self):
        t1 = Entity.objects.create(name="Entity1")
        Project.objects.create(name="Project1", entity_id=t1.id)
        with self.assertRaises(IntegrityError):
            Project.objects.create(name="Project1", entity_id=t1.id)

    def test_project_name_is_not_unique_globaly(self):
        t1 = Entity.objects.create(name="Entity1")
        t2 = Entity.objects.create(name="Entity2")
        p1 = Project.objects.create(name="Project1", entity_id=t1.id)
        p2 = Project.objects.create(name="Project1", entity_id=t2.id)
        self.assertEqual(p1.name, p2.name)
        self.assertNotEqual(p1.id, p2.id)


class StorageTest(TestCase):
    def test_can_store_document(seld):
        e1 = Entity.objects.create(name="Entity1")
        p1 = Project.objects.create(name="Project1", entity_id=e1.id)
        french = Language.objects.create(name="Français", codeAlpha3="FRA", codeAlpha2="FR")

        with open(fixture_dumb_image_with_text, "rb") as f:
            content = f.read()
            dumb_doc = add_document(user_file_name="dumb_image.png", file_content=content, project=p1, language=french)
            assert (
                dumb_doc.footprint == "7fc35c249462834bc672ef618c9ad438873c120c935dae696b35f270cee68125"
            ), "Should be SHA256 of file content"
            assert dumb_doc.size == 437, "Should be 437 bytes"
            assert dumb_doc.mime_type == "image/png", "Should be image/png mime type"
