# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class modal_props(ion_tag_props):
    animated: bool
    backdrop_breakpoint: int
    backdrop_dismiss: bool
    can_dismiss: bool
    handle: bool
    handle_behavior: Literal["cycle", "none"]
    initial_breakpoint: int
    is_open: bool
    keep_contents_mounted: bool
    keyboard_close: bool
    show_backdrop: bool
    trigger: str


class modal(ion_tag):
    """A Modal is a dialog that appears on top of the app's content, and must be
    dismissed by the app before interaction can resume. It is useful as a select
    component when there are a lot of options to choose from, or when filtering
    items in a list, as well as many other use cases.

    see: `https://ionicframework.com/docs/api/modal` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[modal_props]) -> None:
        self.tagname = "ion-modal"
        super().__init__(*args, **kwargs)


class backdrop_props(ion_tag_props):
    stop_propagation: bool
    tappable: bool
    visible: bool


class backdrop(ion_tag):
    """Backdrops are full screen components that overlay other components. They are
    useful behind components that transition in on top of other content and can be
    used to dismiss that component.

    see: `https://ionicframework.com/docs/api/backdrop` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[backdrop_props]) -> None:
        self.tagname = "ion-backdrop"
        super().__init__(*args, **kwargs)
