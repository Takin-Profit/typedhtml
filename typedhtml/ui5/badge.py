# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class badge_props(ui5_tag_props, total=False):
    color_scheme: int
    """Defines the color scheme of the component. There are 10 predefined schemes.
    Each scheme applies different values for the background-color and border-color.
    To use one you can set a number from "1" to "10". The colorScheme"1" will be set by
    default."""


class badge(ui5_tag):
    """Small numerical value or non-numeric character, typically rendered in a
    small circle."""

    def __init__(self: Self, *args, **kwargs: Unpack[badge_props]) -> None:
        self.tagname = "ui5-badge"
        super().__init__(*args, **kwargs)
