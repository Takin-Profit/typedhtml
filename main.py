# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typedhtml import ui5 as ui
from typedhtml.document import document as doc
from typedhtml.tags import p
from typedhtml.ui5 import view_settings_dialog as vsd
from typedhtml.uikit.accordion import (
    accordion,
    accordion_content,
    accordion_item,
    accordion_title,
)

print(ui.avatar(initials="gb", color_scheme="Accent4").render())


print(ui.badge(color_scheme=1).render())


print(doc(title="Hello, world!").render())

print(vsd(accesskey="some key", autofocus=False).render())

print(ui.shell_bar(primary_title="Hello, world!", x_on={"click": "do stuff"}).render())

print(accordion(collapsible=True, multiple=True).render())


def data():
    c = accordion()
    with c:
        with accordion_item(title="Item 1"):
            with accordion_title("Some Title"):
                with accordion_content("some content"):
                    p("Hello, world!")
    return c


print(data().render())
