# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Unpack

from typedhtml.ui5.base import ui5_tag
from typedhtml.ui5.popover import popover_props


class responsive_popover(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[popover_props]):
        self.tagname = "ui5-responsive-popover"
        super().__init__(*args, **kwargs)
