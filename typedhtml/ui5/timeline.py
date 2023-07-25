# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class timeline_props(ui5_tag_props, total=False):
    layout: Literal["Vertical", "Horizontal"]
    accessible_name: str


class timeline(ui5_tag):
    """The ui5-timeline component shows entries (such as objects, events, or posts)
    in chronological order. A common use case is to provide information about
    changes to an object, or events related to an object."""

    def __init__(self: Self, *args, **kwargs: Unpack[timeline_props]) -> None:
        self.tagname = "ui5-timeline"
        super().__init__(*args, **kwargs)
