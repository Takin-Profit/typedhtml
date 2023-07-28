# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, Target, ion_tag, ion_tag_props


class fab_props(ion_tag_props):
    activated: bool
    edge: bool
    horizontal: Literal["center", "end", "start"]
    vertical: Literal["bottom", "center", "top"]


class fab(ion_tag):
    """Fabs are container elements that contain one or more fab buttons. They should
    be placed in a fixed position that does not scroll with the content. Fabs should
    have one main fab button. Fabs can also contain one or more fab lists which contain
    related buttons that show when the main fab button is clicked.

    see: `ion-fab <https://ionicframework.com/docs/api/fab`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[fab_props]) -> None:
        self.tagname = "ion-fab"
        super().__init__(*args, **kwargs)


class fab_button_props(ion_tag_props):
    activated: bool
    close_icon: str
    color: Color
    disabled: bool
    download: str
    href: str
    rel: str
    router_direction: Literal["back", "forward", "root"]
    show: bool
    size: Literal["small"]
    target: Target
    translucent: bool
    type_: Literal["submit", "reset", "button"]


class fab_button(ion_tag):
    """Floating Action Buttons (FABs) represent the primary action in an application.
    By default, they have a circular shape. When pressed, the button may open more
    related actions.

    see: `ion-fab-button <https://ionicframework.com/docs/api/fab-button`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[fab_button_props]) -> None:
        self.tagname = "ion-fab-button"
        super().__init__(*args, **kwargs)


class fab_list_props(ion_tag_props):
    activated: bool
    side: Literal["start", "end", "top", "bottom"]


class fab_list(ion_tag):
    """The fab list component is a container for multiple fab buttons. It contains
    actions related to the main fab button and is flung out on click. To specify what
    side the buttons should appear on, set the side property to "start",
    "end", "top", or "bottom".

    see: `ion-fab-list https://ionicframework.com/docs/api/fab-list`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[fab_list_props]) -> None:
        self.tagname = "ion-fab-list"
        super().__init__(*args, **kwargs)
