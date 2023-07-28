# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class icon_props(ion_tag_props):
    name: str
    size: Literal["small", "large"]
    color: Color
    aria_label: str
    aria_hidden: bool


class icon(ion_tag):
    """Icons are visual indicators usually used to describe action or intent.
    They are also used for displaying information. Ionic comes with a
    number of icons that you can use by default.

    see: `ion-icon https://ionicframework.com/docs/api/icon`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[icon_props]):
        self.tagname = "ion-icon"
        super().__init__(*args, **kwargs)
