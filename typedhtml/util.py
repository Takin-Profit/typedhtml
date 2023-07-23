# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any


def snake_to_camel(snake_str: str) -> str:
    components = snake_str.strip("_").split(
        "_"
    )  # strip leading and trailing underscores before splitting
    return components[0] + "".join(x.title() for x in components[1:])


def fix_args(**kwargs) -> dict[str, Any]:
    return {snake_to_camel(k): v for k, v in kwargs.items()}
