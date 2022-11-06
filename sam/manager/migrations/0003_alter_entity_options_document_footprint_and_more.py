# Generated by Django 4.1.3 on 2022-11-06 15:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0002_alter_entity_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entity",
            options={"ordering": ["-name"]},
        ),
        migrations.AddField(
            model_name="document",
            name="footprint",
            field=models.CharField(default="NO-FOOTPRINT", max_length=255),
        ),
        migrations.AddField(
            model_name="document",
            name="stored_id",
            field=models.UUIDField(default=uuid.UUID("5eafc7ee-f814-4b14-8394-f9eb266b444d")),
        ),
        migrations.AlterField(
            model_name="document",
            name="project",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="documents", to="manager.project"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="entity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="projects", to="manager.entity"
            ),
        ),
    ]
