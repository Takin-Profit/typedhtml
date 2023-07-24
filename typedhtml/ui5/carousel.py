# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class carousel_props(ui5_tag_props, total=False):
    cyclic: bool
    arrows_placement: Literal["Content", "Navigation"]
    background_design: Literal["Solid", "Transparent", "Translucent"]
    hide_navigation_arrows: bool
    hide_page_indicator: bool
    items_per_page_l: int
    items_per_page_m: int
    items_per_page_s: int
    page_indicator_background_design: Literal["Solid", "Transparent", "Translucent"]
    page_indicator_border_design: Literal["Solid", "Transparent"]
    page_indicator_style: Literal["Default", "Numeric"]


class carousel(ui5_tag):
    """The Carousel allows the user to browse through a set of items. The component is
        mostly used for showing a gallery of images, but can hold any other HTMLelement.
    There are several ways to perform navigation:
    on desktop - the user can navigate using the navigation arrows or with keyboard
    shorcuts.
    on mobile - the user can use swipe gestures."""

    def __init__(self: Self, *args, **kwargs: Unpack[carousel_props]) -> None:
        self.tagname = "ui5-carousel"
        super().__init__(*args, **kwargs)
