# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class avatar_props(ui5_tag_props, total=False):
    initials: str
    """Defines the displayed initials.
        Up to three Latin letters can be displayed as initials."""
    interactive: bool
    """Defines if the avatar is interactive (focusable and pressable)."""
    accessible_name: str
    """Defines the text alternative of the component. If not provided a default text
    alternative will be set, if present.
    """
    color_scheme: Literal[
        "Accent1",
        "Accent2",
        "Accent3",
        "Accent4",
        "Accent5",
        "Accent6",
        "Accent7",
        "Accent8",
        "Accent9",
        "Accent10",
        "Placeholder",
    ]
    """Defines the background color of the desired image."""
    icon: str
    """Defines the name of the UI5 Icon, that will be displayed.
    Note: If image slot is provided, the property will be ignored.
    Note: You should import the desired icon first, then use its name as 'icon'."""

    shape: Literal["Circle", "Square"]
    """Defines the shape of the component."""
    size: Literal["XS", "S", "M", "L", "XL"]
    """Defines the size of the component."""


class avatar(ui5_tag):
    """An image-like component that has different display options for representing
    images and icons in different shapes and sizes, depending on the use case.

    The shape can be circular or square. There are several predefined sizes, as well
    as an option to set a custom size.
    https://sap.github.io/ui5-webcomponents/playground/?path=/docs/main-avatar--docs
    """

    def __init__(self: Self, *args, **kwargs: Unpack[avatar_props]) -> None:
        self.tagname = "ui5-avatar"
        super().__init__(*args, **kwargs)


class avatar_group_props(ui5_tag_props, total=False):
    overflow_button: str
    """Defines the overflow button of the component. Note: We recommend using the
    ui5-button component.

    Note: If this slot is not used, the component will display
    the built-in overflow button."""

    type: Literal["Group", "Individual"]
    """Defines the mode of the AvatarGroup.

    Available options are:
    * Group
    * Individual"""


class avatar_group(ui5_tag):
    """Displays a group of avatars arranged horizontally. It is useful to visually
    showcase a group of related avatars, such as, project team members or employees.

    The component allows you to display the avatars in different sizes, depending on
    your use case.

    The AvatarGroup component has two group types:
    Group type: The avatars are displayed as partially overlapped on top of each other
    and the entire group has one click/tap area.
    Individual type: The avatars are displayed side-by-side and each avatar has its own
    click/tap area.

        https://sap.github.io/ui5-webcomponents/playground/?path=/docs/main-avatar-group--docs
    """

    def __init__(self: Self, *args, **kwargs: Unpack[avatar_group_props]) -> None:
        self.tagname = "ui5-avatar-group"
        super().__init__(*args, **kwargs)
