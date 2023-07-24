# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class breadcrumbs_props(ui5_tag_props, total=False):
    design: Literal["Standard", "NoCurrentPage"]
    separator_style: Literal[
        "Slash",
        "BackSlash",
        "DoubleGreaterThan",
        "DoubleSlash",
        "DoubleBackSlash",
        "GreaterThan",
    ]


class breadcrumbs(ui5_tag):
    """Displays a list of links that shows the navigation path."""

    def __init__(self, *args, **kwargs: Unpack[breadcrumbs_props]) -> None:
        self.tagname = "ui5-breadcrumbs"
        super().__init__(*args, **kwargs)


class breadcrumbs_item_props(ui5_tag_props, total=False):
    href: str
    target: Literal["_self", "_top", "_parent", "_blank", "_search"]
    accessible_name: str


class breadcrumbs_item(ui5_tag):
    """Represents a clickable element, used in the ui5-breadcrumbs navigation.
    The user can navigate to the previous location in the app when the user clicks
    on the ui5-breadcrumbs item."""

    def __init__(self, *args, **kwargs: Unpack[breadcrumbs_item_props]) -> None:
        self.tagname = "ui5-breadcrumbs-item"
        super().__init__(*args, **kwargs)
