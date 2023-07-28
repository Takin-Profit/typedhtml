# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class content_props(ion_tag_props):
    color: Color
    force_overscroll: bool
    fullscreen: bool
    scroll_events: bool
    scroll_x: bool
    scroll_y: bool


class content(ion_tag):
    """The content component provides an easy to use content area with some useful
    methods to control the scrollable area. There should only be one content
    in a single view.

    see: `https://ionicframework.com/docs/api/content` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[content_props]):
        self.tagname = "ion-content"
        super().__init__(*args, **kwargs)
