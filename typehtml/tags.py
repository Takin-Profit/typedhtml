# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import typing
from typing import Any, Literal, Mapping, TypedDict, Union, Unpack, cast

from dominate.tags import html_tag

from typehtml.events import EventName


class GLOBAL_ATTR(TypedDict, total=False):
    accesskey: str
    cls: str
    autocapitalize: Literal["off", "none", "", "sentences", "words", "characters"]
    contenteditable: Literal["true", "false", "plaintext-only"]
    contextmenu: str
    dir: Literal["ltr", "rtl", "auto"]
    draggable: Literal["true", "false"]
    enterkeyhint: Literal["enter", "done", "go", "next", "previous", "search", "send"]
    exportparts: str
    hidden: Union[Literal["", "until-found"], str]
    id: str
    autofocus: Literal["true", "false"]
    exportparts: str
    inert: Literal["true", "false"]
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
    spellcheck: Literal["true", "false"]
    style: str
    tabindex: str
    title: str
    translate: Literal["yes", "no"]
    virtualkeyboardpolicy: Literal["auto", "manual"]
    hx_boost: Literal["true"]
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
    hx_push_url: str
    """pushes the URL into the browser location bar, creating a new history entry"""
    hx_select: str
    """select content to swap in from a response"""
    hx_select_oob: str
    """select content to swap in from a response,
    out of band (somewhere other than the target)"""
    hx_target: str
    """select the target element to swap content into """
    hx_trigger: str
    """specifies the event that triggers the request"""
    hx_vals: str
    """adds values to the parameters to submit with the request (json formatted)"""
    hx_confirm: str
    """shows a confirm() dialog before making the request"""
    hx_disable: str
    """disables htmx processing for the given node and any children nodes"""
    hx_disinherit: str
    """control and disable automatic attribute inheritance for child nodes"""
    hx_encoding: Literal["application/x-www-form-urlencoded", "multipart/form-data"]
    """changes the request encoding type"""
    hx_ext: str
    """extensions to use for this element"""
    hx_headers: str
    """adds to the headers that will be submitted with the request"""
    hx_history: Literal["true", "false"]
    """prevent sensitive data being saved to the history cache"""
    hx_history_elt: str
    hx_include: str
    hx_indicator: str
    hx_params: str
    hx_preserve: str
    hx_prompt: str
    hx_replace_url: str
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
    x_on: str
    x_text: str
    x_html: str
    x_model: str
    x_modelable: str
    x_for: str
    x_transition: str
    x_effect: str
    x_ignore: str
    x_ref: str
    x_cloak: Literal["true", "false"]
    """hides the element it's attached to until Alpine is fully loaded on the page."""
    x_teleport: str
    x_if: str
    x_id: str


extrakeys = {
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


def _get_attr(data: Any):
    if isinstance(data, dict):
        return list(cast(Mapping[str, str], data).keys())[0]
    return str(data)


def _mk_key(key: str, val: Any) -> str:
    match (key):
        case "x_bind":
            return f"x-bind:{_get_attr(val)}"
        case "hx_on":
            return f"hx-on:{_get_attr(val)}"
        case key if key in extrakeys:
            return key.replace("_", "-")
        case _:
            return key


def _mk_val(data: Any):
    if isinstance(data, dict):
        return list(cast(Mapping[str, str], data).values())[0]
    return data


class typed_tag(html_tag):
    """
    Creates a new typed html tag instance.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[GLOBAL_ATTR]
    ) -> None:
        fixed = {_mk_key(k, v): _mk_val(v) for k, v in kwargs.items()}

        super().__init__(*args, **fixed)


class html_attr(GLOBAL_ATTR, total=False):
    manifest: str
    version: str
    xmlns: str


class html(typed_tag):
    """
    Creates a new html tag instance.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[html_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


htm = html()


class head(html_tag):
    """
    The head element represents a collection of metadata for the document.
    """

    def __init__(self) -> None:
        ...
