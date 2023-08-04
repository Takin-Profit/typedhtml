# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

from typing import Any, Literal, Optional, Union, Unpack

from typedhtml.attributes import a_attr
from typedhtml.globals import GLOBAL_ATTR
from typedhtml.tags import a, ul
from typedhtml.uikit.util import add_val

Icon = Literal[
    "home",
    "sign-in",
    "sign-out",
    "user",
    "users",
    "lock",
    "unlock",
    "settings",
    "cog",
    "nut",
    "comment",
    "commenting",
    "comments",
    "hashtag",
    "tag",
    "cart",
    "bag",
    "credit-card",
    "mail",
    "receiver",
    "print",
    "search",
    "location",
    "bookmark",
    "code",
    "paint-bucket",
    "camera",
    "video-camera",
    "bell",
    "microphone",
    "bolt",
    "star",
    "heart",
    "happy",
    "lifesaver",
    "rss",
    "social",
    "git-branch",
    "git-fork",
    "world",
    "calendar",
    "clock",
    "history",
    "future",
    "pencil",
    "trash",
    "move",
    "link",
    "eye",
    "eye-slash",
    "question",
    "info",
    "warning",
    "image",
    "thumbnails",
    "table",
    "list",
    "menu",
    "grid",
    "more",
    "more-vertical",
    "plus",
    "plus-circle",
    "minus",
    "minus-circle",
    "close",
    "check",
    "ban",
    "refresh",
    "play",
    "play-circle",
    "tv",
    "desktop",
    "laptop",
    "tablet",
    "phone",
    "tablet-landscape",
    "phone-landscape",
    "file",
    "file-text",
    "file-pdf",
    "copy",
    "file-edit",
    "folder",
    "album",
    "push",
    "pull",
    "server",
    "database",
    "cloud-upload",
    "cloud-download",
    "download",
    "upload",
    "reply",
    "forward",
    "expand",
    "shrink",
    "arrow-up",
    "arrow-down",
    "arrow-left",
    "arrow-right",
    "chevron-up",
    "chevron-down",
    "chevron-left",
    "chevron-right",
    "triangle-up",
    "triangle-down",
    "triangle-left",
    "triangle-right",
    "chevron-double-left",
    "chevron-double-right",
    "bold",
    "italic",
    "strikethrough",
    "quote-right",
    "500px",
    "android",
    "android-robot",
    "apple",
    "behance",
    "discord",
    "dribbble",
    "etsy",
    "facebook",
    "flickr",
    "foursquare",
    "github",
    "github-alt",
    "gitter",
    "google",
    "instagram",
    "joomla",
    "linkedin",
    "microsoft",
    "pagekit",
    "pinterest",
    "reddit",
    "soundcloud",
    "tiktok",
    "tripadvisor",
    "tumblr",
    "twitch",
    "twitter",
    "uikit",
    "vimeo",
    "whatsapp",
    "wordpress",
    "xing",
    "yelp",
    "youtube",
]


def icon(
    *args: Any,
    name: Icon,
    ratio: Optional[Union[int, float]] = None,
    is_link: bool = False,
    is_button: bool = False,
    **kwargs: Unpack[a_attr],
) -> a:
    """Place scalable vector icons anywhere in your content.

    UIkit comes with its own SVG icon system and a comprehensive library, which
    comprises a growing number of elegant outline icons. This component injects SVGs
    into the site, so that they adopt color and can be styled with CSS.

    see: `https://getuikit.com/docs/icon` for more info.
    """

    _ration = f"ratio: {str(ratio)};" if ratio else ""

    if is_link:
        add_val("cls", "uk-icon-link", kwargs)  # type: ignore

    if is_button:
        add_val("cls", "uk-icon-button", kwargs)  # type: ignore

    add_val("uk-icon", f"icon: {name}; {_ration}".strip(), kwargs)  # type: ignore

    return a(*args, **kwargs)


def icon_nav(
    *args: Any,
    is_vertical: bool = False,
    **kwargs: Unpack[GLOBAL_ATTR],
) -> ul:
    """Create a navigation consisting of icons.

    see: `https://getuikit.com/docs/iconnav` for more info.
    """
    _vert = " uk-iconnav-vertical" if is_vertical else ""
    add_val("cls", f"uk-iconnav{_vert}", kwargs)  # type: ignore
    return ul(*args, **kwargs)
