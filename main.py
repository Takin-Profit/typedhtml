# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typedhtml import ui5 as ui
from typedhtml.document import document as doc

print(ui.avatar(initials="gb", color_scheme="Accent4").render())


print(ui.badge(color_scheme=1).render())


print(doc(title="Hello, world!").render())
