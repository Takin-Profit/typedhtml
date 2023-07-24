# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class toast_props(ui5_tag_props, total=False):
    duration: int
    placement: Literal[
        "TopStart",
        "TopCenter",
        "TopEnd",
        "MiddleStart",
        "MiddleCenter",
        "MiddleEnd",
        "BottomStart",
        "BottomCenter",
        "BottomEnd",
    ]


class toast(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[toast_props]) -> None:
        self.tagname = "ui5-toast"
        super().__init__(*args, **kwargs)
