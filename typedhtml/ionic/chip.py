# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class chip_props(ion_tag_props):
    color: Color
    disabled: bool
    outline: bool


class chip(ion_tag):
    """Chips represent complex entities in small blocks, such as a contact. A chip
    can contain several different elements such as avatars, text, and icons.

    see: `https://ionicframework.com/docs/api/chip` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[chip_props]) -> None:
        self.tagname = "ion-chip"
        super().__init__(*args, **kwargs)
