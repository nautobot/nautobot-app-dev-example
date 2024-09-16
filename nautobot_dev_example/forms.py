"""Forms for nautobot_dev_example."""

from django import forms
from nautobot.apps.forms import NautobotBulkEditForm, NautobotFilterForm, NautobotModelForm, TagsBulkEditFormMixin

from nautobot_dev_example import models


class DevExampleForm(NautobotModelForm):  # pylint: disable=too-many-ancestors
    """DevExample creation/edit form."""

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        fields = "__all__"


class DevExampleBulkEditForm(TagsBulkEditFormMixin, NautobotBulkEditForm):  # pylint: disable=too-many-ancestors
    """DevExample bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.DevExample.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class DevExampleFilterForm(NautobotFilterForm):
    """Filter form to filter searches."""

    model = models.DevExample
    field_order = ["q", "name"]

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
