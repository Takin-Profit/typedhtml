# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from typing import Literal

from typedhtml.globals import GLOBAL_ATTR

__all__ = [
    "script_attr",
    "slot_attr",
    "meter_attr",
    "output_attr",
    "option_attr",
    "optgroup_attr",
    "base_attr",
    "html_attr",
    "link_attr",
    "meta_attr",
    "style_attr",
    "body_attr",
    "blockquote_attr",
    "ol_attr",
    "li_attr",
    "a_attr",
    "time_attr",
    "del_attr",
    "img_attr",
    "iframe_attr",
    "embed_attr",
    "object_attr",
    "video_attr",
    "audio_attr",
    "source_attr",
    "track_attr",
    "canvas_attr",
    "map_attr",
    "area_attr",
    "colgroup_attr",
    "td_attr",
    "th_attr",
    "form_attr",
    "fieldset_attr",
    "input_attr",
    "label_attr",
    "button_attr",
    "select_attr",
    "progress_attr",
    "data_attr",
]


class a_attr(GLOBAL_ATTR, total=False):
    download: str
    """Prompts the user to save the linked URL instead of navigating to it. Can be
    used"""
    href: str
    """The URL that the hyperlink points to. Links are not restricted to HTTP-based"""
    hreflang: str
    """Specifies the language of the linked resource. Allowed values are determined
    by"""
    ping: str
    """A space-separated list of URLs. When the link is followed, the browser will send
    POST HTTP requests with the body PING to the URLs. Typically for tracking."""
    referrerpolicy: Literal[
        "no-referrer",
        "origin",
        "unsafe-url",
        "no-referrer-when-downgrade",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
    ]
    """Specifies which referrer to send when fetching the resource.
    See Referrer-Policy."""
    rel: str
    """Specifies the relationship of the target object to the link object."""
    target: Literal["_blank", "_self", "_parent", "_top"]
    """Specifies where to display the linked URL."""
    type: str
    """Specifies the media type in the form of a MIME type for the linked URL."""


class area_attr(GLOBAL_ATTR, total=False):
    alt: str
    """
    A text string alternative to display on browsers that do not display images.
    The text should be phrased so that it presents the user with the same
    kind of choice as the image would offer when displayed without the alternative text.
    This attribute is required only if the href attribute is used.
    """
    coords: str
    """The coords attribute details the coordinates of the shape attribute in size,
    shape, and placement of an <area>."""
    download: str
    href: str
    ping: str
    referrerpolicy: Literal[
        "no-referrer",
        "origin",
        "unsafe-url",
        "no-referrer-when-downgrade",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
    ]
    """Specifies which referrer to send when fetching the resource.
    See Referrer-Policy."""
    rel: str
    """Specifies the relationship of the target object to the link object."""
    target: Literal["_blank", "_self", "_parent", "_top"]
    """Specifies where to display the linked URL."""
    shape: Literal["default", "rect", "circle", "poly"]


class base_attr(GLOBAL_ATTR, total=False):
    href: str
    """The base URL to be used throughout the document for relative URLs. Absolute
    and relative URLs are allowed.
"""
    target: Literal["_blank", "_self", "_parent", "_top"]
    """A keyword or author-defined name of the default browsing context to show the
    results of navigation from <a>, <area>, or <form>
    elements without explicit target attributes."""


class html_attr(GLOBAL_ATTR, total=False):
    """attributes for <html>"""

    manifest: str
    version: str
    xmlns: str


CrossOrigin = Literal["anonymous", "use-credentials", ""]


class link_attr(GLOBAL_ATTR, total=False):
    """attributes belong to link element"""

    as_: str
    crossorigin: CrossOrigin
    disabled: bool
    fetchpriority: Literal["auto", "high", "low", "normal"]
    href: str
    hreflang: str
    imagesizes: str
    imagesrcset: str
    integrity: str
    media: str
    prefetch: str
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
    ]
    rel: str
    sizes: str
    title: str
    type: str
    blocking: bool


class meta_attr(GLOBAL_ATTR, total=False):
    """attributes belong to meta element"""

    charset: str
    content: str
    http_equiv: Literal[
        "content-type",
        "default-style",
        "refresh",
        "x-ua-compatible",
        "content-security-policy",
    ]
    name: str
    scheme: str


class style_attr(GLOBAL_ATTR, total=False):
    """attributes belong to style element"""

    media: str
    nonce: str
    title: str


class body_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    onafterprint: str
    """Function to call after the user has printed the document."""

    onbeforeprint: str
    """Function to call when the user requests printing of the document."""

    onbeforeunload: str
    """Function to call when the document is about to be unloaded."""

    onblur: str
    """Function to call when the document loses focus."""

    onerror: str
    """Function to call when the document fails to load properly."""

    onfocus: str
    """Function to call when the document receives focus."""

    onhashchange: str
    """Function to call when the fragment identifier part (starting with the hash ('#')
    character)  of the document's current address has changed."""

    onlanguagechange: str
    """Function to call when the preferred languages changed."""

    onload: str
    """Function to call when the document has finished loading."""

    onmessage: str
    """Function to call when the document has received a message."""

    onoffline: str
    """Function to call when network communication has failed."""

    ononline: str
    """Function to call when network communication has been restored."""

    onpopstate: str
    """Function to call when the user has navigated session history."""

    onredo: str
    """Function to call when the user has moved forward in undo transaction history."""

    onresize: str
    """Function to call when the document has been resized."""

    onstorage: str
    """Function to call when the storage area has changed."""

    onundo: str
    """Function to call when the user has moved backward in undo transaction history."""

    onunload: str
    """Function to call when the document is going away."""


class blockquote_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    cite: str
    """The URL of the page that the quote came from."""


class ol_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    reversed: bool
    """Indicates whether the list should be displayed in a
    descending order instead of a ascending."""

    type: Literal["1", "a", "A", "i", "I"]
    """Sets the numbering type:

    a for lowercase letters
    A for uppercase letters
    i for lowercase Roman numerals
    I for uppercase Roman numerals
    1 for numbers (default)
    The specified type is used for the entire list unless a different
    type attribute is used on an enclosed <li> element.
    """

    start: int
    """Specifies the start value of an ordered list. Must be an integer."""


class li_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    value: int
    """Specifies the value of a list item. Must be an integer."""


class time_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    datetime: str
    """Specifies the date and time. The format must be a valid date format.
    See Date and time formats used in HTML for a list of valid formats."""


class del_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    cite: str
    """The URL of the page that the quote came from."""

    datetime: str
    """Specifies the date and time. The format must be a valid date format.
    See Date and time formats used in HTML for a list of valid formats."""


class img_attr(GLOBAL_ATTR, total=False):
    """TypedDict for handling various event properties of a document."""

    alt: str
    """Specifies an alternate text for an image, when the image cannot be displayed."""

    crossorigin: CrossOrigin
    """Specifies how the element handles cross-origin requests."""

    decoding: Literal["async", "sync", "auto"]
    """Specifies if/how the author thinks the element should be
    loaded or executed when the page loads."""

    elementtiming: str
    """Specifies that the element should be included in the element timing buffer."""

    height: str
    """Specifies the height of an element."""

    ismap: str
    """Specifies an image as a server-side image-map."""

    loading: Literal["lazy", "eager", "auto"]
    """Specifies the loading strategy of the image."""

    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
    ]
    """Specifies which referrer to send when fetching the resource.
    See Referrer-Policy."""

    sizes: str
    """Specifies the size of the linked resource."""

    src: str
    """Specifies the URL of an image."""

    srcset: str
    """Specifies the URL of the image to use in different situations."""

    usemap: str
    """Specifies an image as a client-side image-map."""

    fetchpriority: Literal["auto", "high", "low", "normal"]
    """Specifies the fetch priority of the image."""

    width: str
    """Specifies the width of an element."""


class iframe_attr(GLOBAL_ATTR, total=False):
    allow: str
    """Specifies a feature policy for the iframe."""
    allowfullscreen: str
    """Specifies whether or not to allow full screen mode."""

    allowpaymentrequest: str
    """Specifies whether or not to allow the payment request API."""

    csp: str
    """Specifies the Content Security Policy that an embedded document must
    agree to enforce upon itself."""

    height: str
    """The height of the frame in CSS pixels. Default is 150."""

    loading: Literal["lazy", "eager"]
    """Specifies the loading strategy of the iframe."""

    name: str
    """Specifies the name of an iframe."""

    referrerpolicy: Literal[
        "no-referrer",
        "origin",
        "unsafe-url",
        "no-referrer-when-downgrade",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
    ]

    sandbox: str
    """Specifies extra restrictions on the content that can appear in the iframe."""

    src: str
    """Specifies the URL of the page to embed."""

    srcdoc: str
    """Specifies the HTML content of the page to show in the iframe."""

    width: str
    """The width of the frame in CSS pixels. Default is 300."""


class embed_attr(GLOBAL_ATTR, total=False):
    height: str
    src: str
    type: str
    width: str


class object_attr(GLOBAL_ATTR, total=False):
    data: str
    form: str
    height: str
    name: str
    type: str
    usemap: str
    width: str


class video_attr(GLOBAL_ATTR, total=False):
    autoplay: bool
    buffered: str
    controls: str
    crossorigin: CrossOrigin
    height: str
    loop: str
    muted: bool
    playsinline: str
    poster: str
    src: str
    width: str
    disablepictureinpicture: str
    disableremoteplayback: str


class audio_attr(GLOBAL_ATTR, total=False):
    autoplay: bool
    buffered: str
    controls: str
    crossorigin: CrossOrigin
    loop: str
    muted: bool
    playsinline: str
    src: str
    disablepictureinpicture: str
    disableremoteplayback: str


class source_attr(GLOBAL_ATTR, total=False):
    media: str
    sizes: str
    src: str
    srcset: str
    type: str
    height: str
    width: str


class track_attr(GLOBAL_ATTR, total=False):
    default: str
    kind: Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]
    label: str
    src: str
    srclang: str


class canvas_attr(GLOBAL_ATTR, total=False):
    height: str
    width: str


class map_attr(GLOBAL_ATTR, total=False):
    name: str
    """Specifies the name of an image-map."""


class colgroup_attr(GLOBAL_ATTR, total=False):
    span: int
    """Specifies the number of columns a <col> element should span."""


class td_attr(GLOBAL_ATTR, total=False):
    colspan: int
    """Specifies the number of columns a <td> element should span."""
    headers: str
    rowspan: int


class th_attr(GLOBAL_ATTR, total=False):
    colspan: int
    """Specifies the number of columns a <td> element should span."""
    headers: str
    rowspan: int
    scope: Literal["row", "col", "rowgroup", "colgroup"]
    abbr: str


class form_attr(GLOBAL_ATTR, total=False):
    accept_charset: str
    action: str
    autocomplete: Literal["on", "off"]
    enctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    rel: str
    method: Literal["get", "post", "dialog"]
    name: str
    novalidate: bool
    target: Literal["_blank", "_self", "_parent", "_top"]


class fieldset_attr(GLOBAL_ATTR, total=False):
    disabled: bool
    form: str
    name: str


class input_attr(GLOBAL_ATTR, total=False):
    accept: str
    alt: str
    autocomplete: Literal["on", "off"]
    checked: bool
    capture: Literal["user", "environment"]
    dirname: str
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    formmethod: Literal["get", "post", "dialog"]
    formnovalidate: bool
    formtarget: Literal["_blank", "_self", "_parent", "_top"]
    height: str
    list: str
    max: str
    maxlength: int
    min: str
    minlength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readonly: bool
    required: bool
    size: int
    src: str
    step: str
    type: Literal[
        "button",
        "checkbox",
        "color",
        "date",
        "datetime-local",
        "email",
        "file",
        "hidden",
        "image",
        "month",
        "number",
        "password",
        "radio",
        "range",
        "reset",
        "search",
        "submit",
        "tel",
        "text",
        "time",
        "url",
        "week",
    ]
    value: str
    width: str


class label_attr(GLOBAL_ATTR, total=False):
    for_: str


class button_attr(GLOBAL_ATTR, total=False):
    autofocus: bool
    disabled: bool
    form: str
    formaction: str
    formenctype: Literal[
        "application/x-www-form-urlencoded", "multipart/form-data", "text/plain"
    ]
    formmethod: Literal["get", "post", "dialog"]
    formnovalidate: bool
    formtarget: Literal["_blank", "_self", "_parent", "_top"]
    name: str
    type: Literal["button", "reset", "submit"]
    value: str
    popovertarget: str
    popovertargetaction: Literal["hide", "show", "toggle"]


class select_attr(GLOBAL_ATTR, total=False):
    disabled: bool
    form: str
    multiple: bool
    name: str
    required: bool
    size: int


class optgroup_attr(GLOBAL_ATTR, total=False):
    disabled: bool
    label: str


class option_attr(GLOBAL_ATTR, total=False):
    disabled: bool
    label: str
    selected: bool
    value: str


class textarea_attr(GLOBAL_ATTR, total=False):
    autocomplete: Literal["on", "off"]
    cols: int
    dirname: str
    disabled: bool
    form: str
    maxlength: int
    minlength: int
    name: str
    placeholder: str
    readonly: bool
    required: bool
    rows: int
    wrap: Literal["hard", "soft"]


class output_attr(GLOBAL_ATTR, total=False):
    for_: str
    form: str
    name: str


class progress_attr(GLOBAL_ATTR, total=False):
    max: int
    value: int


class meter_attr(GLOBAL_ATTR, total=False):
    high: int
    low: int
    max: int
    min: int
    optimum: int
    value: int


class details_attr(GLOBAL_ATTR, total=False):
    open: bool


class data_attr(GLOBAL_ATTR, total=False):
    value: str


class slot_attr(GLOBAL_ATTR, total=False):
    name: str


class script_attr(GLOBAL_ATTR, total=False):
    async_: bool
    crossorigin: CrossOrigin
    defer: bool
    integrity: str
    nomodule: bool
    nonce: str
    fetchpriority: Literal["auto", "high", "low"]
    referrerpolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "origin",
        "origin-when-cross-origin",
        "unsafe-url",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin",
    ]
    src: str
    type: Literal[
        "module",
        "text/javascript",
        "text/ecmascript",
        "application/javascript",
        "application/ecmascript",
        "importmap",
    ]
