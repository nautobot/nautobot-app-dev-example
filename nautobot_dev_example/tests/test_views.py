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

    update_data = {
        "name": "Test 2",
        "description": "Updated model",
    }

    @classmethod
    def setUpTestData(cls):
        fixtures.create_devexample()
