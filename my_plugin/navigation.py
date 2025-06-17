"""Menu items."""

from nautobot.extras.plugins import PluginMenuButton, PluginMenuItem
from nautobot.utilities.choices import ButtonColorChoices

menu_items = (
    PluginMenuItem(
        link="plugins:my_plugin:devexample_list",
        link_text="Nautobot Dev Example App",
        permissions=["my_plugin.view_devexample"],
        buttons=(
            PluginMenuButton(
                link="plugins:my_plugin:devexample_add",
                title="Add",
                icon_class="mdi mdi-plus-thick",
                color=ButtonColorChoices.GREEN,
                permissions=["my_plugin.add_devexample"],
            ),
        ),
    ),
)
