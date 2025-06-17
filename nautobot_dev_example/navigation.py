"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:nautobot_dev_example:devexample_list",
        name="Nautobot Dev Example App",
        permissions=["nautobot_dev_example.view_devexample"],
        buttons=(
            NavMenuAddButton(
                link="plugins:nautobot_dev_example:devexample_add",
                permissions=["nautobot_dev_example.add_devexample"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Nautobot Dev Example App", items=tuple(items)),),
    ),
)
