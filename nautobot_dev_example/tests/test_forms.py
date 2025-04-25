"""Test devexample forms."""

from django.test import TestCase

from nautobot_dev_example import forms


class DevExampleTest(TestCase):
    """Test DevExample forms."""

    def test_specifying_all_fields_success(self):
        form = forms.DevExampleForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.DevExampleForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_devexample_is_required(self):
        form = forms.DevExampleForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
