"""Plugin declaration for my_plugin."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import NautobotAppConfig


class NautobotDevExampleConfig(NautobotAppConfig):
    """Plugin configuration for the my_plugin plugin."""

    name = "my_plugin"
    verbose_name = "Nautobot Dev Example App"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot App to demonstrate how to create a Nautobot App.."
    base_url = "dev-example"
    required_settings = []
    min_version = "2.0.0"
    max_version = "2.9999"
    default_settings = {}
    caching_config = {}


config = NautobotDevExampleConfig  # pylint:disable=invalid-name
