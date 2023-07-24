# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Self, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class card_props(ui5_tag_props, total=False):
    accessible_name: str
    accessible_ref: str


class card(ui5_tag):
    """The ui5-card is a container based control that consists of a header,
    content area and a footer. It can be used for grouping and displaying
    information. The content area of the card can be arbitrary HTML content.
    The card header can be used to display a title, any number of icons,
    action buttons or a menu. The card footer can be used to display additional
    information (e.g. total amount, number of items) and action buttons."""

    def __init__(self: Self, **kwargs: Unpack[card_props]) -> None:
        self.tagname = "ui5-card"
        super().__init__(**kwargs)


class card_header_props(ui5_tag_props, total=False):
    interactive: bool
    status: str
    subtitle_text: str
    title_text: str


class card_header(ui5_tag):
    """The ui5-card-header is a component, used within the ui5-card, that
    displays a title, subtitle, separators and an avatar."""

    def __init__(self: Self, *args, **kwargs: Unpack[card_header_props]) -> None:
        self.tagname = "ui5-card-header"
        super().__init__(*args, **kwargs)
