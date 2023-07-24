# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class file_uploader_props(ui5_tag_props, total=False):
    accept: str
    disabled: bool
    hide_input: bool
    multiple: bool
    name: str
    placeholder: str
    value: str
    value_state: Literal["None", "Success", "Warning", "Error"]


class file_uploader(ui5_tag):
    """The ui5-file-uploader opens a file explorer dialog and enables users to upload
    files. The component consists of input field, but you can provide an HTML element
    by your choice to trigger the file upload, by using the default slot. Furthermore,
    you can set the property "hideInput" to "true" to hide the input field."""

    def __init__(self, *args, **kwargs: Unpack[file_uploader_props]):
        self.tagname = "ui5-file-uploader"
        super().__init__(*args, **kwargs)
