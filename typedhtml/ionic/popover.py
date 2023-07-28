# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class popover_props(ion_tag_props):
    alignment: Literal["center", "end", "start"]
    animated: bool
    arrow: bool


class popover(ion_tag):
    """A Popover is a dialog that appears on top of the current page. It can be used
    for anything, but generally it is used for overflow actions that don't fit in the
    navigation bar.

    see: `https://ionicframework.com/docs/api/popover`
    """

    def __init__(self: Self, *args, **kwargs: Unpack[popover_props]) -> None:
        self.tagname = "ion-popover"
        super().__init__(*args, **kwargs)
