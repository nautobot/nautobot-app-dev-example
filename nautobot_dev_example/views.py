"""Views for nautobot_dev_example."""

from nautobot.apps.ui import ObjectDetailContent, ObjectFieldsPanel, SectionChoices
from nautobot.apps.views import NautobotUIViewSet

# if/when use the table, uncomment the following lines
# from nautobot.core.templatetags import helpers
# from nautobot.apps.ui import ObjectsTablePanel
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

    # Here is an example of using the UI  Component Framework for the detail view.
    # More information can be found in the Nautobot documentation:
    # https://docs.nautobot.com/projects/core/en/stable/development/core/ui-component-framework/
    object_detail_content = ObjectDetailContent(
        panels=[
            ObjectFieldsPanel(
                weight=100,
                section=SectionChoices.LEFT_HALF,
                fields="__all__",
                # Alternatively, you can specify a list of field names:
                # fields=[
                #     "name",
                #     "description",
                # ],
                # Some fields may require additional configuration, we can use value_transforms
                # value_transforms={
                #     "name": [helpers.bettertitle]
                # },
            ),
            # If there is a ForeignKey or M2M with this model we can use ObjectsTablePanel
            # to display them in a table format.
            # ObjectsTablePanel(
            # weight=200,
            # section=SectionChoices.RIGHT_HALF,
            # table_class=tables.DevExampleTable,
            # You will want to filter the table using the related_name
            # filter="devexamples",
            # ),
        ],
    )
