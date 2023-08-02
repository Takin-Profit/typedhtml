# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import progress_attr
from typedhtml.tags import progress
from typedhtml.uikit.util import add_val


def progress(*args: Any, **kwargs: Unpack[progress_attr]) -> progress:
    """Defines progress bars that indicate how far along a process is.

    see: `https://getuikit.com/docs/progress`"""

    add_val("cls", "uk-progress", kwargs)  # type: ignore
    return progress(*args, **kwargs)
