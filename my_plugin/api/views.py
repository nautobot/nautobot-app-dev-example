"""API views for my_plugin."""

from nautobot.core.api.views import ModelViewSet

from my_plugin import filters, models

from my_plugin.api import serializers


class DevExampleViewSet(ModelViewSet):  # pylint: disable=too-many-ancestors
    """DevExample viewset."""

    queryset = models.DevExample.objects.all()
    serializer_class = serializers.DevExampleSerializer
    filterset_class = filters.DevExampleFilterSet

    # Option for modifying the default HTTP methods:
    # http_method_names = ["get", "post", "put", "patch", "delete", "head", "options", "trace"]
