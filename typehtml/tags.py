# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

import typing
from typing import Any, Mapping, Unpack, cast

from dominate.tags import html_tag
from dominate.tags import time_ as time_tag
from dominate.tags import title as title_tag

from .attributes import *  # noqa: F403
from .globals import GLOBAL_ATTR, extrakeys


def _get_attr(data: Any):
    if isinstance(data, dict):
        return list(cast(Mapping[str, str], data).keys())[0]
    return str(data)


def _mk_key(key: str, val: Any) -> str:
    match (key):
        case "x_bind":
            return f":{_get_attr(val)}"
        case "x_on":
            return f"@{_get_attr(val)}"
        case "x_transition":
            return f"x-transition.{'.'.join(cast(list[str], val))}"
        case "hx_on":
            return f"hx-on:{_get_attr(val)}"
        case key if key in extrakeys:
            return key.replace("_", "-")
        case _:
            return key


def _mk_val(data: Any):
    if isinstance(data, dict):
        return list(cast(Mapping[str, str], data).values())[0]
    return "" if isinstance(data, list) else data


class typed_tag(html_tag):
    """
    Creates a new typed html tag instance.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[GLOBAL_ATTR]
    ) -> None:
        fixed = {_mk_key(k, v): _mk_val(v) for k, v in kwargs.items()}

        super().__init__(*args, **fixed)


class a(typed_tag):
    """
    The a element represents a hyperlink.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[a_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class abbr(typed_tag):
    """the abbr element represents an abbreviation or acronym, optionally with its
    expansion. The title attribute may be used to provide an expansion of the
    abbreviation. If specified, the title attribute must contain an expansion of
    the abbreviation, and nothing else.
    """

    pass


class address(typed_tag):
    """
    The address element represents the contact information for its nearest
    article or body element ancestor. If that is the body element, then the
    contact information applies to the document as a whole.
    """

    pass


class html(typed_tag):
    """
    Creates a new html tag instance.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[html_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class head(typed_tag):
    """
    The head element represents a collection of metadata for the document.
    """

    pass


class title(typed_tag, title_tag):
    """
    The title element represents the document's title or name. Authors should use
    titles that identify their documents even when they are used out of context,
    for example in a user's history or bookmarks, or in search results. The
    document's title is often different from its first heading, since the first
    heading does not have to stand alone when taken out of context.
    """

    pass


class base(typed_tag):
    """
    The base element allows authors to specify the document base URL for the
    purposes of resolving relative URLs, and the name of the default browsing
    context for the purposes of following hyperlinks. The element does not
    represent any content beyond this information.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[base_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class link(typed_tag):
    """
    The link element allows authors to link their document to other resources.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[link_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class meta(typed_tag):
    """
    The meta element represents various kinds of metadata that cannot be
    expressed using the title, base, link, style, and script elements.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[meta_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class style(typed_tag):
    """The script element allows authors to include dynamic script and data"""

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[style_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_pretty = False


class noscript(typed_tag):
    """
    The noscript element represents nothing if scripting is enabled, and
    represents its children if scripting is disabled. It is used to present
    different markup to user agents that support scripting and those that don't
    support scripting, by affecting how the document is parsed.
    """

    pass


class body(typed_tag):
    """
    The body element represents the content of the document.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[body_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class main(typed_tag):
    """
    The main element represents the main content of the body of a document or
    application. The main content area consists of content that is directly
    related to or expands upon the central topic of a document or central
    functionality of an application.
    """

    pass


class section(typed_tag):
    """
    The section element represents a generic section of a document or application.
    A section, in this context, is a thematic grouping of content. Each section
    should be identified, typically by including a heading (h1-h6 element) as a
    child of the section element.
    """

    pass


class nav(typed_tag):
    """
    The nav element represents a section of a page that links to other pages or
    to parts within the page: a section with navigation links.
    """

    pass


class article(typed_tag):
    """
    The article element represents a self-contained composition in a document,
    page, application, or site, which is intended to be independently distributable
    or reusable, e.g., in syndication. This could be a forum post, a magazine or
    newspaper article, a blog entry, a user-submitted comment, an interactive
    widget or gadget, or any other independent item of content.
    """

    pass


class aside(typed_tag):
    """
    The aside element represents a portion of a document whose content is only
    indirectly related to the document's main content. Asides are frequently
    presented as sidebars or call-out boxes.
    """

    pass


class h1(typed_tag):
    """
    The h1 element represents a section heading.
    """

    pass


class h2(typed_tag):
    """
    The h2 element represents a section heading.
    """

    pass


class h3(typed_tag):
    """
    The h3 element represents a section heading.
    """

    pass


class h4(typed_tag):
    """
    The h4 element represents a section heading.
    """

    pass


class h5(typed_tag):
    """
    The h5 element represents a section heading.
    """

    pass


class h6(typed_tag):
    """
    The h6 element represents a section heading.
    """

    pass


class hgroup(typed_tag):
    """
    the hgroup element represents the heading of a section. The element is used
    """

    pass


class header(typed_tag):
    """
    The header element represents introductory content for its nearest ancestor
    sectioning content or sectioning root element. A header typically contains a
    group of introductory or navigational aids.
    """

    pass


class footer(typed_tag):
    """
    The footer element represents a footer for its nearest ancestor sectioning"""

    pass


class p(typed_tag):
    """
    The p element represents a paragraph.
    """

    pass


class hr(typed_tag):
    """
    The <hr> HTML element represents a thematic break between paragraph-level elements:
    for example, a change of scene in a story, or a shift of topic within a section.
    """

    pass


class pre(typed_tag):
    """the pre element represents a block of preformatted text, in which structure
    is represented by typographic conventions rather than by elements.
    """

    is_pretty = False


class blockquote(typed_tag):
    """
    The blockquote element represents a section that is quoted from another source.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[blockquote_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class ol(typed_tag):
    """the ol element represents a list of items, where the items have been
    intentionally ordered,
    such that changing the order would change the meaning of the document."""

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[ol_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class ul(typed_tag):
    """The ul element represents a list of items, where the order of the items is
    not important - that is, where changing the order would not materially change
    the meaning of the document."""

    pass


class li(typed_tag):
    """
    The li element represents a list item. If its parent element is an ol, or ul
    element, then the element is an item of the parent element's list, as defined
    for those elements. Otherwise, the list item has no defined list-related
    relationship to any other li element.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[li_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class dl(typed_tag):
    """
    The dl element represents an association list consisting of zero or more
    name-value groups (a description list).
    """

    pass


class dt(typed_tag):
    """
    the dt element represents the term, or name, part of a term-description group
    in a description list (dl element).

    """

    pass


class dd(typed_tag):
    """
    The dd element represents the description, definition, or value, part of a
    term-description group in a description list (dl element).
    """

    pass


class figure(typed_tag):
    """
    The figure element represents some flow content, optionally with a caption,
    that is self-contained and is typically referenced as a single unit from the
    main flow of the document.
    """

    pass


class figcaption(typed_tag):
    """
    The figcaption element represents a caption or legend for the rest of the
    contents of the figcaption element's parent figure element, if any.
    """

    pass


class div(typed_tag):
    """
    The div element has no special meaning at all. It represents its children. It
    can be used with the class, lang, and title attributes to mark up semantics
    common to a group of consecutive elements.
    """

    pass


class em(typed_tag):
    """
    The em element represents stress emphasis of its contents.
    """

    pass


class strong(typed_tag):
    """
    The strong element represents strong importance for its contents.
    """

    pass


class small(typed_tag):
    """
    The small element represents side comments such as small print.
    """

    pass


class s(typed_tag):
    """
    The s element represents contents that are no longer accurate or no longer
    relevant.
    """

    pass


class cite(html_tag):
    """
    The cite element represents the title of a work (e.g. a book, a paper, an
    essay, a poem, a score, a song, a script, a film, a TV show, a game, a
    sculpture, a painting, a theatre production, a play, an opera, a musical, an
    exhibition, a legal case report, etc). This can be a work that is being
    quoted or referenced in detail (i.e. a citation), or it can just be a work
    that is mentioned in passing.
    """

    pass


class q(html_tag):
    """
    The q element represents some phrasing content quoted from another source.
    """

    pass


class dfn(html_tag):
    """
    The dfn element represents the defining instance of a term. The paragraph,
    description list group, or section that is the nearest ancestor of the dfn
    element must also contain the definition(s) for the term given by the dfn
    element.
    """

    pass


class time_(typed_tag, time_tag):
    """
    The time element represents either a time on a 24 hour clock, or a precise
    date in the proleptic Gregorian calendar, optionally with a time and a
    time-zone offset.
    """

    def __init__(  # type: ignore
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[time_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class code(typed_tag):
    """
    The code element represents a fragment of computer code. This could be an
    XML element name, a filename, a computer program, or any other string that a
    computer would recognize.
    """

    pass


class var(typed_tag):
    """
    The var element represents a variable. This could be an actual variable in a
    mathematical expression or programming context, an identifier representing a
    constant, a function parameter, or just be a term used as a placeholder in
    prose.
    """

    pass


class samp(typed_tag):
    """
    The samp element represents (sample) output from a program or computing
    system.
    """

    pass


class kbd(typed_tag):
    """
    The kbd element represents user input (typically keyboard input, although it
    may also be used to represent other input, such as voice commands).
    """

    pass


class sub(typed_tag):
    """
    The sub element represents a subscript.
    """

    pass


class sup(typed_tag):
    """
    The sup element represents a superscript.
    """

    pass


class i(typed_tag):
    is_inline = True
    """
  The i element represents a span of text in an alternate voice or mood, or
  otherwise offset from the normal prose in a manner indicating a different
  quality of text, such as a taxonomic designation, a technical term, an
  idiomatic phrase from another language, a thought, or a ship name in Western
  texts.
  """
    pass


class b(typed_tag):
    """
    The b element represents a span of text to which attention is being drawn for
    utilitarian purposes without conveying any extra importance and with no
    implication of an alternate voice or mood, such as key words in a document
    abstract, product names in a review, actionable words in interactive
    text-driven software, or an article lede.
    """

    pass


class u(typed_tag):
    """
    The u element represents a span of text with an unarticulated, though
    explicitly rendered, non-textual annotation, such as labeling the text as
    being a proper name in Chinese text (a Chinese proper name mark), or
    labeling the text as being misspelt.
    """

    pass


class mark(typed_tag):
    """
    The mark element represents a run of text in one document marked or
    highlighted for reference purposes, due to its relevance in another context.
    When used in a quotation or other block of text referred to from the prose,
    it indicates a highlight that was not originally present but which has been
    added to bring the reader's attention to a part of the text that might not
    have been considered important by the original author when the block was
    originally written, but which is now under previously unexpected scrutiny.
    When used in the main prose of a document, it indicates a part of the
    document that has been highlighted due to its likely relevance to the user's
    current activity.
    """

    pass


class ruby(typed_tag):
    """
    The ruby element allows one or more spans of phrasing content to be marked
    with ruby annotations. Ruby annotations are short runs of text presented
    alongside base text, primarily used in East Asian typography as a guide for
    pronunciation or to include other annotations. In Japanese, this form of
    typography is also known as furigana.
    """

    pass


class rt(typed_tag):
    """
    The rt element marks the ruby text component of a ruby annotation.
    """

    pass


class rp(typed_tag):
    """
    The rp element can be used to provide parentheses around a ruby text
    component of a ruby annotation, to be shown by user agents that don't support
    ruby annotations.
    """

    pass


class bdi(typed_tag):
    """
    The bdi element represents a span of text that is to be isolated from its
    surroundings for the purposes of bidirectional text formatting.
    """

    pass


class bdo(typed_tag):
    """
    The bdo element represents explicit text directionality formatting control
    for its children. It allows authors to override the Unicode bidirectional
    algorithm by explicitly specifying a direction override.
    """

    pass


class span(typed_tag):
    """
    The span element doesn't mean anything on its own, but can be useful when
    used together with the global attributes, e.g. class, lang, or dir. It
    represents its children.
    """

    pass


class br(typed_tag):
    """
    The br element represents a line break.
    """

    is_single = True
    is_inline = True


class wbr(typed_tag):
    """
    The wbr element represents a line break opportunity.
    """

    is_single = True
    is_inline = True


class ins(typed_tag):
    """
    The ins element represents an addition to the document.
    """

    pass


class del_(typed_tag):
    """
    The del element represents a removal from the document.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[del_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class img(typed_tag):
    """
    An img element represents an image.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[img_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class iframe(typed_tag):
    """
    The iframe element represents a nested browsing context.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[iframe_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class embed(typed_tag):
    """
    The embed element represents an integration point for an external (typically
    non-HTML) application or interactive content.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[embed_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class object_(typed_tag):
    """
    The object element can represent an external resource, which, depending on
    the type of the resource, will either be treated as an image, as a nested
    browsing context, or as an external resource to be processed by a plugin.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[object_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class video(typed_tag):
    """
    A video element is used for playing videos or movies, and audio files with
    captions.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[video_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class audio(typed_tag):
    """
    An audio element represents a sound or audio stream.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[audio_attr]
    ) -> None:
        super().__init__(*args, **kwargs)


class source(typed_tag):
    """
    The source element allows authors to specify multiple alternative media
    resources for media elements. It does not represent anything on its own.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[source_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class track(typed_tag):
    """
    The track element allows authors to specify explicit external timed text
    tracks for media elements. It does not represent anything on its own.
    """

    def __init__(
        self: typing.Self, *args: tuple[Any], **kwargs: Unpack[track_attr]
    ) -> None:
        super().__init__(*args, **kwargs)

    is_single = True


class canvas(html_tag):
    """
    The canvas element provides scripts with a resolution-dependent bitmap
    canvas, which can be used for rendering graphs, game graphics, or other
    visual images on the fly.
    """

    pass


class map_(html_tag):
    """
    The map element, in conjunction with any area element descendants, defines an
    image map. The element represents its children.
    """

    pass


_map = map_
