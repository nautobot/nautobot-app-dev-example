"""Unit tests for nautobot_dev_example."""

from nautobot.apps.testing import APIViewTestCases

from nautobot_dev_example import models
from nautobot_dev_example.tests import fixtures


class DevExampleAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for DevExample."""

    model = models.DevExample
    create_data = [
        {
            "name": "Test Model 1",
            "description": "test description",
        },
        {
            "name": "Test Model 2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}

    @classmethod
    def setUpTestData(cls):
        fixtures.create_devexample()
