# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class avatar(ion_tag):
    """Avatars are circular components that usually wrap an image or icon.
    They can be used to represent a person or an object.

    see: `https://ionicframework.com/docs/api/avatar` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-avatar"
        super().__init__(*args, **kwargs)


class img_props(ion_tag_props):
    alt: str
    src: str


class img(ion_tag):
    """Img is a tag that will lazily load an image whenever the tag is in the viewport.
    This is extremely useful when generating a large list as images are only loaded
    when they're visible. The component uses Intersection Observer internally, which
    is supported in most modern browsers, but falls back to a
    setTimeout when it is not supported.

    see: `https://ionicframework.com/docs/api/img` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[img_props]) -> None:
        self.tagname = "ion-img"
        super().__init__(*args, **kwargs)


class thumbnail(ion_tag):
    """Thumbnails are square components that usually wrap an image or icon. They can
    be used to make it easier to display a group of larger images or
    provide a preview of the full-size image.

    see: `https://ionicframework.com/docs/api/thumbnail` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-thumbnail"
        super().__init__(*args, **kwargs)
