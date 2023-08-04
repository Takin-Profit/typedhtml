# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import typedhtml.uikit as uk
from typedhtml.document import document as doc

d = doc(title="Hello, world!")

print(d.render())

print(
    uk.heading(
        "Username Goes Here",
        size="small",
        h_size="h4",
        cls="uk-text-center uk-margin-remove-vertical text-light",
    ).render()
)
