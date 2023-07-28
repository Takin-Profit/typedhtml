from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class nav_props(ion_tag_props):
    animated: bool
    root: str
    swipe_gesture: bool


class nav(ion_tag):
    """Nav is a standalone component for loading arbitrary components
    and pushing new components on to the stack.

    see: `https://ionicframework.com/docs/api/nav` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[nav_props]) -> None:
        self.tagname = "ion-nav"
        super().__init__(*args, **kwargs)


class nav_link_props(ion_tag_props):
    component: str
    router_direction: Literal["back", "forward", "root"]


class nav_link(ion_tag):
    """Nav Link is a component used to navigate to a specified component.

    see: `https://ionicframework.com/docs/api/nav-link` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[nav_link_props]) -> None:
        self.tagname = "ion-nav-link"
        super().__init__(*args, **kwargs)
