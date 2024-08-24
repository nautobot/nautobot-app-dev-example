"""Plugin declaration for nautobot_dev_example."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
from importlib import metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import NautobotAppConfig


class NautobotDevExampleConfig(NautobotAppConfig):
    """Plugin configuration for the nautobot_dev_example plugin."""

    name = "nautobot_dev_example"
    verbose_name = "Nautobot Dev Example App"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot App to demonstrate how to create a Nautobot App.."
    base_url = "dev-example"
    required_settings = []
    min_version = "1.6.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotDevExampleConfig  # pylint:disable=invalid-name
