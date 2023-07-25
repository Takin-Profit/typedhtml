# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class li_notification_group_props(ui5_tag_props, total=False):
    show_counter: bool
    collapsed: bool


class li_notification_group(ui5_tag):
    """The ui5-li-notification-group is a special type of list item, that unlike
    others can group items within self, usually ui5-li-notification items."""

    def __init__(self, *args, **kwargs: Unpack[li_notification_group_props]) -> None:
        self.tagname = "ui5-li-notification-group"
        super().__init__("ui5-li-notification-group", *args, **kwargs)


class notification_action_props(ui5_tag_props, total=False):
    icon: str
    type: str
    disabled: bool
    design: Literal["Default", "Emphasized", "Positive", "Negative", "Transparent"]


class notification_action(ui5_tag):
    """The ui5-notification-action is a special type of button, suitable for
    placement in the footer section of the ui5-li-notification."""

    def __init__(self, *args, **kwargs: Unpack[notification_action_props]) -> None:
        self.tagname = "ui5-notification-action"
        super().__init__("ui5-notification-action", *args, **kwargs)
