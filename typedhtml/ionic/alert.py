# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Any, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class alert_props(ion_tag_props):
    animate: bool
    backdrop_dismiss: bool
    css_class: str
    header: str
    is_open: bool
    keyboard_close: bool
    message: str
    sub_header: str
    translucent: bool
    trigger: str


class alert(ion_tag):
    """An Alert is a dialog that presents users with information or
    collects information from the user using inputs. An alert appears on top of the
    app's content, and must be manually dismissed by the user before they can resume
    interaction with the app. It can also optionally have a header,
    subHeader and message.

    `see https://ionicframework.com/docs/api/alert` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[alert_props]) -> None:
        self.tagname = "ion-alert"
        super().__init__(*args, **kwargs)
