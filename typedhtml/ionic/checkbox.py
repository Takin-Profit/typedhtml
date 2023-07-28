# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class checkbox_props(ion_tag_props):
    checked: bool
    color: Color
    disabled: bool
    indeterminate: bool
    legacy: bool
    name: str
    value: str
    justify: Literal["end", "space-between", "start"]
    label_placement: Literal["end", "start", "fixed"]


class checkbox(ion_tag):
    """Checkboxes allow the selection of multiple options from a set of options.
    They appear as checked (ticked) when activated. Clicking on a checkbox will toggle
    the checked property.
    They can also be checked programmatically by setting the checked property.

    see: `https://ionicframework.com/docs/api/checkbox` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[checkbox_props]) -> None:
        self.tagname = "ion-checkbox"
        super().__init__(*args, **kwargs)
