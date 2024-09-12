"""API serializers for nautobot_dev_example."""

from nautobot.apps.api import NautobotModelSerializer, TaggedModelSerializerMixin

from nautobot_dev_example import models


class DevExampleSerializer(NautobotModelSerializer, TaggedModelSerializerMixin):  # pylint: disable=too-many-ancestors
    """DevExample Serializer."""

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        fields = "__all__"

        # Option for disabling write for certain fields:
        # read_only_fields = []
