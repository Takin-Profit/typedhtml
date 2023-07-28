# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class list_props(ion_tag_props):
    inset: bool
    lines: Literal["full", "inset", "none"]


class list_(ion_tag):
    """Lists are made up of multiple rows of items which can contain text, buttons,
    toggles, icons, thumbnails, and much more. Lists generally contain items with
    similar data content, such as images and text.

    see: `https://ionicframework.com/docs/api/list` for more info."""

    def __init__(self: Self, *args: Any, **kwargs: Unpack[list_props]) -> None:
        self.tagname = "ion-list"
        super().__init__(*args, **kwargs)


class list_header_props(ion_tag_props):
    color: Color
    lines: Literal["full", "inset", "none"]


class list_header(ion_tag):
    """List headers are block elements that are used to describe the contents of a list.
    Unlike item dividers, list headers should only be used once at the top
    of a list of items.

    see: `https://ionicframework.com/docs/api/list-header` for more info."""

    def __init__(self: Self, *args: Any, **kwargs: Unpack[list_header_props]) -> None:
        self.tagname = "ion-list-header"
        super().__init__(*args, **kwargs)
