# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class page_props(ui5_tag_props, total=False):
    background_design: Literal["Solid", "Transparent", "List"]
    floating_footer: bool
    disable_scrolling: bool
    hide_footer: bool


class page(ui5_tag):
    """<ui5-page> The ui5-page is a container component that holds one whole screen
    of an application. The page has three distinct areas that can hold content -
    a header, content area and a footer."""

    def __init__(self, *args, **kwargs: Unpack[page_props]) -> None:
        self.tagname = "ui5-page"
        super().__init__("ui5-page", *args, **kwargs)
