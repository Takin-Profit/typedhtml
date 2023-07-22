# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
import pytest

from typehtml.tags import typed_tag


@pytest.fixture
def get_tags() -> list[typed_tag]:
    return [
        typed_tag(
            id=str(i),
            x_bind={"placeholder": "Enter your name"},
        )
        if i % 2 == 0
        else typed_tag(id=str(i))
        for i in range(10)
    ]
