# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class list_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_name_ref: str
    accessible_role: str
    busy: bool
    busy_delay: int
    footer_text: str
    growing: Literal["Button", "Scroll"]
    header_text: str
    indent: bool
    mode: Literal[
        "None",
        "SingleSelect",
        "SingleSelectBegin",
        "SingleSelectEnd",
        "MultiSelect",
        "Delete",
    ]
    no_data_text: str
    separators: Literal["All", "Inner", "None"]


class list(ui5_tag):
    """The List component allows displaying a list of items, advanced keyboard
    handling support for navigating between items, and predefined modes to
    improve the development efficiency."""

    def __init__(self, *args, **kwargs: Unpack[list_props]) -> None:
        self.tagname = "ui5-list"
        super().__init__(*args, **kwargs)
