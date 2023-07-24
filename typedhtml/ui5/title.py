# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class title_props(ui5_tag_props, total=False):
    level: Literal["H1", "H2", "H3", "H4", "H5", "H6"]
    wrapping_type: Literal["None", "Normal"]


class title(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[title_props]) -> None:
        self.tagname = "ui5-title"
        super().__init__(*args, **kwargs)
