# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal, Unpack

from typedhtml.ui5.base import ui5_tag, ui5_tag_props


class upload_collection_props(ui5_tag_props, total=False):
    mode: Literal[
        "None",
        "SingleSelect",
        "MultiSelect",
        "SingleSelectBegin",
        "SingleSelectEnd",
        "Delete",
    ]
    accessible_name: str
    hide_drag_overlay: bool
    no_data_description: str
    no_data_text: str


class upload_collection(ui5_tag):
    """This component allows you to represent files before uploading them to a server,
    with the help of ui5-upload-collection-item. It also allows you to
    show already uploaded files."""

    def __init__(self, *args, **kwargs: Unpack[upload_collection_props]):
        self.tagname = "ui5-upload-collection"
        super().__init__(*args, **kwargs)


class upload_collection_item_props(ui5_tag_props, total=False):
    disable_delete_button: bool
    file: str
    file_name: str
    file_name_clickable: bool
    hide_delete_button: bool
    hide_retry_button: bool
    hide_terminate_button: bool
    progress: int
    upload_state: int


class upload_collection_item(ui5_tag):
    def __init__(self, *args, **kwargs: Unpack[upload_collection_item_props]):
        self.tagname = "ui5-upload-collection-item"
        super().__init__(*args, **kwargs)
