# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typedhtml.tags import typed_tag


def makeid(x: int) -> str:
    return f'id="{x}"'


def test_x_bind_formatted_correctly(get_tags: list[typed_tag]) -> None:
    for x, tag in enumerate(get_tags):
        if x % 2 == 0:
            assert (
                tag.render()
                == f'<typed_tag {makeid(x)} x-bind:placeholder="Enter your name"></typed_tag>'  # noqa: E501
            )
        else:
            assert tag.render() == f"<typed_tag {makeid(x)}></typed_tag>"


def test_xh_on_formatted_correctly(get_hx_on_tags: list[typed_tag]) -> None:
    for x, tag in enumerate(get_hx_on_tags):
        if x % 2 == 0:
            assert (
                tag.render()
                == f"<html hx-on:click=\"alert('clicked {x}')\" {makeid(x)}></html>"  # noqa: E501
            )
        else:
            assert tag.render() == f"<html {makeid(x)}></html>"
