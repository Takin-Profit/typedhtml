# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any


def add_val(key: str, val: str, args: dict[Any, Any]) -> None:
    if key in args:
        args[key] += f" {val}"
    else:
        args[key] = val
