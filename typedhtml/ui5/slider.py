# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class slider_props(ui5_tag_props, total=False):
    accessible_name: str
    disabled: bool
    label_interval: int
    max_: int
    min_: int
    show_tickmarks: bool
    show_tooltip: bool
    step: int


class slider(ui5_tag):
    """<ui5-slider> allows users to input a value in a specified range."""

    def __init__(self, *args, **kwargs: Unpack[slider_props]):
        self.tagname = "ui5-slider"
        super().__init__(*args, **kwargs)
