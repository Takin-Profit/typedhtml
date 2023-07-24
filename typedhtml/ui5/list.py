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


class list_item_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_text: str
    accessible_text_state: Literal[
        "None",
        "Success",
        "Warning",
        "Error",
        "Information",
    ]
    description: str
    icon: str
    icon_end: bool
    image: str


class li(ui5_tag):
    """The ListItem component represents the items to be displayed in the
    List."""

    def __init__(self, *args, **kwargs: Unpack[list_item_props]) -> None:
        self.tagname = "ui5-li"
        super().__init__(*args, **kwargs)


class li_groupheader_props(ui5_tag_props, total=False):
    accessible_name: str


class li_groupheader(ui5_tag):
    """The GroupHeaderListItem component is used to group list items inside a
    List."""

    def __init__(self, *args, **kwargs: Unpack[li_groupheader_props]) -> None:
        self.tagname = "ui5-li-groupheader"
        super().__init__(*args, **kwargs)


class li_custom(ui5_tag):
    """The CustomListItem component allows the usage of any HTML content as an
    item of the List."""

    def __init__(self, *args, **kwargs: Unpack[li_groupheader_props]) -> None:
        self.tagname = "ui5-li-custom"
        super().__init__(*args, **kwargs)
