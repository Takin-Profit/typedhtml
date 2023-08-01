# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Unpack

from typedhtml.attributes import ol_attr
from typedhtml.tags import ul
from typedhtml.uikit.util import add_val

ListClasses = Literal[
    "uk-list-disc",
    "uk-list-circle",
    "uk-list-square",
    "uk-list-decimal",
    "uk-list-hyphen",
    "uk-list-hyphen",
    "uk-list-emphasis",
    "uk-list-primary",
    "uk-list-secondary",
    "uk-list-divider",
    "uk-list-bullet",
    "uk-list-striped",
    "uk-list-large",
    "uk-list-collapse",
]


def list_(*args: Any, classes: list[ListClasses], **kwargs: Unpack[ol_attr]) -> ul:
    """Use the list component to create lists of items.

    see: `https://getuikit.com/docs/list`_
    """
    add_val("cls", " ".join(classes), kwargs)  # type: ignore
    return ul(*args, **kwargs)
