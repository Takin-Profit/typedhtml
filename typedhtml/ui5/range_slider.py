# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class range_slider_props(ui5_tag_props, total=False):
    end_value: int
    start_value: int


class range_slider(ui5_tag):
    """<ui5-range-slider> Represents a numerical interval and two handles (grips) to
    select a sub-range within it. The purpose of the component to enable visual
    selection of sub-ranges within a given interval."""

    def __init__(self, *args, **kwargs: Unpack[range_slider_props]):
        self.tagname = "ui5-range-slider"
        super().__init__(*args, **kwargs)
