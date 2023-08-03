# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import video_attr
from typedhtml.tags import video as vid
from typedhtml.uikit.util import add_val


def video(
    *args: Any,
    autoplay: bool = False,
    automute: bool = False,
    **kwargs: Unpack[video_attr],
) -> vid:
    """Start playing videos as they are shown or enter the viewport.

    see: `UIKit Video <https://getuikit.com/docs/video>`
    """
    _auto = " autoplay: inview;" if autoplay else ""
    _mute = " automute: inview;" if automute else ""

    add_val("uk-video", f"{_auto}{_mute}".strip(), kwargs)  # type: ignore
    return vid(*args, **kwargs)
