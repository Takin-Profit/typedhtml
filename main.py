# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typedhtml.uikit import flex

print(
    flex(
        classes=[
            "uk-flex-center",
            "uk-flex-around@m",
            "uk-flex-between@m",
        ],
        id_="flex",
    )
)
