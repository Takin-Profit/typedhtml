# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Self, Unpack

from typedhtml.ionic.base import ion_tag, ion_tag_props


class app(ion_tag):
    """App is a container element for an Ionic application. There should only be one
    <ion-app> element per project. An app can have many Ionic components including
    menus, headers, content, and footers. The overlay components get appended to the
    <ion-app> when they are presented.

    see: `https://ionicframework.com/docs/api/app` for more info.
    """

    def __init__(self: Self, *args: Any, **kwargs: Unpack[ion_tag_props]) -> None:
        self.tagname = "ion-app"
        super().__init__(*args, **kwargs)
