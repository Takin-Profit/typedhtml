# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class product_switch(ui5_tag):
    """The ui5-product-switch is an SAP Fiori specific web component that is used
    in ui5-shellbar and allows the user to easily switch between products."""


class product_switch_item_props(ui5_tag_props, total=False):
    icon: str
    subtitle_text: str
    target: Literal["_self", "_top", "_blank", "_parent", "_search"]
    target_src: str
    title_text: str


class product_switch_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[product_switch_item_props]):
        self.tagname = "ui5-product-switch-item"
        super().__init__(*args, **kwargs)
