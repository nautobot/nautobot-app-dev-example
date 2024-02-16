"""Unit tests for views."""

from nautobot.apps.testing import ViewTestCases

from nautobot_dev_example import models
from nautobot_dev_example.tests import fixtures


class DevExampleViewTest(ViewTestCases.PrimaryObjectViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the DevExample views."""

    model = models.DevExample
    bulk_edit_data = {"description": "Bulk edit views"}
    form_data = {
        "name": "Test 1",
        "description": "Initial model",
    }
    csv_data = (
        "name",
        "Test csv1",
        "Test csv2",
        "Test csv3",
    )

    @classmethod
    def setUpTestData(cls):
        fixtures.create_devexample()
