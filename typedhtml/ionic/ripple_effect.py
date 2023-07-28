# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class ripple_effect_props(ion_tag_props):
    type_: Literal["unbounded", "bounded"]


class ripple_effect(ion_tag):
    """The ripple effect component adds the Material Design ink ripple interaction
    effect. This component can only be used inside of an <ion-app> and can be
    added inside of any element.

    see: `https://ionicframework.com/docs/api/ripple-effect` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ripple_effect_props]) -> None:
        self.tagname = "ion-ripple-effect"
        super().__init__(*args, **kwargs)
