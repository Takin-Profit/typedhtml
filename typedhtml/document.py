# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Self

from dominate.document import document as doc

from typedhtml.tags import meta, typed_tag


class document(doc):
    def __init__(
        self: Self, title: str = "", doctype: str = "<!DOCTYPE html>", *a, **kw
    ) -> None:
        super().__init__(title, doctype, *a, **kw)
        self.head.add(  # type: ignore
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1"),
        )

    def get_title(self: Self) -> str:
        return super().get_title()

    def set_title(self: Self, title: str) -> None:
        super().set_title(title)

    def add(self: Self, *args: typed_tag) -> None:
        super().add(*args)

    def render(self: Self) -> str:
        return super().render()
