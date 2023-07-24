# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class table_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_name_ref: str
    busy: bool
    busy_delay: int
    growing: Literal["Button", "Scroll"]
    growing_button_subtext: str
    growing_button_text: str
    hide_no_data: bool
    hide_no_data: bool
    mode: Literal["MultiSelect", "None", "SingleSelect"]
    no_data_text: str
    sticky_column_header: bool


class table(ui5_tag):
    """The ui5-table component provides a set of sophisticated and convenient
    functions for responsive table design. It provides a comprehensive set of features
    for displaying and dealing with vast amounts of data."""

    def __init__(self, *args, **kwargs: Unpack[table_props]):
        self.tagname = "ui5-table"
        super().__init__(*args, **kwargs)


class table_column_props(ui5_tag_props, total=False):
    demand_popin: bool
    min_width: int
    popin_display: Literal["Block", "Inline"]
    popin_text: str


class table_column(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[ui5_tag_props]) -> None:
        self.tagname = "ui5-table-column"
        super().__init__(**kwargs)


class table_row_props(ui5_tag_props, total=False):
    navigated: bool
    selected: bool
    type: Literal["Active", "Inactive"]


class table_row(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[table_row_props]) -> None:
        self.tagname = "ui5-table-row"
        super().__init__(*args, **kwargs)


class table_group_row(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[ui5_tag_props]) -> None:
        self.tagname = "ui5-table-group-row"
        super().__init__(*args, **kwargs)


class table_cell(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[ui5_tag_props]) -> None:
        self.tagname = "ui5-table-cell"
        super().__init__(*args, **kwargs)
