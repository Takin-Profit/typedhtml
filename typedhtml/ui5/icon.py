# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class icon_props(ui5_tag_props, total=False):
    name: str
    accessible_name: str
    accessible_role: str
    design: Literal[
        "Contrast",
        "Critical",
        "Default",
        "Negative",
        "Neutral",
        "Positive",
        "Information",
        "NonInteractive",
    ]
    interactive: bool
    show_tooltip: bool


class icon(ui5_tag):
    """The ui5-icon component represents an SVG icon. There are two main scenarios how
    the ui5-icon component is used: as a purely decorative element,
    or as an interactive element that can be focused and clicked."""

    def __init__(self, *args, **kwargs: Unpack[icon_props]) -> None:
        self.tagname = "ui5-icon"
        super().__init__(*args, **kwargs)
