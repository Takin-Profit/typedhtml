# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from collections.abc import Mapping
from typing import Literal, TypedDict, Union

from typedhtml.events import EventName


class GLOBAL_ATTR(TypedDict, total=False):
    accesskey: str
    cls: str
    autocapitalize: Literal["off", "none", "", "sentences", "words", "characters"]
    contenteditable: Union[bool, Literal["plaintext-only"]]
    contextmenu: str
    dir: Literal["ltr", "rtl", "auto"]
    draggable: bool
    enterkeyhint: Literal["enter", "done", "go", "next", "previous", "search", "send"]
    exportparts: str
    hidden: Union[Literal["", "until-found"], str]
    id: str
    autofocus: bool
    exportparts: str
    inert: bool
    inputmode: Literal[
        "none", "text", "decimal", "numeric", "tel", "search", "email", "url"
    ]
    itemid: str
    itemprop: str
    itemref: str
    lang: str
    itemprop: str
    nonce: str
    part: str
    slot: str
    spellcheck: bool
    style: str
    tabindex: str
    title: str
    translate: Literal["yes", "no"]
    virtualkeyboardpolicy: Literal["auto", "manual"]
    hx_swap: Union[
        Literal[
            "innerHTML",
            "outerHTML",
            "beforebegin",
            "afterbegin",
            "beforeend",
            "afterend",
            "delete",
            "none",
        ],
        str,
    ]
    hx_swap_oob: Union[
        Literal[
            "true",
            "innerHTML",
            "outerHTML",
            "beforebegin",
            "afterbegin",
            "beforeend",
            "afterend",
            "delete",
            "none",
        ],
        str,
    ]
    hx_boost: Literal[True]
    """add or remove progressive enhancement for links and forms"""
    hx_on: dict[EventName, str]
    hx_get: str
    """issues a GET to the specified URL"""
    hx_post: str
    """issues a POST to the specified URL"""
    hx_put: str
    """issues a PUT to the specified URL"""
    hx_patch: str
    """issues a PATCH to the specified URL"""
    hx_delete: str
    """issues a DELETE to the specified URL"""
    hx_push_url: Union[bool, str]
    """pushes the URL into the browser location bar, creating a new history entry"""
    hx_select: str
    """select content to swap in from a response"""
    hx_select_oob: str
    """select content to swap in from a response,
    out of band (somewhere other than the target)"""
    hx_target: str
    """select the target element to swap content into """
    hx_trigger: Union[Literal["this"], str]
    """specifies the event that triggers the request"""
    hx_vals: str
    """adds values to the parameters to submit with the request (json formatted)"""
    hx_confirm: str
    """shows a confirm() dialog before making the request"""
    hx_disable: bool
    """disables htmx processing for the given node and any children nodes"""
    hx_disinherit: str
    """control and disable automatic attribute inheritance for child nodes"""
    hx_encoding: Literal["application/x-www-form-urlencoded", "multipart/form-data"]
    """changes the request encoding type"""
    hx_ext: str
    """extensions to use for this element"""
    hx_headers: str
    """adds to the headers that will be submitted with the request"""
    hx_history: bool
    """prevent sensitive data being saved to the history cache"""
    hx_history_elt: bool
    hx_include: str
    hx_indicator: str
    hx_params: Union[Literal["*", "none"], str]
    hx_preserve: bool
    hx_prompt: str
    hx_replace_url: Union[bool, str]
    hx_request: str
    hx_sse: str
    hx_sync: str
    hx_validate: str
    hx_vars: str
    hx_ws: str
    x_data: str
    x_init: str
    x_show: str
    x_bind: Mapping[str, str]
    x_on: Mapping[EventName, str]
    x_text: str
    x_html: str
    x_model: str
    x_modelable: str
    x_for: str
    # TODO: Model this correctly to match Alpine x_transition: Union[Literal[True], Optional[list[str]]]
    """Alpine.js transition directives"""
    x_effect: str
    x_ignore: Literal[True]
    """Alpine directive https://alpinejs.dev/directives/ignore"""
    x_ref: str
    x_cloak: Literal[True]
    """hides the element it's attached to until Alpine is fully loaded on the page."""
    x_teleport: str
    x_if: str
    x_id: str
    sse_connect: str
    """htmx server sent event connection url"""
    sse_swap: str
    """htmx server sent event swap target"""
    classes: str
    """htmx extension for manipulating timed addition
    and removal of classes on HTML elements"""
    mustache_template: str
    """htmx extension for rendering mustache templates"""
    handlebars_template: str
    """htmx extension for rendering handlebars templates"""
    nunjucks_template: str
    """htmx extension for rendering nunjucks templates"""
    hx_disable_element: str
    """htmx extension for disabling elements"""
    include_vals: str
    """htmx extension for including values in requests"""
    data_loading: str
    """htmx loading-states extension"""
    data_loading_class: str
    """htmx loading-states extension"""
    data_loading_class_remove: str
    """htmx loading-states extension"""
    data_loading_disable: str
    """htmx loading-states extension"""
    data_loading_aria_busy: str
    """htmx loading-states extension"""
    data_loading_delay: str
    """htmx loading-states extension"""
    data_loading_target: str
    """htmx loading-states extension"""
    data_loading_path: str
    """htmx loading-states extension"""
    data_loading_states: Literal[True]
    path_deps: str
    """htmx extension for path dependencies"""
    preload: EventName
    """htmx extension for preloading content"""
    preload_images: bool
    """htmx extension for preloading images"""
    remove_me: str
    """the remove-me htmx extension  allows you to
    remove an element after a specified interval."""
    ws_connect: str
    """htmx websocket connection url"""


extrakeys = {
    "ws_connect",
    "path_deps",
    "preload_images",
    "remove_me",
    "data_loading",
    "data_loading_class",
    "data_loading_class_remove",
    "data_loading_disable",
    "data_loading_aria_busy",
    "data_loading_delay",
    "data_loading_target",
    "data_loading_path",
    "data_loading_states",
    "include_vals",
    "hx_disable_element",
    "nunjucks_template",
    "handlebars_template",
    "hx_swap",
    "hx_swap_oob",
    "sse_connect",
    "sse_swap",
    "mustache_template",
    "htmx_boost",
    "hx_get",
    "hx_post",
    "hx_put",
    "hx_patch",
    "hx_delete",
    "hx_push_url",
    "hx_select",
    "hx_select_oob",
    "hx_target",
    "hx_trigger",
    "hx_vals",
    "hx_confirm",
    "hx_disable",
    "hx_disinherit",
    "hx_encoding",
    "hx_ext",
    "hx_headers",
    "hx_history",
    "hx_history_elt",
    "hx_include",
    "hx_indicator",
    "hx_params",
    "hx_preserve",
    "hx_prompt",
    "hx_replace_url",
    "hx_request",
    "hx_sse",
    "hx_sync",
    "hx_validate",
    "hx_vars",
    "hx_ws",
    "x_data",
    "x_init",
    "x_show",
    "x_bind",
    "x_on",
    "x_text",
    "x_html",
    "x_model",
    "x_modelable",
    "x_for",
    "x_transition",
    "x_effect",
    "x_ignore",
    "x_ref",
    "x_cloak",
    "x_teleport",
    "x_if",
    "x_id",
}
