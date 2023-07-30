# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import datetime
from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import div, span
from typedhtml.uikit.util import add_val


def countdown(*args: Any, date: datetime.date, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """The Countdown component is a simple wrapper for your site content.

    see: `https://getuikit.com/docs/countdown`_
    """
    add_val("uk-countdown", f"date: {date.isoformat()}", kwargs)  # type: ignore
    it = div(*args, **kwargs)
    with it:
        count_down()
    return it


def count_down():
    span(cls="uk-countdown-number uk-countdown-days")
    span(":", cls="uk-countdown-separator")
    span(cls="uk-countdown-number uk-countdown-hours")
    span(":", cls="uk-countdown-separator")
    span(cls="uk-countdown-number uk-countdown-minutes")
    span(":", cls="uk-countdown-separator")
    span(cls="uk-countdown-number uk-countdown-seconds")
