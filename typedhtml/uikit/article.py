# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Any, Unpack

from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import article as art
from typedhtml.tags import h1, p
from typedhtml.uikit.util import add_val


def article(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> art:
    """Article is a semantic element that defines an independent, self-contained
    content.

    see: `https://getuikit.com/docs/article"
    """

    add_val("cls", "uk-article", kwargs)  # type: ignore
    return art(*args, **kwargs)


def article_title(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> h1:
    """Article is a semantic element that defines an independent, self-contained
    content.

    see: `https://getuikit.com/docs/article"
    """

    add_val("cls", "uk-article-title", kwargs)  # type: ignore
    return h1(*args, **kwargs)


def article_meta(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> p:
    """Article is a semantic element that defines an independent, self-contained
    content.

    see: `https://getuikit.com/docs/article"
    """

    add_val("cls", "uk-article-meta", kwargs)  # type: ignore
    return p(*args, **kwargs)
