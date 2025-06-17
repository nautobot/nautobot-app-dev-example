"""Unit tests for my_plugin."""
from nautobot.utilities.testing import APIViewTestCases

from my_plugin import models
from my_plugin.tests import fixtures


class DevExampleAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for DevExample."""

    model = models.DevExample
    create_data = [
        {
            "name": "Test Model 1",
            "slug": "test-model-1",
        },
        {
            "name": "Test Model 2",
            "slug": "test-model-2",
        },
    ]
    bulk_update_data = {"description": "Test Bulk Update"}
    brief_fields = ["created", "description", "display", "id", "last_updated", "name", "slug", "url"]

    @classmethod
    def setUpTestData(cls):
        fixtures.create_devexample()
