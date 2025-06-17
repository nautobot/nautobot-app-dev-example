"""API views for nautobot_dev_example."""

from nautobot.apps.api import NautobotModelViewSet

from nautobot_dev_example import filters, models
from nautobot_dev_example.api import serializers


class DevExampleViewSet(NautobotModelViewSet):  # pylint: disable=too-many-ancestors
    """DevExample viewset."""

    queryset = models.DevExample.objects.all()
    serializer_class = serializers.DevExampleSerializer
    filterset_class = filters.DevExampleFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
