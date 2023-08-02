# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Optional, Unpack

from typedhtml.attributes import a_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, div
from typedhtml.uikit.util import add_val


def scroll(*args: Any, **kwargs: Unpack[a_attr]) -> a:
    """Scroll smoothly when jumping to different sections on a page.

    see: `https://getuikit.com/docs/scroll`
    """
    add_val("cls", "uk-scroll", kwargs)  # type: ignore
    return a(*args, **kwargs)


def scrollspy(
    *args: Any,
    cls_: str,
    target: Optional[str] = None,
    hidden: bool = False,
    margin: Optional[str] = None,
    repeat: bool = False,
    delay: int = 0,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> div:
    """Trigger events and animations while scrolling your page."""
    _cls = f" cls: {cls_};"
    _repeat = f" repeat: {repeat};" if repeat else ""
    _target = f"target: {target};" if target else ""
    _hidden = f" hidden: {hidden};" if hidden else ""
    _margin = f" margin: {margin};" if margin else ""
    _delay = f" delay: {delay};" if delay else ""
    add_val(
        "uk-scrollspy",
        f"{_target}{_cls}{_repeat}{_hidden}" + f"{_margin}{_delay}",
        kwargs,  # type: ignore
    )
    return div(*args, **kwargs)
