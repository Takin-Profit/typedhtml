# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class progress_props(ui5_tag_props, total=False):
    value: int
    disabled: bool
    display_value: bool
    hide_value: bool
    value_state: Literal["None", "Success", "Warning", "Error", "Information"]


class progress(ui5_tag):
    """<ui5-progress-indicator> Shows the progress of a process in a graphical way.
    To indicate the progress, the inside of the component is filled with a color.
    """

    def __init__(self, *args, **kwargs: Unpack[progress_props]):
        self.tagname = "ui5-progress-indicator"
        super().__init__(*args, **kwargs)
