"""API nested serializers for nautobot_dev_example."""

from rest_framework import serializers

from nautobot.core.api import WritableNestedSerializer

from nautobot_dev_example import models


class DevExampleNestedSerializer(WritableNestedSerializer):
    """DevExample Nested Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:nautobot_dev_example-api:devexample-detail")

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        fields = "__all__"
