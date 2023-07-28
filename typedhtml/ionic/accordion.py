# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class accordion_props(ion_tag_props):
    disabled: bool
    readonly: bool
    toggle_icon: str
    toggle_icon_slot: Literal["end", "start"]
    value: str


class accordion(ion_tag):
    """Accordions provide collapsible sections in your content to reduce vertical
    space while providing a way of organizing and grouping information.
    All ion-accordion components should be grouped inside
    ion-accordion-group components.

    `see https://ionicframework.com/docs/api/accordion` for more info.`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[accordion_props]) -> None:
        self.tagname = "ion-accordion"
        super().__init__(*args, **kwargs)


class accordion_group_props(ion_tag_props):
    disabled: bool
    animated: bool
    expand: Literal["compact", "inset"]
    multiple: bool
    readonly: bool
    value: str


class accordion_group(ion_tag):
    """Accordion group is a container for accordion instances.
    It manages the state of the accordions and provides keyboard navigation.

    `see: https://ionicframework.com/docs/api/accordion-group for more info`.
    """

    def __init__(
        self: Self, *args: Any, **kwargs: Unpack[accordion_group_props]
    ) -> None:
        self.tagname = "ion-accordion-group"
        super().__init__(*args, **kwargs)
