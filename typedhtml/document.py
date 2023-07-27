# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Self

from dominate.document import document as doc

from typedhtml.tags import typed_tag


class document(doc):
    def __init__(
        self: Self, title: str = "", doctype: str = "<!DOCTYPE html>", *a, **kw
    ) -> None:
        super().__init__(title, doctype, *a, **kw)

    def get_title(self: Self) -> str:
        return super().get_title()

    def set_title(self: Self, title: str) -> None:
        super().set_title(title)

    def add(self: Self, *args: tuple[typed_tag]) -> None:
        super().add(*args)

    def render(self: Self) -> str:
        return super().render()
