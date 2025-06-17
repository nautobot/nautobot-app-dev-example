"""Test DevExample Filter."""

from nautobot.apps.testing import FilterTestCases

from nautobot_dev_example import filters, models
from nautobot_dev_example.tests import fixtures


class DevExampleFilterTestCase(FilterTestCases.FilterTestCase):
    """DevExample Filter Test Case."""

    queryset = models.DevExample.objects.all()
    filterset = filters.DevExampleFilterSet
    generic_filter_tests = (
        ("id",),
        ("created",),
        ("last_updated",),
        ("name",),
    )

    @classmethod
    def setUpTestData(cls):
        """Setup test data for DevExample Model."""
        fixtures.create_devexample()

    def test_q_search_name(self):
        """Test using Q search with name of DevExample."""
        params = {"q": "Test One"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 1)

    def test_q_invalid(self):
        """Test using invalid Q search for DevExample."""
        params = {"q": "test-five"}
        self.assertEqual(self.filterset(params, self.queryset).qs.count(), 0)
