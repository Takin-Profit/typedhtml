# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, Target, ion_tag, ion_tag_props


class item_props(ion_tag_props):
    button: bool
    color: Color
    detail: bool
    detail_icon: str
    disabled: bool
    download: str
    fill: Literal["outline", "solid"]
    href: str
    lines: Literal["full", "inset", "none"]
    rel: str
    router_direction: Literal["back", "forward", "root"]
    shape: Literal["round"]
    target: Target
    type_: Literal["button", "reset", "submit"]


class item(ion_tag):
    """Items are elements that can contain text, icons, avatars, images, inputs, and
    any other native or custom elements. Generally they are placed in a list with
    other items. Items can be swiped, deleted, reordered, edited, and more.

    see: `https://ionicframework.com/docs/api/item` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[item_props]) -> None:
        self.tagname = "ion-item"
        super().__init__(*args, **kwargs)


class item_divider_props(ion_tag_props):
    color: Color
    sticky: bool


class item_divider(ion_tag):
    """Item dividers are block elements that can be used to separate items in a list.
    They are similar to list headers, but instead of only being placed at the top of a
    list, they should go in between groups of items.

    see: `https://ionicframework.com/docs/api/item-divider` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[item_divider_props]) -> None:
        self.tagname = "ion-item-divider"
        super().__init__(*args, **kwargs)


class item_group(ion_tag):
    """Item groups are containers that organize similar items together. They can
    contain item dividers to divide the items into multiple sections. They
    can also be used to group sliding items.

    see: `https://ionicframework.com/docs/api/item-group` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-item-group"
        super().__init__(*args, **kwargs)


class item_sliding_props(ion_tag_props):
    disabled: bool


class item_sliding(ion_tag):
    """A sliding item contains an item that can be dragged to reveal option buttons.
    It requires an item component as a child.
    All options to reveal should be placed in the item options element.

    see: `https://ionicframework.com/docs/api/item-sliding` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[item_sliding_props]) -> None:
        self.tagname = "ion-item-sliding"
        super().__init__(*args, **kwargs)


class item_options_props(ion_tag_props):
    side: Literal["end", "start"]


class item_options(ion_tag):
    """The item options component is a container for the item option buttons in a
    sliding item. These buttons can be placed either on the start or end side.

    see: `https://ionicframework.com/docs/api/item-options`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[item_options_props]) -> None:
        self.tagname = "ion-item-options"
        super().__init__(*args, **kwargs)


class item_option(ion_tag):
    """The item option component is an button for a sliding item. It must be placed
    inside of item options. The ionSwipe event and the expandable property can be
    combined to create a full swipe action for the item.

    see: `https://ionicframework.com/docs/api/item-option`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-item-option"
        super().__init__(*args, **kwargs)


class label_props(ion_tag_props):
    color: Color
    position: Literal["fixed", "floating", "stacked"]


class label(ion_tag):
    """Label is a wrapper element that can be used in combination with ion-item,
    ion-input, ion-toggle, and more. The position of the label inside of an item can be
    inline, fixed, stacked, or floating.

    see: `https://ionicframework.com/docs/api/label`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[label_props]) -> None:
        self.tagname = "ion-label"
        super().__init__(*args, **kwargs)


class note(ion_tag):
    """Notes are text elements generally used as subtitles that provide more
    information. They are styled to appear grey by default.
    Notes can be used in an item as metadata text.

    see: `https://ionicframework.com/docs/api/note`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-note"
        super().__init__(*args, **kwargs)
