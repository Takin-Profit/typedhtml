# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class li_notification_item_props(ui5_tag_props, total=False):
    title_text: str
    show_close: bool
    priority: Literal["None", "Low", "Medium", "High"]
    actions: str


class li_notification(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[li_notification_item_props]) -> None:
        self.tagname = "ui5-li-notification"
        super().__init__("ui5-li-notification", *args, **kwargs)
