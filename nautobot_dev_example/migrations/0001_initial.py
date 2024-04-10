# Generated by Django 3.2.21 on 2024-02-16 08:32

import uuid

import django.core.serializers.json
import nautobot.core.models.fields
import nautobot.extras.models.mixins
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("extras", "0098_rename_data_jobresult_result"),
    ]

    operations = [
        migrations.CreateModel(
            name="DevExample",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "_custom_field_data",
                    models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.CharField(blank=True, max_length=200)),
                ("tags", nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag")),
            ],
            options={
                "ordering": ["name"],
            },
            bases=(
                models.Model,
                nautobot.extras.models.mixins.DynamicGroupMixin,
                nautobot.extras.models.mixins.NotesMixin,
            ),
        ),
    ]
