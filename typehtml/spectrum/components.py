# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal, Self, TypedDict, Unpack

from typehtml.tags import typed_tag


class accordion_item_args(TypedDict, total=False):
    disabled: bool
    label: str
    open: bool


class sp_accordion_item(typed_tag):
    def __init__(self: Self, **kwargs: Unpack[accordion_item_args]):
        super().__init__(**kwargs)


class sp_accordion:
    def __init__(
        self,
        allow_multiple: bool,
        density: Literal["compact", "spacious"],
        *args: tuple[sp_accordion_item],
    ) -> None:
        self._args = args

    def __str__(self) -> str:
        return (
            f"<sp-accordion>{''.join([str(arg) for arg in self._args])}</sp-accordion>"
        )
