# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class media_gallery_props(ui5_tag_props, total=False):
    show_all_thumbnails: bool
    interactive_display_area: bool
    layout: Literal["Auto", "Vertical", "Horizontal"]
    menu_horizontal_align: Literal["Left", "Right"]
    menu_vertical_align: Literal["Top", "Bottom"]


class media_gallery(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[media_gallery_props]) -> None:
        self.tagname = "ui5-media-gallery"
        super().__init__("ui5-media-gallery", *args, **kwargs)


class media_gallery_item_props(ui5_tag_props, total=False):
    disabled: bool
    layout: Literal["Square", "Wide"]
    selected: bool


class media_gallery_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[media_gallery_item_props]) -> None:
        self.tagname = "ui5-media-gallery-item"
        super().__init__("ui5-media-gallery-item", *args, **kwargs)
