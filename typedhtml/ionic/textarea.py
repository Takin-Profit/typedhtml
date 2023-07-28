# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class textarea_props(ion_tag_props):
    auto_grow: bool
    autocapitalize: Literal[  # type: ignore
        "off",
        "none",
        "on",
        "sentences",
        "words",
        "characters",
    ]
    autofocus: bool
    clear_on_edit: bool
    color: Color
    cols: int
    counter: bool
    disable: bool
    enterkeyhint: Literal[
        "done",
        "enter",
        "go",
        "next",
        "previous",
        "search",
        "send",
    ]
    error_text: str
    fill: Literal["outline", "solid"]
    helper_text: str
    inputmode: Literal[
        "decimal",
        "email",
        "none",
        "numeric",
        "search",
        "tel",
        "text",
        "url",
    ]
    label: str
    label_placement: Literal["end", "fixed", "floating", "stacked", "start"]
    legacy: bool
    maxlength: int
    minLength: int
    name: str
    placeholder: str
    readonly: bool
    required: bool
    rows: int
    shape: Literal["round"]
    spellcheck: bool
    value: str
    wrap: Literal["hard", "soft", "off"]


class textarea(ion_tag):
    """The textarea component is used for multi-line text input. Unlike the
    native textarea element, the Ionic textarea does not support loading its
    value from the value attribute. In order to set the value for the
    textarea in Ionic, you can use the ionChange event of IonTextarea or
    NgModel of IonTextarea.

    see: `ion-textarea https://ionicframework.com/docs/api/textarea`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[textarea_props]) -> None:
        self.tagname = "ion-textarea"
        super().__init__(*args, **kwargs)  # type: ignore
