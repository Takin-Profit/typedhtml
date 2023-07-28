# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class picker_props(ion_tag_props):
    animated: bool
    backdrop_dismiss: bool
    columns: list
    css_class: str
    is_open: bool
    keyboard_close: bool
    show_backdrop: bool
    trigger: str


class picker(ion_tag):
    """A Picker is a dialog that displays a row of buttons and columns underneath.
    It appears on top of the app's content, and at the bottom of the viewport.

    see: `ion-picker <https://ionicframework.com/docs/api/picker` for more info
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[picker_props]) -> None:
        self.tagname = "ion-picker"
        super().__init__(*args, **kwargs)
