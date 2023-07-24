# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class color_palette(ui5_tag):
    """The ui5-color-palette is meant for users that need to select a color from a
    predefined set. To define the colors, use the ui5-color-palette-item component
    inside the default slot of the ui5-color-palette.
    """

    def __init__(self, *args, **kwargs):
        self.tagname = "ui5-color-palette"
        super().__init__(*args, **kwargs)


class color_palette_item_props(ui5_tag_props, total=False):
    value: str


class color_palette_item(ui5_tag):
    """The ui5-color-palette-item component represents the color in
    the ui5-color-palette."""

    def __init__(self, *args, **kwargs: Unpack[color_palette_item_props]):
        self.tagname = "ui5-color-palette-item"
        super().__init__(*args, **kwargs)


class color_palette_popover_props(ui5_tag_props, total=False):
    default_color: str
    show_default_color: bool
    show_more_colors: bool
    show_recent_colors: bool


class color_palette_popover(ui5_tag):
    """Represents a predefined range of colors for easier selection.
    Overview The ColorPalettePopover provides the users with a slot to predefine colors.
    """

    def __init__(self, *args, **kwargs: Unpack[color_palette_popover_props]):
        self.tagname = "ui5-color-palette-popover"
        super().__init__(*args, **kwargs)
