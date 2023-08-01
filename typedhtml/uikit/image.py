# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import img_attr
from typedhtml.tags import div
from typedhtml.uikit.util import add_val


def image(*args: Any, src: str, eager: bool = False, **kwargs: Unpack[img_attr]) -> div:
    """Use background images with lazy loading, responsive images and
    different image sources

    see: `https://getuikit.com/docs/image`_
    """

    _loading = "loading: eager;" if eager else ""
    add_val("uk-img", _loading, kwargs)  # type: ignore
    add_val("data-src", src, kwargs)  # type: ignore
    return div(*args, **kwargs)
