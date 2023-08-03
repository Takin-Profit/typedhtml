# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.attributes import button_attr
from typedhtml.tags import button
from typedhtml.uikit.types import Animation
from typedhtml.uikit.util import add_val

Mode = Literal["click", "hover", "media", "click, hover"]


def toggle(
    *args: Any,
    target: str,
    custom_cls: Optional[str] = None,
    animations: Optional[list[Animation]] = None,
    queued: bool = False,
    mode: Optional[Mode] = None,
    media: Optional[str] = None,
    **kwargs: Unpack[button_attr],
) -> button:
    """Hide, switch or change the appearance of different contents through a toggle.

    see: `https://getuikit.com/docs/toggle`
    """
    _media = f"media: {media};" if media else ""
    _mode = f"mode: {mode};" if mode else ""
    _queued = " queued: true;" if queued else ""
    _target = f"target: {target};"
    _custom = f"cls: {custom_cls};" if custom_cls else ""
    _ani = f"animation: {','.join(animations)};" if animations else ""
    add_val(
        "uk-toggle",
        (f"{_target}{_custom}{_ani}" + f"{_target}{_mode}{_queued}{_media}"),
        kwargs,  # type: ignore
    )
    return button(*args, **kwargs)
