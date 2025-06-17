"""Forms for my_plugin."""
from django import forms
from nautobot.utilities.forms import (
    BootstrapMixin,
    BulkEditForm,
    SlugField,
)

from my_plugin import models


class DevExampleForm(BootstrapMixin, forms.ModelForm):
    """DevExample creation/edit form."""

    slug = SlugField()

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        fields = [
            "name",
            "slug",
            "description",
        ]


class DevExampleBulkEditForm(BootstrapMixin, BulkEditForm):
    """DevExample bulk edit form."""

    pk = forms.ModelMultipleChoiceField(queryset=models.DevExample.objects.all(), widget=forms.MultipleHiddenInput)
    description = forms.CharField(required=False)

    class Meta:
        """Meta attributes."""

        nullable_fields = [
            "description",
        ]


class DevExampleFilterForm(BootstrapMixin, forms.ModelForm):
    """Filter form to filter searches."""

    q = forms.CharField(
        required=False,
        label="Search",
        help_text="Search within Name or Slug.",
    )
    name = forms.CharField(required=False, label="Name")
    slug = forms.CharField(required=False, label="Slug")

    class Meta:
        """Meta attributes."""

        model = models.DevExample
        # Define the fields above for ordering and widget purposes
        fields = [
            "q",
            "name",
            "slug",
            "description",
        ]
