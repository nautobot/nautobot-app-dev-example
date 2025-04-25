"""Filtering for nautobot_dev_example."""

from nautobot.apps.filters import NameSearchFilterSet, NautobotFilterSet

from nautobot_dev_example import models


class DevExampleFilterSet(NautobotFilterSet, NameSearchFilterSet):  # pylint: disable=too-many-ancestors
    """Filter for DevExample."""

    class Meta:
        """Meta attributes for filter."""

        model = models.DevExample

        # add any fields from the model that you would like to filter your searches by using those
        fields = "__all__"
