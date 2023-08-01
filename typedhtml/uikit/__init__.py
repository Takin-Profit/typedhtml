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
from .height import height
from .icon import icon, icon_nav
from .image import image
from .label import label

__all__ = [
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
