# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class infinite_scroll_props(ion_tag_props):
    disabled: bool
    position: Literal["bottom", "top"]
    threshold: str


class infinite_scroll(ion_tag):
    """The Infinite Scroll component calls an action to be performed when the user
    scrolls a specified distance from the bottom or top of the page.

    see: `ion-infinite-scroll https://ionicframework.com/docs/api/infinite-scroll`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[infinite_scroll_props]):
        self.tagname = "ion-infinite-scroll"
        super().__init__(*args, **kwargs)


class infinite_scroll_content_props(ion_tag_props):
    loading_spinner: Literal[
        "bubbles",
        "circles",
        "circular",
        "crescent",
        "dots",
        "lines",
        "lines-sharp",
        "lines-sharp-small",
        "lines-small",
    ]
    loading_text: str


class infinite_scroll_content(ion_tag):
    """The Infinite Scroll Content component wraps the content of the infinite scroll
    and listens for scroll events emitted by the infinite scroll's parent
    component. It can also emit loading and complete events to allow for
    programmatic control of the infinite scroll.

    see: `ion-infinite-scroll-content https://ionicframework.com/docs/api/infinite-scroll-content`
    """

    def __init__(
        self: Self, *args: Any, **kwargs: Unpack[infinite_scroll_content_props]
    ):
        self.tagname = "ion-infinite-scroll-content"
        super().__init__(*args, **kwargs)
