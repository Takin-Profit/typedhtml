# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import Color, Target, ion_tag, ion_tag_props


class breadcrumb_item_props(ion_tag_props):
    active: bool
    color: Color
    disabled: bool
    download: str
    href: str
    rel: str
    router_direction: str
    separator: bool
    target: Target


class breadcrumb_item(ion_tag):
    """A Breadcrumb is a single navigation item that is a child of the Breadcrumbs
    component. A breadcrumb can link elsewhere in an app or it can be plain text.
    Each breadcrumb has a separator between it and the next breadcrumb and can
    optionally contain an icon.
    see `https://ionicframework.com/docs/api/breadcrumb` for more info.
    """

    def __init__(
        self: Self, *args: Any, **kwargs: Unpack[breadcrumb_item_props]
    ) -> None:
        self.tagname = "ion-breadcrumb-item"
        super().__init__(*args, **kwargs)


class breadcrumbs_props(ion_tag_props):
    color: Color
    items_after_collapse: int
    items_before_collapse: int
    max_items: int


class breadcrumbs(ion_tag):
    """Breadcrumbs are navigation items that are used to indicate where a user is on
    an app or site. They should be used for large sites and apps with hierarchically
    arranged pages. Breadcrumbs can be collapsed based on the maximum number that can
    show, and the collapsed indicator can be clicked on to present a popover with more
    information or expand the collapsed breadcrumbs.

    see: `https://ionicframework.com/docs/api/breadcrumbs` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[breadcrumbs_props]) -> None:
        self.tagname = "ion-breadcrumbs"
        super().__init__(*args, **kwargs)
