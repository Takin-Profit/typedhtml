# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class grid_props(ion_tag_props):
    fixed: bool


class grid(ion_tag):
    """The Grid component is a powerful mobile-first flexbox system for building custom
    layouts.

    see: `ion-grid https://ionicframework.com/docs/api/grid`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[grid_props]) -> None:
        self.tagname = "ion-grid"
        super().__init__(*args, **kwargs)  # type: ignore


class col_props(ion_tag_props):
    offset: str
    offset_lg: str
    offset_md: str
    offset_sm: str
    offset_xl: str
    offset_xs: str
    pull: str
    pull_lg: str
    pull_md: str
    pull_sm: str
    pull_xl: str
    pull_xs: str
    push: str
    push_lg: str
    push_md: str
    push_sm: str
    push_xl: str
    push_xs: str
    size: str
    size_lg: str
    size_md: str
    size_sm: str
    size_lg: str
    size_xs: str


class col(ion_tag):
    """Columns are cellular components of the grid system and go inside of a row.
    They will expand to fill the row. All content within a grid should go
    inside of a column.

    see: `ion-col https://ionicframework.com/docs/api/col`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[col_props]) -> None:
        self.tagname = "ion-col"
        super().__init__(*args, **kwargs)


class row(ion_tag):
    """Rows are horizontal components of the grid system and contain varying numbers
    of columns. They ensure the columns are positioned properly.

    see: `ion-row https://ionicframework.com/docs/api/row`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-row"
        super().__init__(*args, **kwargs)
