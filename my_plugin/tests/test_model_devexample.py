"""Test DevExample."""

from django.test import TestCase

from my_plugin import models


class TestDevExample(TestCase):
    """Test DevExample."""

    def test_create_devexample_only_required(self):
        """Create with only required fields, and validate null description and __str__."""
        devexample = models.DevExample.objects.create(name="Development", slug="development")
        self.assertEqual(devexample.name, "Development")
        self.assertEqual(devexample.description, "")
        self.assertEqual(str(devexample), "Development")
        self.assertEqual(devexample.slug, "development")

    def test_create_devexample_all_fields_success(self):
        """Create DevExample with all fields."""
        devexample = models.DevExample.objects.create(
            name="Development", slug="development", description="Development Test"
        )
        self.assertEqual(devexample.name, "Development")
        self.assertEqual(devexample.slug, "development")
        self.assertEqual(devexample.description, "Development Test")
