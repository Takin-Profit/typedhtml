# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Literal

Width = Literal[
    "uk-width-1-1",
    "uk-width-1-2",
    "uk-width-1-3",
    "uk-width-1-4",
    "uk-width-1-5",
    "uk-width-1-6",
    "uk-width-2-3",
    "uk-width-3-4",
    "uk-width-2-5",
    "uk-width-3-5",
    "uk-width-4-5",
    "uk-width-5-6",
]

Container = Literal[
    "uk-container-small",
    "uk-container-xsmall",
    "uk-container-large",
    "uk-container-xlarge",
    "uk-container-expand",
]

Heading = Literal["h1", "h2", "h3", "h4", "h5", "h6"]
Transition = Literal["ease", "ease-in", "ease-out", "ease-in-out"]

Style = Literal["primary", "success", "warning", "danger"]
