# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class loading_props(ion_tag_props):
    animated: bool
    backdrop_dismiss: bool
    css_class: str
    duration: int
    enter_animation: str
    is_open: str
    keyboard_close: bool
    message: str
    spinner: str
    translucent: bool
    show_backdrop: bool
    trigger: str


class loading(ion_tag):
    """An overlay that can be used to indicate activity while blocking user
    interaction. The loading indicator appears on top of the app's content, and can be
    dismissed by the app to resume user interaction with the app. It includes an
    optional backdrop, which can be disabled by setting showBackdrop:
    false upon creation.

    see: `https://ionicframework.com/docs/api/loading`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[loading_props]) -> None:
        self.tagname = "ion-loading"
        super().__init__(*args, **kwargs)


class progress_bar_props(ion_tag_props):
    buffer: int
    color: Color
    reversed_: bool
    type_: Literal["determinate", "indeterminate"]
    value: int


class progress_bar(ion_tag):
    """Progress bars inform users about the status of ongoing processes, such as
    loading an app, submitting a form, or saving updates. There are two types of
    progress bars: determinate and indeterminate.

    see: `https://ionicframework.com/docs/api/progress-bar`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[progress_bar_props]) -> None:
        self.tagname = "ion-progress-bar"
        super().__init__(*args, **kwargs)


class skeleton_props(ion_tag_props):
    animated: bool


class skeleton_text(ion_tag):
    """Skeleton Text is a component that can be used to create placeholder loadings
    for your applications similar to Facebook cards loading.

    see: `https://ionicframework.com/docs/api/skeleton-text`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[skeleton_props]) -> None:
        self.tagname = "ion-skeleton-text"
        super().__init__(*args, **kwargs)


class spinner_props(ion_tag_props):
    color: Color
    duration: int
    name: Literal[
        "bubbles",
        "circles",
        "circular",
        "crescent",
        "dots",
        "lines",
        "lines-sharp",
        "line-sharp-small",
        "line-small",
    ]
    paused: bool


class spinner(ion_tag):
    """The Spinner component provides a variety of animated SVG spinners. Spinners
    are visual indicators that the app is loading content or performing another
    process that the user needs to wait on.

    see: `https://ionicframework.com/docs/api/spinner`
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[spinner_props]) -> None:
        self.tagname = "ion-spinner"
        super().__init__(*args, **kwargs)
