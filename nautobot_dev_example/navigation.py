"""Menu items."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:nautobot_dev_example:devexample_list",
        link_text="Nautobot Dev Example App",
        permissions=["nautobot_dev_example.view_devexample"],
        buttons=(
            PluginMenuButton(
                link="plugins:nautobot_dev_example:devexample_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["nautobot_dev_example.add_devexample"],
            ),
        ),
    ),
)
