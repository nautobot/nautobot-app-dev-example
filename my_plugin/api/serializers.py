"""API serializers for my_plugin."""
from rest_framework import serializers

from nautobot.core.api.serializers import ValidatedModelSerializer

from my_plugin import models

from . import nested_serializers  # noqa: F401, pylint: disable=unused-import


class DevExampleSerializer(ValidatedModelSerializer):
    """DevExample Serializer."""

    url = serializers.HyperlinkedIdentityField(view_name="plugins-api:my_plugin-api:devexample-detail")

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
