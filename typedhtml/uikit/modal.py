# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.attributes import a_attr, button_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, button, div
from typedhtml.uikit import link
from typedhtml.uikit.button import button as btn
from typedhtml.uikit.heading import heading
from typedhtml.uikit.types import Heading, HeadingType, LinkMods, Width
from typedhtml.uikit.util import add_val

Style = Literal["default", "primary", "secondary", "danger", "text", "link"]


def modal_button(
    *args: Any,
    style_: Style = "default",
    target: str,
    size: Literal["default", "small", "large"] = "default",
    width: Optional[Width] = None,
    **kwargs: Unpack[button_attr],
) -> button:
    """see `https://getuikit.com/docs/modal`"""
    add_val("uk-toggle", f"target: #{target}", kwargs)  # type: ignore
    return btn(*args, style_=style_, size=size, width=width, **kwargs)


def modal_link(
    *args: Any,
    target: str,
    classes: list[LinkMods],
    **kwargs: Unpack[a_attr],
) -> a:
    """see `https://getuikit.com/docs/modal`"""

    add_val("href", f"#{target}", kwargs)  # type: ignore
    add_val("uk-toggle", "", kwargs)  # type: ignore
    return link(*args, classes=classes, **kwargs)  # type: ignore


ModalClasses = Literal[
    "uk-modal-container",
    "uk-modal-full",
]


def modal(
    *args: Any,
    modal_container: bool = False,
    modal_full: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """see `https://getuikit.com/docs/modal`"""
    _container = "uk-modal-container" if modal_container else ""
    _full = "uk-modal-full" if modal_full else ""
    add_val("cls", f"{_container} {_full}".strip(), kwargs)  # type: ignore
    add_val("uk-modal", "", kwargs)  # type: ignore
    return div(*args, **kwargs)


def modal_dialog(
    *args: Any,
    body: bool = True,
    overflow_auto: bool = True,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """see `https://getuikit.com/docs/modal`"""

    _body = "uk-modal-body" if body else ""
    if overflow_auto:
        add_val("uk-overflow-auto", "", kwargs)  # type: ignore
    add_val("cls", f"uk-modal-dialog {_body}".strip(), kwargs)  # type: ignore
    return div(*args, **kwargs)


Size = Literal["small", "large", "medium", "xlarge", "2xlarge"]


def modal_title(
    *args: Any,
    size: Size,
    h_size: Heading,
    divider: bool = False,
    line: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> HeadingType:
    """see `https://getuikit.com/docs/modal`"""

    add_val("cls", "uk-modal-title", kwargs)  # type: ignore
    return heading(
        *args, size=size, h_size=h_size, divider=divider, line=line, **kwargs
    )


def modal_close(
    *args: Any, outside: bool = False, **kwargs: Unpack[GLOBAL_ATTR]
) -> button:
    """see `https://getuikit.com/docs/modal`"""

    _outside = "outside" if outside else "default"
    add_val("uk-close", "", kwargs)  # type: ignore
    add_val("cls", f"uk-modal-close-{_outside}", kwargs)  # type: ignore
    add_val("type_", "button", kwargs)  # type: ignore
    return button(*args, **kwargs)


def modal_header(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """see `https://getuikit.com/docs/modal`"""

    add_val("cls", "uk-modal-header", kwargs)  # type: ignore
    return div(*args, **kwargs)


def modal_footer(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """see `https://getuikit.com/docs/modal`"""

    add_val("cls", "uk-modal-footer", kwargs)  # type: ignore
    return div(*args, **kwargs)
