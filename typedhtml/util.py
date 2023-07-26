# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


import json
from typing import Any


def snake_to_html(snake_str: str) -> str:
    return snake_str.replace("_", "-").strip("-")


def fix_args(**kwargs) -> dict[str, Any]:
    return {snake_to_html(k): v for k, v in kwargs.items()}


def xdata(data: dict[str, Any]) -> str:
    return json.dumps(data, separators=(",", ":"))
