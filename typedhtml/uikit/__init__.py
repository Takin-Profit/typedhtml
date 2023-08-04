# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from .accordion import accordion, accordion_content, accordion_item, accordion_title
from .alert import alert
from .article import article, article_title
from .badge import badge
from .button import button, button_group
from .card import card, card_title
from .comment import (
    comment,
    comment_avatar,
    comment_body,
    comment_header,
    comment_meta,
    comment_title,
)
from .container import container
from .countdown import countdown
from .cover import cover
from .description_list import description_list
from .divider import divider
from .dotnav import dotnav
from .drop import drop, drop_bar, dropdown
from .flex import flex
from .form import checkbox, fieldset, input_, legend, radio, range_, select, textarea
from .heading import heading
from .height import height
from .icon import icon, icon_nav
from .image import image
from .label import label
from .lightbox import lightbox, lightbox_content
from .link import link
from .list_ import list_
from .marker import marker
from .modal import (
    modal,
    modal_button,
    modal_close,
    modal_dialog,
    modal_footer,
    modal_header,
    modal_link,
    modal_title,
)
from .nav import (
    nav,
    nav_item,
    navbar,
    navbar_align,
    navbar_item,
    navbar_subtitle,
    navbar_toggle,
    navigation,
)
from .offcanvas import offcanvas
from .overlay import overlay, overlay_icon
from .pagination import pagination
from .placeholder import placeholder
from .progress import progress
from .scroll import scroll, scrollspy
from .search import search
from .section import section
from .slidenav import slidenav, slidenav_container
from .sortable import sortable
from .spinner import spinner
from .sticky import sticky
from .subnav import subnav
from .svg import svg
from .tab import tab
from .table import table
from .thumbnav import thumbnav
from .tile import tile
from .toggle import toggle
from .tooltip import tooltip
from .totop import totop
from .video import video

__all__ = [
    "heading",
    "hidden",
    "invisible",
    "hidden_s",
    "hidden_m",
    "hidden_l",
    "hidden_xl",
    "visible_s",
    "visible_m",
    "visible_l",
    "visible_xl",
    "hidden_hover",
    "hidden_invisible_hover",
    "hidden_touch",
    "hidden_notouch",
    "video",
    "transition_fade",
    "transition_scale_up",
    "transition_scale_down",
    "transition_slide_top",
    "transition_slide_bottom",
    "transition_slide_left",
    "transition_slide_right",
    "transition_slide_top_small",
    "transition_slide_bottom_small",
    "transition_slide_left_small",
    "transition_slide_right_small",
    "transition_slide_top_medium",
    "transition_slide_bottom_medium",
    "transition_slide_left_medium",
    "transition_slide_right_medium",
    "totop",
    "tooltip",
    "toggle",
    "tile",
    "thumbnav",
    "text_lead",
    "text_default",
    "text_large",
    "text_light",
    "text_normal",
    "text_bold",
    "text_lighter",
    "text_bolder",
    "text_italic",
    "text_capitalize",
    "text_uppercase",
    "text_lowercase",
    "text_decoration_none",
    "text_muted",
    "text_emphasis",
    "text_primary",
    "text_secondary",
    "text_success",
    "text_warning",
    "text_danger",
    "text_background",
    "text_left",
    "text_right",
    "text_center",
    "text_justify",
    "text_left_s",
    "text_center_s",
    "text_right_s",
    "text_left_m",
    "text_center_m",
    "text_right_m",
    "text_left_l",
    "text_center_l",
    "text_right_l",
    "text_left_xl",
    "text_center_xl",
    "text_right_xl",
    "text_top",
    "text_middle",
    "text_bottom",
    "text_baseline",
    "text_truncate",
    "text_break",
    "text_nowrap",
    "table",
    "tab",
    "svg",
    "subnav",
    "sticky",
    "spinner",
    "sortable",
    "uk_width_1_1_m",
    "uk_width_1_2_m",
    "uk_width_1_3_m",
    "uk_width_2_3_m",
    "uk_width_1_4_m",
    "uk_width_3_4_m",
    "uk_width_1_5_m",
    "uk_width_2_5_m",
    "uk_width_3_5_m",
    "uk_width_4_5_m",
    "uk_width_1_6_m",
    "uk_width_5_6_m",
    "uk_width_auto_m",
    "uk_width_expand_m",
    "uk_width_1_1_s",
    "uk_width_1_2_s",
    "uk_width_1_3_s",
    "uk_width_2_3_s",
    "uk_width_1_4_s",
    "uk_width_3_4_s",
    "uk_width_1_5_s",
    "uk_width_2_5_s",
    "uk_width_3_5_s",
    "uk_width_4_5_s",
    "uk_width_1_6_s",
    "uk_width_5_6_s",
    "uk_width_auto_s",
    "uk_width_expand_s",
    "uk_width_1_1_l",
    "uk_width_1_2_l",
    "uk_width_1_3_l",
    "uk_width_2_3_l",
    "uk_width_1_4_l",
    "uk_width_3_4_l",
    "uk_width_1_5_l",
    "uk_width_2_5_l",
    "uk_width_3_5_l",
    "uk_width_4_5_l",
    "uk_width_1_6_l",
    "uk_width_5_6_l",
    "uk_width_auto_l",
    "uk_width_expand_l",
    "uk_width_1_1_xl",
    "uk_width_1_2_xl",
    "uk_width_1_3_xl",
    "uk_width_2_3_xl",
    "uk_width_1_4_xl",
    "uk_width_3_4_xl",
    "uk_width_1_5_xl",
    "uk_width_2_5_xl",
    "uk_width_3_5_xl",
    "uk_width_4_5_xl",
    "uk_width_1_6_xl",
    "uk_width_5_6_xl",
    "uk_width_auto_xl",
    "uk_width_expand_xl",
    "width_small",
    "width_medium",
    "width_large",
    "width_xlarge",
    "width_2xlarge",
    "child_width_1_2",
    "child_width_1_3",
    "child_width_1_4",
    "child_width_1_5",
    "child_width_1_6",
    "child_width_auto",
    "child_width_expand",
    "width_auto",
    "width_expand",
    "width_1_1",
    "width_1_2",
    "width_1_3",
    "width_2_3",
    "width_1_4",
    "width_3_4",
    "width_1_5",
    "width_2_5",
    "width_3_5",
    "width_4_5",
    "width_1_6",
    "width_5_6",
    "slidenav_container",
    "slidenav",
    "section",
    "search",
    "scrollspy",
    "scroll",
    "disabled",
    "drag",
    "transform_origin_top_left",
    "transform_origin_top_center",
    "transform_origin_top_right",
    "transform_origin_center_left",
    "transform_origin_center_right",
    "transform_origin_bottom_left",
    "transform_origin_bottom_center",
    "transform_origin_bottom_right",
    "transform_center",
    "blend_multiply",
    "blend_screen",
    "blend_overlay",
    "blend_darken",
    "blend_lighten",
    "blend_color_dodge",
    "blend_color_burn",
    "blend_hard_light",
    "blend_soft_light",
    "blend_difference",
    "blend_exclusion",
    "blend_hue",
    "blend_saturation",
    "blend_color",
    "blend_luminosity",
    "logo",
    "dropcap",
    "box_shadow_hover_small",
    "box_shadow_hover_medium",
    "box_shadow_hover_large",
    "box_shadow_hover_xlarge",
    "box_shadow_bottom",
    "box_shadow_small",
    "box_shadow_medium",
    "box_shadow_large",
    "box_shadow_xlarge",
    "border_pill",
    "border_circle",
    "border_rounded",
    "object_position_top_left",
    "object_position_top_center",
    "object_position_top_right",
    "object_position_center_left",
    "object_position_center_center",
    "object_position_center_right",
    "object_position_bottom_left",
    "object_position_bottom_center",
    "object_position_bottom_right",
    "object_cover",
    "object_contain",
    "object_fill",
    "object_none",
    "object_scale_down",
    "responsive_width",
    "responsive_height",
    "preserve_width",
    "inline",
    "inline_clip",
    "display_block",
    "display_inline",
    "display_inline_block",
    "resize",
    "resize_vertical",
    "overflow_auto",
    "overflow_hidden",
    "float_left",
    "float_right",
    "clearfix",
    "progress",
    "placeholder",
    "pagination",
    "padding",
    "padding_small",
    "padding_large",
    "padding_remove",
    "padding_remove_top",
    "padding_remove_bottom",
    "padding_remove_left",
    "padding_remove_right",
    "padding_remove_vertical",
    "padding_remove_horizontal",
    "overlay_icon",
    "overlay",
    "offcanvas",
    "navbar_subtitle",
    "navbar_toggle",
    "navbar_item",
    "navigation",
    "navbar_align",
    "navbar",
    "nav",
    "nav_item",
    "modal",
    "modal_button",
    "modal_link",
    "modal_dialog",
    "modal_title",
    "modal_close",
    "modal_footer",
    "modal_header",
    "marker",
    "margin_auto_left_s",
    "margin_auto_s",
    "margin_auto_right_s",
    "margin_auto_left_m",
    "margin_auto_m",
    "margin_auto_right_m",
    "margin_auto_left_l",
    "margin_auto_l",
    "margin_auto_right_l",
    "margin_auto_left_xl",
    "margin_auto_xl",
    "margin_auto_right_xl",
    "margin_auto",
    "margin_auto_top",
    "margin_auto_bottom",
    "margin_auto_left",
    "margin_auto_right",
    "margin_auto_vertical",
    "margin_remove_left_s",
    "margin_remove_right_s",
    "margin_remove_left_m",
    "margin_remove_right_m",
    "margin_remove_left_l",
    "margin_remove_right_l",
    "margin_remove_left_xl",
    "margin_remove_right_xl",
    "margin_remove",
    "margin_remove_top",
    "margin_remove_bottom",
    "margin_remove_left",
    "margin_remove_right",
    "margin_remove_vertical",
    "margin_remove_adjacent",
    "margin_remove_first_child",
    "margin_remove_last_child",
    "margin_xlarge",
    "margin_xlarge_top",
    "margin_xlarge_bottom",
    "margin_xlarge_left",
    "margin_xlarge_right",
    "margin_large",
    "margin_large_top",
    "margin_large_bottom",
    "margin_large_left",
    "margin_large_right",
    "margin_medium",
    "margin_medium_top",
    "margin_medium_bottom",
    "margin_medium_left",
    "margin_medium_right",
    "margin_small",
    "margin_small_top",
    "margin_small_bottom",
    "margin_small_left",
    "margin_small_right",
    "margin",
    "margin_top",
    "margin_bottom",
    "margin_left",
    "margin_right",
    "list_",
    "list_large",
    "list_collapse",
    "list_bullet",
    "list_divider",
    "list_muted",
    "list_emphasis",
    "list_primary",
    "list_secondary",
    "list_disc",
    "list_circle",
    "list_square",
    "list_decimal",
    "list_hyphen",
    "link",
    "link_muted",
    "link_text",
    "link_heading",
    "link_reset",
    "link_toggle",
    "lightbox_content",
    "lightbox",
    "label",
    "image",
    "icon_nav",
    "icon",
    "height",
    "height_1_1",
    "height_small",
    "height_max_small",
    "height_medium",
    "height_max_medium",
    "height_large",
    "height_max_large",
    "grid_column_small",
    "grid_row_small",
    "grid_column_medium",
    "grid_row_medium",
    "grid_column_large",
    "grid_row_large",
    "grid_column_collapse",
    "grid_row_collapse",
    "grid_collapse",
    "grid_large",
    "grid_medium",
    "grid_small",
    "range_",
    "fieldset",
    "legend",
    "radio",
    "checkbox",
    "input_",
    "select",
    "textarea",
    "flex",
    "flex_none",
    "flex_auto",
    "flex_1",
    "flex_first",
    "flex_last",
    "flex_first_s",
    "flex_last_s",
    "flex_first_m",
    "flex_last_m",
    "flex_first_l",
    "flex_last_l",
    "flex_first_xl",
    "flex_last_xl",
    "flex_wrap_stretch",
    "flex_wrap_between",
    "flex_wrap_around",
    "flex_wrap_top",
    "flex_wrap_middle",
    "flex_wrap_bottom",
    "flex_wrap",
    "flex_wrap_reverse",
    "flex_nowrap",
    "flex_row",
    "flex_row_reverse",
    "flex_column",
    "flex_column_reverse",
    "flex_middle",
    "flex_bottom",
    "flex_top",
    "flex_stretch",
    "flex_left_s",
    "flex_center_s",
    "flex_right_s",
    "flex_between_s",
    "flex_around_s",
    "flex_left_m",
    "flex_center_m",
    "flex_right_m",
    "flex_between_m",
    "flex_around_m",
    "flex_left_l",
    "flex_center_l",
    "flex_right_l",
    "flex_between_l",
    "flex_around_l",
    "flex_left_xl",
    "flex_center_xl",
    "flex_right_xl",
    "flex_between_xl",
    "flex_around_xl",
    "flex_align_around",
    "flex_align_between",
    "flex_align_center",
    "flex_align_right",
    "flex_align_left",
    "drop",
    "drop_bar",
    "dropdown",
    "dotnav",
    "divider",
    "description_list",
    "countdown",
    "cover",
    "position_top",
    "position_left",
    "position_right",
    "position_bottom",
    "position_top_left",
    "position_top_center",
    "position_top_right",
    "position_center",
    "position_center_left",
    "position_center_right",
    "position_bottom_left",
    "position_bottom_center",
    "position_bottom_right",
    "position_cover",
    "position_center_left_out",
    "position_center_right_out",
    "position_small",
    "position_medium",
    "position_large",
    "position_relative",
    "position_absolute",
    "position_fixed",
    "position_z_index",
    "container",
    "container_expand",
    "container_small",
    "container_xsmall",
    "container_xlarge",
    "container_large",
    "comment",
    "comment_header",
    "comment_avatar",
    "comment_title",
    "comment_meta",
    "comment_body",
    "column_1_2_s",
    "column_1_3_s",
    "column_1_4_s",
    "column_1_5_s",
    "column_1_6_s",
    "column_1_2_m",
    "column_1_3_m",
    "column_1_4_m",
    "column_1_5_m",
    "column_1_6_m",
    "column_1_2_l",
    "column_1_3_l",
    "column_1_4_l",
    "column_1_5_l",
    "column_1_6_l",
    "column_1_2_xl",
    "column_1_3_xl",
    "column_1_4_xl",
    "column_1_5_xl",
    "column_1_6_xl",
    "column_1_2",
    "column_1_3",
    "column_1_4",
    "column_1_5",
    "column_1_6",
    "card",
    "card_title",
    "button",
    "button_group",
    "width_1_1",
    "width_1_2",
    "width_1_3",
    "width_1_4",
    "width_1_5",
    "width_1_6",
    "width_2_3",
    "width_3_4",
    "width_2_5",
    "width_3_5",
    "width_4_5",
    "width_5_6",
    "badge",
    "background_blend_multiply",
    "background_blend_screen",
    "background_blend_overlay",
    "background_blend_darken",
    "background_blend_lighten",
    "background_blend_color_dodge",
    "background_blend_color_burn",
    "background_blend_hard_light",
    "background_blend_soft_light",
    "background_blend_difference",
    "background_blend_exclusion",
    "background_blend_hue",
    "background_blend_saturation",
    "background_blend_color",
    "background_blend_luminosity",
    "background_image_xl",
    "background_image_l",
    "background_image_m",
    "background_image_s",
    "background_no_repeat",
    "background_bottom_right",
    "background_bottom_center",
    "background_bottom_left",
    "background_center_right",
    "background_center_center",
    "background_center_left",
    "background_top_center",
    "_background_top_right",
    "background_top_left",
    "background_height_1_1",
    "background_width_1_1",
    "background_contain",
    "background_cover",
    "background_secondary",
    "background_primary",
    "background_muted",
    "background_default",
    "animation_fast",
    "animation_reverse",
    "animation_stroke",
    "animation_shake",
    "animation_kenburns",
    "animation_slide_right_small",
    "animation_slide_left_small",
    "animation_slide_bottom_small",
    "animation_slide_top_small",
    "animation_scale_up",
    "animation_scale_down",
    "animation_slide_top",
    "animation_slide_bottom",
    "animation_slide_left",
    "animation_fade",
    "animation_slide_right",
    "align_center",
    "align_right",
    "align_left",
    "article_title",
    "article",
    "alert",
    "accordion",
    "accordion_item",
    "accordion_title",
    "accordion_content",
]

align_left = "uk-align-left"
align_right = "uk-align-right"
align_center = "uk-align-center"
animation_fade = "uk-animation-fade"
animation_scale_up = "uk-animation-scale-up"
animation_scale_down = "uk-animation-scale-down"
animation_slide_top = "uk-animation-slide-top"
animation_slide_bottom = "uk-animation-slide-bottom"
animation_slide_left = "uk-animation-slide-left"
animation_slide_right = "uk-animation-slide-right"
animation_slide_top_small = "uk-animation-slide-top-small"
animation_slide_bottom_small = "uk-animation-slide-bottom-small"
animation_slide_left_small = "uk-animation-slide-left-small"
animation_slide_right_small = "uk-animation-slide-right-small"
animation_kenburns = "uk-animation-kenburns"
animation_shake = "uk-animation-shake"
animation_stroke = "uk-animation-stroke"
animation_reverse = "uk-animation-reverse"
animation_fast = "uk-animation-fast"

background_default = "uk-background-default"
background_muted = "uk-background-muted"
background_primary = "uk-background-primary"
background_secondary = "uk-background-secondary"
background_cover = "uk-background-cover"
background_contain = "uk-background-contain"
background_width_1_1 = "uk-background-width-1-1"
background_height_1_1 = "uk-background-height-1-1"
background_top_left = "uk-background-top-left"
_background_top_right = "uk-background-top-right"
background_top_center = "uk-background-top-center"
background_center_left = "uk-background-center-left"
background_center_center = "uk-background-center-center"
background_center_right = "uk-background-center-right"
background_bottom_left = "uk-background-bottom-left"
background_bottom_center = "uk-background-bottom-center"
background_bottom_right = "uk-background-bottom-right"
background_no_repeat = "uk-background-norepeat"
background_image_s = "uk-background-image@s"
background_image_m = "uk-background-image@m"
background_image_l = "uk-background-image@l"
background_image_xl = "uk-background-image@xl"
background_blend_multiply = "uk-background-blend-multiply"
background_blend_screen = "uk-background-blend-screen"
background_blend_overlay = "uk-background-blend-overlay"
background_blend_darken = "uk-background-blend-darken"
background_blend_lighten = "uk-background-blend-lighten"
background_blend_color_dodge = "uk-background-blend-color-dodge"
background_blend_color_burn = "uk-background-blend-color-burn"
background_blend_hard_light = "uk-background-blend-hard-light"
background_blend_soft_light = "uk-background-blend-soft-light"
background_blend_difference = "uk-background-blend-difference"
background_blend_exclusion = "uk-background-blend-exclusion"
background_blend_hue = "uk-background-blend-hue"
background_blend_saturation = "uk-background-blend-saturation"
background_blend_color = "uk-background-blend-color"
background_blend_luminosity = "uk-background-blend-luminosity"

width_1_1 = "uk-width-1-1"
width_1_2 = "uk-width-1-2"
width_1_3 = "uk-width-1-3"
width_1_4 = "uk-width-1-4"
width_1_5 = "uk-width-1-5"
width_1_6 = "uk-width-1-6"
width_2_3 = "uk-width-2-3"
width_3_4 = "uk-width-3-4"
width_2_5 = "uk-width-2-5"
width_3_5 = "uk-width-3-5"
width_4_5 = "uk-width-4-5"
width_5_6 = "uk-width-5-6"

column_1_2 = "uk-column-1-2"
column_1_3 = "uk-column-1-3"
column_1_4 = "uk-column-1-4"
column_1_5 = "uk-column-1-5"
column_1_6 = "uk-column-1-6"

# Responsive classes for 640px and higher
column_1_2_s = "uk-column-1-2@s"
column_1_3_s = "uk-column-1-3@s"
column_1_4_s = "uk-column-1-4@s"
column_1_5_s = "uk-column-1-5@s"
column_1_6_s = "uk-column-1-6@s"

# Responsive classes for 960px and higher
column_1_2_m = "uk-column-1-2@m"
column_1_3_m = "uk-column-1-3@m"
column_1_4_m = "uk-column-1-4@m"
column_1_5_m = "uk-column-1-5@m"
column_1_6_m = "uk-column-1-6@m"

# Responsive classes for 1200px and higher
column_1_2_l = "uk-column-1-2@l"
column_1_3_l = "uk-column-1-3@l"
column_1_4_l = "uk-column-1-4@l"
column_1_5_l = "uk-column-1-5@l"
column_1_6_l = "uk-column-1-6@l"

# Responsive classes for 1600px and higher
column_1_2_xl = "uk-column-1-2@xl"
column_1_3_xl = "uk-column-1-3@xl"
column_1_4_xl = "uk-column-1-4@xl"
column_1_5_xl = "uk-column-1-5@xl"
column_1_6_xl = "uk-column-1-6@xl"

container_expand = "uk-container-expand"
container_small = "uk-container-small"
container_xsmall = "uk-container-xsmall"
container_xlarge = "uk-container-xlarge"
container_large = "uk-container-large"

position_top = "uk-position-top"
position_left = "uk-position-left"
position_right = "uk-position-right"
position_bottom = "uk-position-bottom"
position_top_left = "uk-position-top-left"
position_top_center = "uk-position-top-center"
position_top_right = "uk-position-top-right"
position_center = "uk-position-center"
position_center_left = "uk-position-center-left"
position_center_right = "uk-position-center-right"
position_bottom_left = "uk-position-bottom-left"
position_bottom_center = "uk-position-bottom-center"
position_bottom_right = "uk-position-bottom-right"
position_cover = "uk-position-cover"
position_center_left_out = "uk-position-center-left-out"
position_center_right_out = "uk-position-center-right-out"
position_small = "uk-position-small"
position_medium = "uk-position-medium"
position_large = "uk-position-large"
position_relative = "uk-position-relative"
position_absolute = "uk-position-absolute"
position_fixed = "uk-position-fixed"
position_z_index = "uk-position-z-index"

flex_align_left = "uk-flex-left"
flex_align_center = "uk-flex-center"
flex_align_right = "uk-flex-right"
flex_align_between = "uk-flex-between"
flex_align_around = "uk-flex-around"

flex_left_s = "uk-flex-left@s"
flex_center_s = "uk-flex-center@s"
flex_right_s = "uk-flex-right@s"
flex_between_s = "uk-flex-between@s"
flex_around_s = "uk-flex-around@s"

flex_left_m = "uk-flex-left@m"
flex_center_m = "uk-flex-center@m"
flex_right_m = "uk-flex-right@m"
flex_between_m = "uk-flex-between@m"
flex_around_m = "uk-flex-around@m"

flex_left_l = "uk-flex-left@l"
flex_center_l = "uk-flex-center@l"
flex_right_l = "uk-flex-right@l"
flex_between_l = "uk-flex-between@l"
flex_around_l = "uk-flex-around@l"

flex_left_xl = "uk-flex-left@xl"
flex_center_xl = "uk-flex-center@xl"
flex_right_xl = "uk-flex-right@xl"
flex_between_xl = "uk-flex-between@xl"
flex_around_xl = "uk-flex-around@xl"

flex_middle = "uk-flex-middle"
flex_bottom = "uk-flex-bottom"
flex_top = "uk-flex-top"
flex_stretch = "uk-flex-stretch"

flex_row = "uk-flex-row"
flex_row_reverse = "uk-flex-row-reverse"
flex_column = "uk-flex-column"
flex_column_reverse = "uk-flex-column-reverse"

flex_wrap = "uk-flex-wrap"
flex_wrap_reverse = "uk-flex-wrap-reverse"
flex_nowrap = "uk-flex-nowrap"

flex_wrap_stretch = "uk-flex-wrap-stretch"
flex_wrap_between = "uk-flex-wrap-between"
flex_wrap_around = "uk-flex-wrap-around"
flex_wrap_top = "uk-flex-wrap-top"
flex_wrap_middle = "uk-flex-wrap-middle"
flex_wrap_bottom = "uk-flex-wrap-bottom"

flex_first = "uk-flex-first"
flex_last = "uk-flex-last"
flex_first_s = "uk-flex-first@s"
flex_last_s = "uk-flex-last@s"
flex_first_m = "uk-flex-first@m"
flex_last_m = "uk-flex-last@m"
flex_first_l = "uk-flex-first@l"
flex_last_l = "uk-flex-last@l"
flex_first_xl = "uk-flex-first@xl"
flex_last_xl = "uk-flex-last@xl"

flex_none = "uk-flex-none"
flex_auto = "uk-flex-auto"
flex_1 = "uk-flex-1"

grid_small = "uk-grid-small"
grid_medium = "uk-grid-medium"
grid_large = "uk-grid-large"
grid_collapse = "uk-grid-collapse"

grid_column_small = "uk-grid-column-small"
grid_row_small = "uk-grid-row-small"
grid_column_medium = "uk-grid-column-medium"
grid_row_medium = "uk-grid-row-medium"
grid_column_large = "uk-grid-column-large"
grid_row_large = "uk-grid-row-large"
grid_column_collapse = "uk-grid-column-collapse"
grid_row_collapse = "uk-grid-row-collapse"

height_1_1 = "uk-height-1-1"
height_small = "uk-height-small"
height_max_small = "uk-height-max-small"
height_medium = "uk-height-medium"
height_max_medium = "uk-height-max-medium"
height_large = "uk-height-large"
height_max_large = "uk-height-max-large"

link_muted = "uk-link-muted"
link_text = "uk-link-text"
link_heading = "uk-link-heading"
link_reset = "uk-link-reset"
link_toggle = "uk-link-toggle"

list_disc = "uk-list-disc"
list_circle = "uk-list-circle"
list_square = "uk-list-square"
list_decimal = "uk-list-decimal"
list_hyphen = "uk-list-hyphen"

list_muted = "uk-list-muted"
list_emphasis = "uk-list-emphasis"
list_primary = "uk-list-primary"
list_secondary = "uk-list-secondary"
list_bullet = "uk-list-bullet"
list_divider = "uk-list-divider"
list_striped = "uk-list-striped"
list_large = "uk-list-large"
list_collapse = "uk-list-collapse"

margin = "uk-margin"
margin_top = "uk-margin-top"
margin_bottom = "uk-margin-bottom"
margin_left = "uk-margin-left"
margin_right = "uk-margin-right"
margin_small = "uk-margin-small"
margin_small_top = "uk-margin-small-top"
margin_small_bottom = "uk-margin-small-bottom"
margin_small_left = "uk-margin-small-left"
margin_small_right = "uk-margin-small-right"
margin_medium = "uk-margin-medium"
margin_medium_top = "uk-margin-medium-top"
margin_medium_bottom = "uk-margin-medium-bottom"
margin_medium_left = "uk-margin-medium-left"
margin_medium_right = "uk-margin-medium-right"
margin_large = "uk-margin-large"
margin_large_top = "uk-margin-large-top"
margin_large_bottom = "uk-margin-large-bottom"
margin_large_left = "uk-margin-large-left"
margin_large_right = "uk-margin-large-right"

margin_xlarge = "uk-margin-xlarge"
margin_xlarge_top = "uk-margin-xlarge-top"
margin_xlarge_bottom = "uk-margin-xlarge-bottom"
margin_xlarge_left = "uk-margin-xlarge-left"
margin_xlarge_right = "uk-margin-xlarge-right"

margin_remove = "uk-margin-remove"
margin_remove_top = "uk-margin-remove-top"
margin_remove_bottom = "uk-margin-remove-bottom"
margin_remove_left = "uk-margin-remove-left"
margin_remove_right = "uk-margin-remove-right"
margin_remove_vertical = "uk-margin-remove-vertical"
margin_remove_adjacent = "uk-margin-remove-adjacent"
margin_remove_first_child = "uk-margin-remove-first-child"
margin_remove_last_child = "uk-margin-remove-last-child"
margin_remove_left_s = "uk-margin-remove-left@s"
margin_remove_right_s = "uk-margin-remove-right@s"
margin_remove_left_m = "uk-margin-remove-left@m"
margin_remove_right_m = "uk-margin-remove-right@m"
margin_remove_left_l = "uk-margin-remove-left@l"
margin_remove_right_l = "uk-margin-remove-right@l"
margin_remove_left_xl = "uk-margin-remove-left@xl"
margin_remove_right_xl = "uk-margin-remove-right@xl"
margin_auto = "uk-margin-auto"
margin_auto_top = "uk-margin-auto-top"
margin_auto_bottom = "uk-margin-auto-bottom"
margin_auto_left = "uk-margin-auto-left"
margin_auto_right = "uk-margin-auto-right"
margin_auto_vertical = "uk-margin-auto-vertical"
margin_auto_left_s = "uk-margin-auto-left@s"
margin_auto_s = "uk-margin-auto@s"
margin_auto_right_s = "uk-margin-auto-right@s"

margin_auto_left_m = "uk-margin-auto-left@m"
margin_auto_m = "uk-margin-auto@m"
margin_auto_right_m = "uk-margin-auto-right@m"

margin_auto_left_l = "uk-margin-auto-left@l"
margin_auto_l = "uk-margin-auto@l"
margin_auto_right_l = "uk-margin-auto-right@l"

margin_auto_left_xl = "uk-margin-auto-left@xl"
margin_auto_xl = "uk-margin-auto@xl"
margin_auto_right_xl = "uk-margin-auto-right@xl"

padding = "uk-padding"
padding_small = "uk-padding-small"
padding_large = "uk-padding-large"

padding_remove = "uk-padding-remove"
padding_remove_top = "uk-padding-remove-top"
padding_remove_bottom = "uk-padding-remove-bottom"
padding_remove_left = "uk-padding-remove-left"
padding_remove_right = "uk-padding-remove-right"
padding_remove_vertical = "uk-padding-remove-vertical"
padding_remove_horizontal = "uk-padding-remove-horizontal"

float_left = "uk-float-left"
float_right = "uk-float-right"
clearfix = "uk-clearfix"
overflow_hidden = "uk-overflow-hidden"
overflow_auto = "uk-overflow-auto"

resize = "uk-resize"
resize_vertical = "uk-resize-vertical"

display_block = "uk-display-block"
display_inline = "uk-display-inline"
display_inline_block = "uk-display-inline-block"

inline = "uk-inline"
inline_clip = "uk-inline-clip"

responsive_width = "uk-responsive-width"
responsive_height = "uk-responsive-height"
preserve_width = "uk-preserve-width"
object_cover = "uk-object-cover"
object_contain = "uk-object-contain"
object_fill = "uk-object-fill"
object_none = "uk-object-none"
object_scale_down = "uk-object-scale-down"

object_position_top_left = "uk-object-position-top-left"
object_position_top_center = "uk-object-position-top-center"
object_position_top_right = "uk-object-position-top-right"
object_position_center_left = "uk-object-position-center-left"
object_position_center_center = "uk-object-position-center-center"
object_position_center_right = "uk-object-position-center-right"
object_position_bottom_left = "uk-object-position-bottom-left"
object_position_bottom_center = "uk-object-position-bottom-center"
object_position_bottom_right = "uk-object-position-bottom-right"

border_rounded = "uk-border-rounded"
border_circle = "uk-border-circle"
border_pill = "uk-border-pill"

box_shadow_small = "uk-box-shadow-small"
box_shadow_medium = "uk-box-shadow-medium"
box_shadow_large = "uk-box-shadow-large"
box_shadow_xlarge = "uk-box-shadow-xlarge"

box_shadow_bottom = "uk-box-shadow-bottom"

box_shadow_hover_small = "uk-box-shadow-hover-small"
box_shadow_hover_medium = "uk-box-shadow-hover-medium"
box_shadow_hover_large = "uk-box-shadow-hover-large"
box_shadow_hover_xlarge = "uk-box-shadow-hover-xlarge"

dropcap = "uk-dropcap"
logo = "uk-logo"

blend_multiply = "uk-blend-multiply"
blend_screen = "uk-blend-screen"
blend_overlay = "uk-blend-overlay"
blend_darken = "uk-blend-darken"
blend_lighten = "uk-blend-lighten"
blend_color_dodge = "uk-blend-color-dodge"
blend_color_burn = "uk-blend-color-burn"
blend_hard_light = "uk-blend-hard-light"
blend_soft_light = "uk-blend-soft-light"
blend_difference = "uk-blend-difference"
blend_exclusion = "uk-blend-exclusion"
blend_hue = "uk-blend-hue"
blend_saturation = "uk-blend-saturation"
blend_color = "uk-blend-color"
blend_luminosity = "uk-blend-luminosity"

transform_center = "uk-transform-center"

transform_origin_top_left = "uk-transform-origin-top-left"
transform_origin_top_center = "uk-transform-origin-top-center"
transform_origin_top_right = "uk-transform-origin-top-right"
transform_origin_center_left = "uk-transform-origin-center-left"
transform_origin_center_right = "uk-transform-origin-center-right"
transform_origin_bottom_left = "uk-transform-origin-bottom-left"
transform_origin_bottom_center = "uk-transform-origin-bottom-center"
transform_origin_bottom_right = "uk-transform-origin-bottom-right"

disabled = "uk-disabled"
drag = "uk-drag"

light = "uk-light"
dark = "uk-dark"

width_1_1 = "uk-width-1-1"
width_1_2 = "uk-width-1-2"
width_1_3 = "uk-width-1-3"
width_2_3 = "uk-width-2-3"
width_1_4 = "uk-width-1-4"
width_3_4 = "uk-width-3-4"
width_1_5 = "uk-width-1-5"
width_2_5 = "uk-width-2-5"
width_3_5 = "uk-width-3-5"
width_4_5 = "uk-width-4-5"
width_1_6 = "uk-width-1-6"
width_5_6 = "uk-width-5-6"
width_auto = "uk-width-auto"
width_expand = "uk-width-expand"
child_width_1_2 = "uk-child-width-1-2"
child_width_1_3 = "uk-child-width-1-3"
child_width_1_4 = "uk-child-width-1-4"
child_width_1_5 = "uk-child-width-1-5"
child_width_1_6 = "uk-child-width-1-6"
child_width_auto = "uk-child-width-auto"
child_width_expand = "uk-child-width-expand"
width_small = "uk-width-small"
width_medium = "uk-width-medium"
width_large = "uk-width-large"
width_xlarge = "uk-width-xlarge"
width_2xlarge = "uk-width-2xlarge"
uk_width_1_1_m = "uk-width-1-1@m"
uk_width_1_2_m = "uk-width-1-2@m"
uk_width_1_3_m = "uk-width-1-3@m"
uk_width_2_3_m = "uk-width-2-3@m"
uk_width_1_4_m = "uk-width-1-4@m"
uk_width_3_4_m = "uk-width-3-4@m"
uk_width_1_5_m = "uk-width-1-5@m"
uk_width_2_5_m = "uk-width-2-5@m"
uk_width_3_5_m = "uk-width-3-5@m"
uk_width_4_5_m = "uk-width-4-5@m"
uk_width_1_6_m = "uk-width-1-6@m"
uk_width_5_6_m = "uk-width-5-6@m"
uk_width_auto_m = "uk-width-auto@m"
uk_width_expand_m = "uk-width-expand@m"

uk_width_1_1_s = "uk-width-1-1@s"
uk_width_1_2_s = "uk-width-1-2@s"
uk_width_1_3_s = "uk-width-1-3@s"
uk_width_2_3_s = "uk-width-2-3@s"
uk_width_1_4_s = "uk-width-1-4@s"
uk_width_3_4_s = "uk-width-3-4@s"
uk_width_1_5_s = "uk-width-1-5@s"
uk_width_2_5_s = "uk-width-2-5@s"
uk_width_3_5_s = "uk-width-3-5@s"
uk_width_4_5_s = "uk-width-4-5@s"
uk_width_1_6_s = "uk-width-1-6@s"
uk_width_5_6_s = "uk-width-5-6@s"
uk_width_auto_s = "uk-width-auto@s"
uk_width_expand_s = "uk-width-expand@s"

uk_width_1_1_l = "uk-width-1-1@l"
uk_width_1_2_l = "uk-width-1-2@l"
uk_width_1_3_l = "uk-width-1-3@l"
uk_width_2_3_l = "uk-width-2-3@l"
uk_width_1_4_l = "uk-width-1-4@l"
uk_width_3_4_l = "uk-width-3-4@l"
uk_width_1_5_l = "uk-width-1-5@l"
uk_width_2_5_l = "uk-width-2-5@l"
uk_width_3_5_l = "uk-width-3-5@l"
uk_width_4_5_l = "uk-width-4-5@l"
uk_width_1_6_l = "uk-width-1-6@l"
uk_width_5_6_l = "uk-width-5-6@l"
uk_width_auto_l = "uk-width-auto@l"
uk_width_expand_l = "uk-width-expand@l"

uk_width_1_1_xl = "uk-width-1-1@xl"
uk_width_1_2_xl = "uk-width-1-2@xl"
uk_width_1_3_xl = "uk-width-1-3@xl"
uk_width_2_3_xl = "uk-width-2-3@xl"
uk_width_1_4_xl = "uk-width-1-4@xl"
uk_width_3_4_xl = "uk-width-3-4@xl"
uk_width_1_5_xl = "uk-width-1-5@xl"
uk_width_2_5_xl = "uk-width-2-5@xl"
uk_width_3_5_xl = "uk-width-3-5@xl"
uk_width_4_5_xl = "uk-width-4-5@xl"
uk_width_1_6_xl = "uk-width-1-6@xl"
uk_width_5_6_xl = "uk-width-5-6@xl"
uk_width_auto_xl = "uk-width-auto@xl"
uk_width_expand_xl = "uk-width-expand@xl"

text_lead = "uk-text-lead"
text_default = "uk-text-default"
text_large = "uk-text-large"
text_light = "uk-text-light"
text_normal = "uk-text-normal"
text_bold = "uk-text-bold"
text_lighter = "uk-text-lighter"
text_bolder = "uk-text-bolder"
text_italic = "uk-text-italic"
text_capitalize = "uk-text-capitalize"
text_uppercase = "uk-text-uppercase"
text_lowercase = "uk-text-lowercase"
text_decoration_none = "uk-text-decoration-none"
text_muted = "uk-text-muted"
text_emphasis = "uk-text-emphasis"
text_primary = "uk-text-primary"
text_secondary = "uk-text-secondary"
text_success = "uk-text-success"
text_warning = "uk-text-warning"
text_danger = "uk-text-danger"
text_background = "uk-text-background"
text_left = "uk-text-left"
text_right = "uk-text-right"
text_center = "uk-text-center"
text_justify = "uk-text-justify"
text_left_s = "uk-text-left@s"
text_center_s = "uk-text-center@s"
text_right_s = "uk-text-right@s"

text_left_m = "uk-text-left@m"
text_center_m = "uk-text-center@m"
text_right_m = "uk-text-right@m"

text_left_l = "uk-text-left@l"
text_center_l = "uk-text-center@l"
text_right_l = "uk-text-right@l"

text_left_xl = "uk-text-left@xl"
text_center_xl = "uk-text-center@xl"
text_right_xl = "uk-text-right@xl"
text_top = "uk-text-top"
text_middle = "uk-text-middle"
text_bottom = "uk-text-bottom"
text_baseline = "uk-text-baseline"
text_truncate = "uk-text-truncate"
text_break = "uk-text-break"
text_nowrap = "uk-text-nowrap"

transition_fade = "uk-transition-fade"
transition_scale_up = "uk-transition-scale-up"
transition_scale_down = "uk-transition-scale-down"
transition_slide_top = "uk-transition-slide-top"
transition_slide_bottom = "uk-transition-slide-bottom"
transition_slide_left = "uk-transition-slide-left"
transition_slide_right = "uk-transition-slide-right"
transition_slide_top_small = "uk-transition-slide-top-small"
transition_slide_bottom_small = "uk-transition-slide-bottom-small"
transition_slide_left_small = "uk-transition-slide-left-small"
transition_slide_right_small = "uk-transition-slide-right-small"
transition_slide_top_medium = "uk-transition-slide-top-medium"
transition_slide_bottom_medium = "uk-transition-slide-bottom-medium"
transition_slide_left_medium = "uk-transition-slide-left-medium"
transition_slide_right_medium = "uk-transition-slide-right-medium"

hidden = "uk-hidden"
invisible = "uk-invisible"
hidden_s = "uk-hidden@s"
hidden_m = "uk-hidden@m"
hidden_l = "uk-hidden@l"
hidden_xl = "uk-hidden@xl"


visible_s = "uk-visible@s"
visible_m = "uk-visible@m"
visible_l = "uk-visible@l"
visible_xl = "uk-visible@xl"

hidden_hover = "uk-hidden-hover"
hidden_invisible_hover = "uk-hidden-invisible-hover"

hidden_touch = "uk-hidden-touch"
hidden_notouch = "uk-hidden-notouch"
