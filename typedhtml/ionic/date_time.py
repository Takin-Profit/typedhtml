# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Self, Unpack

from typedhtml.ionic.base import Color, ion_tag, ion_tag_props


class date_time_props(ion_tag_props):
    cancel_text: str
    clear_text: str
    color: Color
    day_values: int
    disabled: bool
    done_text: str
    first_day_of_week: int
    hour_cycle: Literal["h12", "h23"]
    hour_values: str
    locale: str
    max_: str
    min_: str
    minute_values: str
    month_values: str
    multiple: bool
    name: str
    prefer_wheel: bool
    presentation: Literal[
        "date",
        "date-time",
        "month",
        "month-year",
        "time",
        "time-date",
        "year",
    ]
    readonly: bool
    show_clear_button: bool
    show_default_buttons: bool
    show_default_time_label: bool
    show_default_title: bool
    size: Literal["cover", "fixed"]
    value: str
    year_values: str


class date_time(ion_tag):
    """Datetimes present a calendar interface and time wheel, making it easy for users
    to select dates and times. Datetimes are similar to the native input elements of
    datetime-local, however, Ionic Framework's Datetime component makes it easy to
    display the date and time in the preferred format, and manage the datetime values.

    see: `ion-datetime <https://ionicframework.com/docs/api/datetime>`_
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[date_time_props]) -> None:
        self.tagname = "ion-datetime"
        super().__init__(*args, **kwargs)


class datetime_button_props(ion_tag_props):
    color: Color
    datetime_: str
    disabled: bool


class datetime_button(ion_tag):
    """Datetime Button links with a Datetime component to display the formatted date
    and time. It also provides buttons to present the datetime in a modal,
    popover, and more.

    see: `ion-datetime-button <https://ionicframework.com/docs/api/datetime-button`
    for more info.
    """

    def __init__(
        self: Self, *args: Any, **kwargs: Unpack[datetime_button_props]
    ) -> None:
        self.tagname = "ion-datetime-button"
        super().__init__(*args, **kwargs)
