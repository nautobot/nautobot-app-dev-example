"""Create fixtures for tests."""
from my_plugin.models import DevExample


def create_devexample():
    """Fixture to create necessary number of DevExample for tests."""
    DevExample.objects.create(name="Test One", slug="test-one")
    DevExample.objects.create(name="Test Two", slug="test-two")
    DevExample.objects.create(name="Test Three", slug="test-three")
