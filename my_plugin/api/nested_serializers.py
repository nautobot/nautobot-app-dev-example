"""API nested serializers for my_plugin."""
from rest_framework import serializers

from nautobot.core.api import WritableNestedSerializer

from my_plugin import models


class DevExampleNestedSerializer(WritableNestedSerializer):
    """DevExample Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:my_plugin-api:devexample-detail")

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        fields = "__all__"
