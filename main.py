# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typedhtml.document import document as doc

d = doc(title="Hello, world!")

print(d.render())
