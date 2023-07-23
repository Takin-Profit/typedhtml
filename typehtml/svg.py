# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Any, Unpack

from dominate.svg import svg_tag
from typing_extensions import TypedDict


class core_attr(TypedDict, total=False):
    id: str
    lang: str
    tabindex: int
    xml_base: str
    xml_lang: str
    xml_space: str


class typedsvg_tag(svg_tag):
    def __init__(self, *args: tuple[Any], **kwargs: Unpack[core_attr]):
        super().__init__(*args, **kwargs)


class animate(typedsvg_tag):
    """
    The  animate SVG element is used to animate an attribute or property of an element over time.
    It's normally inserted inside the element or referenced by the href attribute of the target element.
    """

    pass


class animateMotion(svg_tag):
    """
    The <animateMotion> element causes a referenced element to move along a motion path.
    """

    pass


class animateTransform(svg_tag):
    """
    The animateTransform element animates a transformation attribute on its target element, thereby allowing
    animations to control translation, scaling, rotation, and/or skewing.
    """

    is_single = True
