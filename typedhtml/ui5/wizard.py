# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class wizard_props(ui5_tag_props, total=False):
    content_layout: Literal["MultipleSteps", "SingleStep"]


class wizard(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[wizard_props]):
        self.tagname = "ui5-wizard"
        super().__init__(*args, **kwargs)


class wizard_step_props(ui5_tag_props, total=False):
    icon: str
    branching: bool
    disabled: bool
    selected: bool
    subtitle_text: str
    title_text: str


class wizard_step(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[wizard_step_props]):
        self.tagname = "ui5-wizard-step"
        super().__init__(*args, **kwargs)
