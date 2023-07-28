# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Any, Self, Unpack

from typing_extensions import Literal

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class input_props(ion_tag_props):
    accept: str
    autocapitalize: Literal[  #  type: ignore
        "off", "none", "on", "sentences", "words", "characters"
    ]
    autocomplete: Literal[
        "name",
        "email",
        "tel",
        "url",
        "on",
        "off",
        "honorific-prefix",
        "given-name",
        "family-name",
        "honorific-suffix",
        "nickname",
        "username",
        "new-password",
        "current-password",
        "one-time-code",
        "organization-title",
        "organization",
        "street-address",
        "address-line1",
        "address-line2",
        "address-line3",
        "address-level4",
        "address-level3",
        "address-level2",
        "address-level1",
        "country",
        "country-name",
        "postal-code",
        "cc-name",
        "cc-given-name",
        "cc-additional-name",
        "cc-family-name",
        "cc-number",
        "cc-exp",
        "cc-exp-month",
        "cc-exp-year",
        "cc-csc",
        "cc-type",
        "transaction-currency",
        "transaction-amount",
        "language",
        "bday",
        "bday-day",
        "bday-month",
        "bday-year",
        "sex",
        "tel-country-code",
        "tel-national",
        "tel-area-code",
        "tel-local",
        "tel-extension",
        "impp",
        "photo",
    ]
    autocorrect: Literal["on", "off"]
    autofocus: bool
    clear_input: bool
    clear_on_edit: bool
    color: Color
    counter: bool
    debounce: int
    disabled: bool
    enterkeyhint: Literal["enter", "done", "go", "next", "previous", "search", "send"]
    error_text: str
    fill: Literal["outline", "solid"]
    helper_text: str
    input_mode: Literal[
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
    label_placement: Literal["end", "start", "fixed", "floating", "stacked"]
    legacy: bool
    max_: str
    maxlength: int
    min_: str
    minLength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readonly: bool
    required: bool
    shape: Literal["round"]
    size: int
    spellcheck: bool
    step: str
    type_: Literal[
        "date",
        "datetime-local",
        "month",
        "time",
        "week",
        "email",
        "number",
        "password",
        "search",
        "tel",
        "text",
        "url",
    ]
    value: str


class input_(ion_tag):
    """The input component is a wrapper to the HTML input element with custom
    styling and additional functionality. It accepts most of the same
    properties as the HTML input, but works great on desktop devices and
    integrates with the keyboard on mobile devices.

    see: `ion-input https://ionicframework.com/docs/api/input`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[input_props]):
        self.tagname = "ion-input"
        super().__init__(*args, **kwargs)  # type: ignore
