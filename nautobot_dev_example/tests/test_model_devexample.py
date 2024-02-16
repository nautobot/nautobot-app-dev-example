"""Test DevExample."""

from django.test import TestCase

from nautobot_dev_example import models


class TestDevExample(TestCase):
    """Test DevExample."""

    def test_create_devexample_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        devexample = models.DevExample.objects.create(name="Development")
        self.assertEqual(devexample.name, "Development")
        self.assertEqual(devexample.description, "")
        self.assertEqual(str(devexample), "Development")

    def test_create_devexample_all_fields_success(self):
        """Create DevExample with all fields."""
        devexample = models.DevExample.objects.create(name="Development", description="Development Test")
        self.assertEqual(devexample.name, "Development")
        self.assertEqual(devexample.description, "Development Test")
