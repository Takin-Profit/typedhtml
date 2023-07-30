# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Unpack
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import h1, h2, h3, h4, h5, h6

from typedhtml.uikit.types import Heading


def add_val(key: str, val: str, args: dict[Any, Any]) -> None:
    if key in args:
        args[key] += f" {val}"
    else:
        args[key] = val


def heading(size: Heading, *args: Any, **kwargs: Unpack[GLOBAL_ATTR]):
    match size:
        case "h1":
            return h1(*args, **kwargs)
        case "h2":
            return h2(*args, **kwargs)
        case "h3":
            return h3(*args, **kwargs)
        case "h4":
            return h4(*args, **kwargs)
        case "h5":
            return h5(*args, **kwargs)
        case "h6":
            return h6(*args, **kwargs)
