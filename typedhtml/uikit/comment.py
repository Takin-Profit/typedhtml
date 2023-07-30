# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Unpack

from typedhtml.attributes import img_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import article, div, header, img, typed_tag, ul
from typedhtml.uikit.types import Heading
from typedhtml.uikit.util import add_val, heading


def comment(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> article:
    """The Comment component consists of the comment itself, a comment header,
    including an avatar, a title and meta text, and a comment body.

    see: `https://getuikit.com/docs/comment`_
    """

    add_val("cls", "uk-comment", kwargs)  # type: ignore
    return article(*args, **kwargs)


def comment_header(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> header:
    """The Comment component consists of the comment itself, a comment header,
    including an avatar, a title and meta text, and a comment body.

    see: `https://getuikit.com/docs/comment`_
    """

    add_val("cls", "uk-comment-header", kwargs)  # type: ignore
    return header(*args, **kwargs)


def comment_avatar(*args: Any, **kwargs: Unpack[img_attr]) -> img:
    """The Comment component consists of the comment itself, a comment header,
    including an avatar, a title and meta text, and a comment body.

    see: `https://getuikit.com/docs/comment`_
    """

    add_val("cls", "uk-comment-avatar", kwargs)  # type: ignore
    return img(*args, **kwargs)


def comment_title(
    *args: Any, heading_size: Heading, **kwargs: Unpack[GLOBAL_ATTR]
) -> typed_tag:
    """The Comment component consists of the comment itself, a comment header,
    including an avatar, a title and meta text, and a comment body.

    see: `https://getuikit.com/docs/comment`_
    """

    add_val("cls", "uk-comment-title", kwargs)  # type: ignore
    return heading(heading_size, *args, **kwargs)


def comment_meta(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> ul:
    """The Comment component consists of the comment itself, a comment header,
    including an avatar, a title and meta text, and a comment body.

    see: `https://getuikit.com/docs/comment`_
    """

    add_val("cls", "uk-comment-meta uk-subnav", kwargs)  # type: ignore
    return ul("ul", *args, **kwargs)


def comment_body(*args: Any, **kwargs: Unpack[GLOBAL_ATTR]) -> div:
    """The Comment component consists of the comment itself, a comment header,
    including an avatar, a title and meta text, and a comment body.

    see: `https://getuikit.com/docs/comment`_
    """

    add_val("cls", "uk-comment-body", kwargs)  # type: ignore
    return div("div", *args, **kwargs)
