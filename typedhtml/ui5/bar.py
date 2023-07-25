# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class bar_props(ui5_tag_props, total=False):
    design: Literal["Header", "SubHeader", "FloatingFooter", "Footer"]


class bar(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[bar_props]) -> None:
        self.tagname = "ui5-bar"
        super().__init__("ui5-bar", *args, **kwargs)
