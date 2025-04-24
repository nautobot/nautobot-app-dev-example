"""Unit tests for nautobot_dev_example."""

from nautobot.apps.testing import APIViewTestCases

from nautobot_dev_example import models
from nautobot_dev_example.tests import fixtures


class DevExampleAPIViewTest(APIViewTestCases.APIViewTestCase):
    # pylint: disable=too-many-ancestors
    """Test the API viewsets for DevExample."""

    model = models.DevExample

    @classmethod
    def setUpTestData(cls):
        """Create test data for DevExample API viewset."""
        super().setUpTestData()
        # Create 3 objects for the generic API test cases.
        fixtures.create_devexample()
        # Provided data for 3 objects to be created.
        cls.create_data = [
            {
                "name": "API Test One",
                "description": "Test One Description",
            },
            {
                "name": "API Test Two",
                "description": "Test Two Description",
            },
            {
                "name": "API Test Three",
                "description": "Test Three Description",
            },
        ]
        cls.update_data = {
            "name": "Update Test Two",
            "description": "Test Two Description",
        }
        cls.bulk_update_data = {
            "description": "Test Bulk Update Description",
        }
