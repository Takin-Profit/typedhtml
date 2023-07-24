# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class panel_props(ui5_tag_props):
    header_text: str
    accessible_name: str
    accessible_role: str
    collapsed: bool
    fixed: bool
    header_level: Literal["H6", "H5", "H4", "H3", "H2", "H1"]
    no_animation: bool


class panel(ui5_tag):
    """The ui5-panel component is a container which has a header and a content area and
    can be collapsed to save space on the screen."""

    def __init__(self, *args, **kwargs: Unpack[panel_props]) -> None:
        self.tagname = "ui5-panel"
        super().__init__(*args, **kwargs)
