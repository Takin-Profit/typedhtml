# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class menu_props(ion_tag_props):
    content_id: str
    disabled: bool
    max_edge_start: int
    menu_id: str
    side: Literal["start", "end"]
    swipe_gesture: bool
    type_: Literal["overlay", "reveal", "push"]


class menu(ion_tag):
    """The menu component is a navigation drawer that slides in from the side of the
    current view. By default, it uses the start side, making it slide in from the left
    for LTR and right for RTL, but the side can be overridden. The menu will be
    displayed differently based on the mode, however the display type can be changed
    to any of the available menu types.

    see: `https://ionicframework.com/docs/api/menu` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[menu_props]) -> None:
        self.tagname = "ion-menu"
        super().__init__(*args, **kwargs)


class menu_button_props(ion_tag_props):
    auto_hide: bool
    color: Color
    disabled: bool
    menu: str
    type_: Literal["button", "reset", "submit"]


class menu_button(ion_tag):
    """The Menu Button component contains an icon and automatically
    adds functionality to open a menu when clicked.

    see: `https://ionicframework.com/docs/api/menu-button` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[menu_button_props]) -> None:
        self.tagname = "ion-menu-button"
        super().__init__(*args, **kwargs)


class menu_toggle_props(ion_tag_props):
    auto_hide: bool
    menu: str


class menu_toggle(ion_tag):
    """The Menu Toggle component allows the user to toggle a menu open or closed.

    see: `https://ionicframework.com/docs/api/menu-toggle` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[menu_toggle_props]) -> None:
        self.tagname = "ion-menu-toggle"
        super().__init__(*args, **kwargs)


class split_pane_props(ion_tag_props):
    content_id: str
    disabled: bool
    when: bool


class split_pane(ion_tag):
    """A split pane is useful when creating multi-view layouts. It allows UI elements,
    like menus, to be displayed as the viewport width increases."""

    def __init__(self: Self, *args: Any, **kwargs: Unpack[split_pane_props]) -> None:
        self.tagname = "ion-split-pane"
        super().__init__(*args, **kwargs)
