# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import pytest

from typedhtml.tags import html, typed_tag


@pytest.fixture
def get_tags() -> list[typed_tag]:
    return [
        typed_tag(
            id_=str(i),
            x_bind={"placeholder": "Enter your name"},
        )
        if i % 2 == 0
        else typed_tag(id_=str(i))
        for i in range(10)
    ]


@pytest.fixture
def get_hx_on_tags() -> list[typed_tag]:
    return [
        html(
            id_=str(i),
            hx_on={
                "click": f"alert('clicked {i}')",
            },
        )
        if i % 2 == 0
        else html(id_=str(i))
        for i in range(10)
    ]
