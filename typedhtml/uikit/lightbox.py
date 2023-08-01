# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.attributes import a_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div
from typedhtml.uikit.util import add_val


def lightbox(
    *args: Any,
    animation: Optional[str] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Create a responsive lightbox gallery with images and videos.

    see: `https://getuikit.com/docs/lightbox`_
    """
    _ani = f"animation: {animation};" if animation else ""
    add_val("uk-lightbox", _ani, kwargs)  # type: ignore
    return div(*args, **kwargs)


def lightbox_content(
    *args: Any,
    alt: Optional[str] = None,
    caption: Optional[str] = None,
    poster: Optional[str] = None,
    **kwargs: Unpack[a_attr],
) -> a:
    """"""
    if alt:
        add_val("data-alt", alt, kwargs)  # type: ignore
    if caption:
        add_val("data-caption", caption, kwargs)  # type: ignore
    if poster:
        add_val("data-poster", poster, kwargs)  # type: ignore

    return a(*args, **kwargs)
