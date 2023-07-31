# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.attributes import fieldset_attr, input_attr, select_attr, textarea_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import fieldset as fs
from typedhtml.tags import input_ as inp
from typedhtml.tags import legend as leg
from typedhtml.tags import select as sel
from typedhtml.tags import textarea as ta
from typedhtml.uikit.types import FormState
from typedhtml.uikit.util import add_val

Size = Literal["small", "large"]
Width = Literal["large", "medium", "small", "xsmall"]


def input_(
    *args: Any,
    state: Optional[FormState] = None,
    size: Optional[Size] = None,
    width: Optional[Width] = None,
    is_disabled: bool = False,
    **kwargs: Unpack[input_attr],
) -> inp:
    _state = state or ""
    _width = f" uk-width-{width}" if width else ""
    _size = f" uk-form-{size}" if size else ""
    if is_disabled:
        add_val("disabled", "", kwargs)  # type: ignore
    add_val("cls", f"uk-input {_state}{_size}{_width}".strip(), kwargs)  # type: ignore

    return inp(*args, **kwargs)


def select(
    *args: Any,
    size: Optional[Size] = None,
    width: Optional[Width],
    **kwargs: Unpack[select_attr],
) -> sel:
    _width = f" uk-width-{width}" if width else ""
    _size = f" uk-form-{size}" if size else ""
    add_val("cls", f"uk-select{_size}{_width}", kwargs)  # type: ignore

    return sel(*args, **kwargs)


def textarea(
    *args: Any,
    state: Optional[FormState] = None,
    size: Optional[Size] = None,
    width: Optional[Width] = None,
    is_disabled: bool = False,
    **kwargs: Unpack[textarea_attr],
) -> ta:
    _width = f" uk-width-{width}" if width else ""
    _size = f" uk-form-{size}" if size else ""
    _state = state or ""
    if is_disabled:
        add_val("disabled", "", kwargs)  # type: ignore
    add_val("cls", f"uk-textarea {_state}{_size}{_width}".strip(), kwargs)  # type: ignore

    return ta(*args, **kwargs)


def radio(*args: Any, **kwargs: Unpack[input_attr]) -> inp:
    add_val("cls", "uk-radio", kwargs)  # type: ignore
    add_val("type", "radio", kwargs)  # type: ignore
    return inp(*args, **kwargs)


def checkbox(*args: Any, **kwargs: Unpack[input_attr]) -> inp:
    add_val("cls", "uk-checkbox", kwargs)  # type: ignore
    add_val("type", "checkbox", kwargs)  # type: ignore
    return inp(*args, **kwargs)


def range_(*args: Any, **kwargs: Unpack[input_attr]) -> inp:
    add_val("cls", "uk-range", kwargs)  # type: ignore
    add_val("type", "range", kwargs)  # type: ignore
    return inp(*args, **kwargs)


def fieldset(*args: Any, **kwargs: Unpack[fieldset_attr]) -> fs:
    add_val("cls", "uk-fieldset", kwargs)  # type: ignore
    return fs(*args, **kwargs)


def legend(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> leg:
    add_val("cls", "uk-legend", kwargs)  # type: ignore
    return leg(*args, **kwargs)
