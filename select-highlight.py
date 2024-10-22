#!/usr/bin/env python

from gimpfu import *

def highlight_selection(image, drawable, in_bg_color, in_copy_color, in_bg_opacity, in_border_color, in_border_opacity, in_border_size, in_border_radius, in_border_type) :
    gimp.context_push()
    image.undo_group_start()
    if in_copy_color:
         in_border_color = in_bg_color
    layer = pdb.gimp_layer_new(image, image.width, image.height, RGBA_IMAGE, "Hightlight plugin workspace", 100, NORMAL_MODE)
    pdb.gimp_image_insert_layer(image, layer, None, -1)
    
    pdb.gimp_context_set_background(in_border_color)

    if in_border_radius>0:
        pdb.script_fu_selection_rounded_rectangle(image, layer, in_border_radius, 0)   
        
    if in_border_type==0:
        pdb.gimp_selection_grow(image, in_border_size)
    elif in_border_type==2:
        pdb.gimp_selection_grow(image, in_border_size/2)
        
    if in_border_opacity>0:
        pdb.gimp_edit_bucket_fill_full(layer, BG_BUCKET_FILL, NORMAL_MODE, in_border_opacity, 0, True, False, SELECT_CRITERION_COMPOSITE, 0, 0)
        pdb.gimp_selection_shrink(image, in_border_size)
        pdb.gimp_edit_clear(layer)
    

    if in_bg_opacity>0:
        pdb.gimp_context_set_background(in_bg_color)
        pdb.gimp_edit_bucket_fill_full(layer, BG_BUCKET_FILL, NORMAL_MODE, in_bg_opacity, 0, True, False, SELECT_CRITERION_COMPOSITE, 0, 0) 
    
    pdb.gimp_image_merge_down(image, layer, EXPAND_AS_NECESSARY)

    image.undo_group_end()
    gimp.displays_flush()
    gimp.context_pop()

    return

register(
    "krzysiu_select_red",    
    "Highlight selection",   
    "Highlight selection",
    "Krzysztof Blachnicki", 
    "krzysiu.net", 
    "December 2015",
    "<Image>/Filters/Krzysiu/Highlight selection...", 
    "*", 
    [
        (PF_COLOR, "in_bg_color", "Color of background:", (255, 0, 0)),
        (PF_TOGGLE, "in_copy_color", "Use background color for border", 0),
        (PF_SLIDER, "in_bg_opacity", "Opacity of background (%; 0=off):", 10, (0, 100, 1)),
        (PF_COLOR, "in_border_color", "Border color:", (255, 0, 0)),
        (PF_SLIDER, "in_border_opacity", "Opacity of border (%; 0=off):", 90, (0, 100, 1)),
        (PF_SPINNER, "in_border_size", "Border size (px):", 2, (1, 100, 1)),
        (PF_SPINNER, "in_border_radius", "Border radius (%; 0=rectangle):", 30, (0, 100, 1)),
        (PF_OPTION, "in_border_type", "Border type:", 0, ["Outer","Inner","Middle"])
    ], 
    [],
    highlight_selection,
    )

main()
