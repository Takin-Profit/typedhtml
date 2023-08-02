# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import img_attr
from typedhtml.tags import img
from typedhtml.uikit.util import add_val


def svg(*args: Any, stroke_animation: bool = False, **kwargs: Unpack[img_attr]) -> img:
    """Inject inline SVG images into the page markup and style them with CSS.

    see: `https://getuikit.com/docs/svg`_
    """
    _stroke_ani = "stroke-animation: true" if stroke_animation else ""
    add_val("uk-svg", _stroke_ani, kwargs)  # type: ignore
    return img(*args, **kwargs)
