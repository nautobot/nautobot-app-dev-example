"""Filtering for nautobot_dev_example."""

from nautobot.utilities.filters import BaseFilterSet, NameSlugSearchFilterSet

from nautobot_dev_example import models


class DevExampleFilterSet(BaseFilterSet, NameSlugSearchFilterSet):
    """Filter for DevExample."""

    class Meta:
        """Meta attributes for filter."""

        model = models.DevExample

        # add any fields from the model that you would like to filter your searches by using those
        fields = ["id", "name", "slug", "description"]
