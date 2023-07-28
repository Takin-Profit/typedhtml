# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class badge_props(ion_tag_props):
    color: Literal[
        "primary",
        "secondary",
        "tertiary",
        "success",
        "warning",
        "danger",
        "light",
        "medium",
        "dark",
    ]


class badge(ion_tag):
    """Badges are inline block elements that usually appear near another element.
    Typically they contain a number or other characters. They can be used as a
    notification that there are additional items associated with an element and
    indicate how many items there are. Badges are hidden if no content is passed in.

    see: `http://ionicframework.com/docs/api/badge` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[badge_props]) -> None:
        self.tagname = "ion-badge"
        super().__init__(*args, **kwargs)
