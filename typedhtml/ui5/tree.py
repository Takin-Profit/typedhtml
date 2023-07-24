# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class tree_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_name_ref: str
    footer_text: str
    header_text: str
    mode: Literal[
        "None",
        "SingleSelect",
        "SingleSelectBegin",
        "SingleSelectEnd",
        "MultiSelect",
        "Delete",
    ]
    no_data_text: str


class tree(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[tree_props]):
        self.tagname = "ui5-tree"
        super().__init__(*args, **kwargs)


class tree_item_props(ui5_tag_props, total=False):
    additional_text: str
    additional_text_state: Literal[
        "None",
        "Success",
        "Warning",
        "Information",
        "Error",
    ]
    text: str


class tree_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[tree_item_props]):
        self.tagname = "ui5-tree-item"
        super().__init__(*args, **kwargs)
