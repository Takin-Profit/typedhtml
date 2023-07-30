# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import iframe_attr, img_attr, video_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div, iframe, img, video
from typedhtml.uikit.util import add_val


def cover(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """Expand images, videos or iframes to cover their entire container and place
    your own content on top.
    """

    add_val("cls", "uk-cover-container", kwargs)  # type: ignore
    return div(*args, **kwargs)


def cover_img(*args: Any, **kwargs: Unpack[img_attr]) -> img:
    """Expand images, videos or iframes to cover their entire container and place
    your own content on top.
    """

    add_val("uk-cover", "", kwargs)  # type: ignore
    return img(*args, **kwargs)


def cover_vid(*args: Any, **kwargs: Unpack[video_attr]) -> video:
    """Expand images, videos or iframes to cover their entire container and place
    your own content on top.
    """

    add_val("uk-cover", "", kwargs)  # type: ignore
    return video(*args, **kwargs)


def cover_iframe(*args: Any, **kwargs: Unpack[iframe_attr]) -> iframe:
    """Expand images, videos or iframes to cover their entire container and place
    your own content on top.
    """

    add_val("uk-cover", "", kwargs)  # type: ignore
    return iframe(*args, **kwargs)
