"""Create fixtures for tests."""

from nautobot_dev_example.models import DevExample


def create_devexample():
    """Fixture to create necessary number of DevExample for tests."""
    DevExample.objects.create(name="Test One")
    DevExample.objects.create(name="Test Two")
    DevExample.objects.create(name="Test Three")
