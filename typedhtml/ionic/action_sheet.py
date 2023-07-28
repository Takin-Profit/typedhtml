# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class action_sheet_props(ion_tag_props):
    animated: bool
    backdrop_dismiss: bool
    css_class: str
    header: str
    is_open: bool
    keyboard_close: bool
    sub_header: str
    translucent: bool
    trigger: str


class action_sheet(ion_tag):
    """An Action Sheet is a dialog that displays a set of options. It appears on top of
    the app's content, and must be manually dismissed by the user before they can resume
    interaction with the app. Destructive options are made obvious in ios mode.
    There are multiple ways to dismiss the action sheet, including tapping the backdrop
    or hitting the escape key on desktop.

    `see https://ionicframework.com/docs/api/action-sheet` for more info.`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[action_sheet_props]) -> None:
        self.tagname = "ion-action-sheet"
        super().__init__(*args, **kwargs)
