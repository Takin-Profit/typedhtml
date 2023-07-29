# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typedhtml import ui5 as ui
from typedhtml.document import document as doc
from typedhtml.tags import p
from typedhtml.ui5 import view_settings_dialog as vsd
from typedhtml.uikit import alert
from typedhtml.uikit.accordion import accordion

print(ui.avatar(initials="gb", color_scheme="Accent4").render())


print(ui.badge(color_scheme=1).render())


print(doc(title="Hello, world!").render())

print(vsd(accesskey="some key", autofocus=False).render())

print(ui.shell_bar(primary_title="Hello, world!", x_on={"click": "do stuff"}).render())

print(accordion(collapsible=True, multiple=True).render())


def data():
    al = alert(animation=True, duration=0, style="danger")
    with al:
        p("Hello, world!")
    return al


print(data().render())
