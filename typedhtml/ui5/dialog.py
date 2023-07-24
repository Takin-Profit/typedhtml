# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class dialog_props(ui5_tag_props, total=False):
    header_text: str
    draggable: bool
    resizable: bool
    state: Literal["None", "Information", "Success", "Warning", "Error"]
    stretch: bool


class dialog(ui5_tag):
    """The Dialog component is used to temporarily display some information
    in a simple popup."""

    def __init__(self, *args, **kwargs: Unpack[dialog_props]) -> None:
        self.tagname = "ui5-dialog"
        super().__init__(*args, **kwargs)
