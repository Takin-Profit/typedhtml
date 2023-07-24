# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class color_picker_props(ui5_tag_props, total=False):
    color: str


class color_picker(ui5_tag):
    """The ui5-color-picker allows users to choose any color and provides different
    input options for selecting colors."""

    def __init__(self, *args, **kwargs: Unpack[color_picker_props]):
        self.tagname = "ui5-color-picker"
        super().__init__(*args, **kwargs)
