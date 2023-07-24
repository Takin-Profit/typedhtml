# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class switch_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_name_ref: str
    checked: bool
    design: Literal["Graphical", "Textual"]
    disabled: bool
    text_off: str
    text_on: str
    tooltip: str


class switch(ui5_tag):
    """The ui5-switch component is used for changing between binary states.
    The component can display texts, that will be switched, based on the component
    state, via the textOn and textOff properties, but texts longer than 3 letters
    will be cut off."""

    def __init__(self, *args, **kwargs: Unpack[switch_props]):
        self.tagname = "ui5-switch"
        super().__init__(*args, **kwargs)
