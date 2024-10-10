"""Views for nautobot_dev_example."""

from nautobot.apps.views import NautobotUIViewSet

from nautobot_dev_example import filters, forms, models, tables
from nautobot_dev_example.api import serializers


class DevExampleUIViewSet(NautobotUIViewSet):
    """ViewSet for DevExample views."""

    bulk_update_form_class = forms.DevExampleBulkEditForm
    filterset_class = filters.DevExampleFilterSet
    filterset_form_class = forms.DevExampleFilterForm
    form_class = forms.DevExampleForm
    lookup_field = "pk"
    queryset = models.DevExample.objects.all()
    serializer_class = serializers.DevExampleSerializer
    table_class = tables.DevExampleTable
