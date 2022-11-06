# Generated by Django 4.1.3 on 2022-11-06 19:15

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("manager", "0004_alter_entity_options_entity_color_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Language",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=15)),
                ("codeAlpha3", models.CharField(max_length=3)),
                ("codeAlpha2", models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name="entity",
            options={"ordering": ["color"]},
        ),
        migrations.AddField(
            model_name="document",
            name="size",
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="document",
            name="footprint",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="document",
            name="stored_id",
            field=models.UUIDField(default=uuid.UUID("cda0324e-c0e6-41ef-b9e8-805a0bcc15c7")),
        ),
        migrations.AlterField(
            model_name="entity",
            name="color",
            field=colorfield.fields.ColorField(default="#FFFFFF", image_field=None, max_length=18, samples=None),
        ),
        migrations.AddField(
            model_name="document",
            name="language",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="languages",
                to="manager.language",
            ),
        ),
    ]
