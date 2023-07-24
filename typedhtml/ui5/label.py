# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class label_props(ui5_tag_props, total=False):
    show_colon: bool
    required: bool
    wrapping_type: Literal["None", "Normal"]
    for_: str


class label(ui5_tag):
    """The ui5-label is a component used to represent a label for elements like input,
    textarea, select."""

    def __init__(self, *args, **kwargs: Unpack[label_props]) -> None:
        self.tagname = "ui5-label"
        super().__init__(*args, **kwargs)
