# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typing_extensions import Literal

from typedhtml.ionic.base import Color, Target, ion_tag, ion_tag_props


class card_props(ion_tag_props):
    button: bool
    color: Color
    disabled: bool
    download: str
    href: str
    rel: str
    router_direction: Literal["back", "forward", "root"]
    target: Target
    type_: Literal["button", "reset", "submit"]


class card(ion_tag):
    """Cards are containers that display content such as text, images, buttons,
    and lists. A card can be a single component, but is often made up of a header,
    title, subtitle, and content. Cards are broken up into several components to
    accommodate this structure: card header, card title, card subtitle,
    and card content.

    see: `https://ionicframework.com/docs/api/card` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[card_props]) -> None:
        self.tagname = "ion-card"
        super().__init__(*args, **kwargs)


class card_content(ion_tag):
    """Card content is a child component of card that adds padding around its contents.
    It is recommended that any text content for a card should be placed
    inside of card content.

    see `https://ionicframework.com/docs/api/card-content` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-card-content"
        super().__init__(*args, **kwargs)


class card_header_props(ion_tag_props):
    color: Color
    translucent: bool


class card_header(ion_tag):
    """Card header is a child component of card that should be placed before the
    card content. It can contain a card title and a card subtitle.

    see: `https://ionicframework.com/docs/api/card-header` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[card_header_props]) -> None:
        self.tagname = "ion-card-header"
        super().__init__(*args, **kwargs)


class card_subtitle_props(ion_tag_props):
    color: Color


class card_subtitle(ion_tag):
    """Card subtitle is a child component of card that should be placed inside of a
    card header.

    see: `https://ionicframework.com/docs/api/card-subtitle` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[card_subtitle_props]) -> None:
        self.tagname = "ion-card-subtitle"
        super().__init__(*args, **kwargs)


class card_title(ion_tag):
    """Card title is a child component of card that should be placed inside of a
    card header.

    see: `https://ionicframework.com/docs/api/card-title` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[card_subtitle_props]) -> None:
        self.tagname = "ion-card-title"
        super().__init__(*args, **kwargs)
