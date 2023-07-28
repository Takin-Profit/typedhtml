# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, Target, ion_tag, ion_tag_props


class button_props(ion_tag_props):
    color: Color
    disabled: bool
    download: str
    expand: Literal["block", "full"]
    fill: Literal[
        "clear",
        "default",
        "outline",
        "solid",
    ]
    form: str
    rel: str
    router_direction: Literal["back", "forward", "root"]
    shape: Literal["round"]
    size: Literal["default", "large", "small"]
    strong: bool
    target: Target
    type_: Literal["button", "reset", "submit"]


class button(ion_tag):
    """Buttons provide a clickable element, which can be used in forms, or anywhere that
    needs simple, standard button functionality. They may display text, icons, or both.

    see: `https://ionicframework.com/docs/api/button` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[button_props]) -> None:
        self.tagname = "ion-button"
        super().__init__(*args, **kwargs)
