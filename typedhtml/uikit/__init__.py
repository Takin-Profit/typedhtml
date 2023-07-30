# Copyright 2023 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.


from .accordion import accordion, accordion_content, accordion_item, accordion_title
from .alert import alert
from .article import article, article_title
from .badge import badge
from .button import button, button_group
from .card import card, card_title

__all__ = [
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
