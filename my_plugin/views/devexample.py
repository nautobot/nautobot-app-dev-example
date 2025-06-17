"""Views for DevExample."""

from nautobot.core.views import generic

from my_plugin import filters, forms, models, tables


class DevExampleListView(generic.ObjectListView):
    """List view."""

    queryset = models.DevExample.objects.all()
    # These aren't needed for simple models, but we can always add
    # this search functionality.
    filterset = filters.DevExampleFilterSet
    filterset_form = forms.DevExampleFilterForm
    table = tables.DevExampleTable

    # Option for modifying the top right buttons on the list view:
    # action_buttons = ("add", "import", "export")


class DevExampleView(generic.ObjectView):
    """Detail view."""

    queryset = models.DevExample.objects.all()


class DevExampleCreateView(generic.ObjectEditView):
    """Create view."""

    model = models.DevExample
    queryset = models.DevExample.objects.all()
    model_form = forms.DevExampleForm


class DevExampleDeleteView(generic.ObjectDeleteView):
    """Delete view."""

    model = models.DevExample
    queryset = models.DevExample.objects.all()


class DevExampleEditView(generic.ObjectEditView):
    """Edit view."""

    model = models.DevExample
    queryset = models.DevExample.objects.all()
    model_form = forms.DevExampleForm


class DevExampleBulkDeleteView(generic.BulkDeleteView):
    """View for deleting one or more DevExample records."""

    queryset = models.DevExample.objects.all()
    table = tables.DevExampleTable


class DevExampleBulkEditView(generic.BulkEditView):
    """View for editing one or more DevExample records."""

    queryset = models.DevExample.objects.all()
    table = tables.DevExampleTable
    form = forms.DevExampleBulkEditForm
