# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class toggle_button_props(ui5_tag_props, total=False):
    pressed: bool


class toggle_button(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[toggle_button_props]):
        self.tagname = "ui5-togglebutton"
        super().__init__(*args, **kwargs)
