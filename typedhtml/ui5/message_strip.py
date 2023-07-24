# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class message_strip_props(ui5_tag_props, total=False):
    design: Literal["Information", "Positive", "Negative", "Warning"]
    hide_close_button: bool
    hide_icon: bool


class message_strip(ui5_tag):
    """The ui5-message-strip component enables the embedding of app-related messages.
    It displays 4 designs of messages, each with corresponding semantic color and icon:
    Information, Positive, Warning and Negative. Each message can have a Close button,
    so that it can be removed from the UI, if needed."""

    def __init__(self, *args, **kwargs: Unpack[message_strip_props]) -> None:
        self.tagname = "ui5-message-strip"
        super().__init__(*args, **kwargs)
