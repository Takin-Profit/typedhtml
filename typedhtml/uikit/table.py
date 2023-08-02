# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import table as table_
from typedhtml.uikit.util import add_val


def table(
    *args: Any,
    striped: bool = False,
    divider: bool = False,
    hover: bool = False,
    justify: bool = False,
    align_center: bool = False,
    responsive: bool = True,
    size_: Optional[Literal["small", "large"]] = None,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> table_:
    """Easily create nice looking tables, which come in different styles.

    see: `https://getuikit.com/docs/table`_
    """
    _resp = " uk-table-responsive" if responsive else ""
    _align = " uk-table-middle" if align_center else ""
    _justify = " uk-table-justify" if justify else ""
    _size = f" uk-table-{size_}" if size_ else ""
    _hover = " uk-table-hover" if hover else ""
    _div = " uk-table-divider" if divider else ""
    _striped = " uk-table-striped" if striped else ""
    add_val(
        "cls",
        (f"{_div}{_striped}{_hover}" + f"{_size}{_justify}{_align}{_resp}"),
        kwargs,  # type: ignore
    )
    add_val("uk-table", "", kwargs)  # type: ignore
    return table_(*args, **kwargs)
