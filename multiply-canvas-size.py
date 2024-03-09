#!/usr/bin/env python

from gimpfu import *

def multiply_canvas_size(image, drawable, in_width, in_height, in_guides):
    if (in_width > 1) or (in_height > 1):
        gimp.context_push()
        image.undo_group_start()

        old_width = int(image.width)
        old_height = int(image.height)
        in_width = int(in_width)
        in_height = int(in_height)
        
        pdb.gimp_image_resize(image, image.width*in_width, image.height*in_height, 0, 0)
        if in_guides:
            if in_width > 1:
                for x in range(1, in_width):
                    pdb.gimp_image_add_vguide(image, x*old_width)
                
            if in_height > 1:
                for x in range(1, in_height):
                    pdb.gimp_image_add_hguide(image, x*old_height)
                
        image.undo_group_end()
        gimp.displays_flush()
        gimp.context_pop()

    return

register(
    "multiply_canvas_size",    
    "Multiply canvas size",
    "Resizes canvas by multiplying current size. For example, picture 100x200 with settings w2 h3 will change canvas size to 200x600. It's a shorthand method for standard canvas resize.",
    "Krzysztof Blachnicki", 
    "krzysiu.net", 
    "January 2019",
    "<Image>/Filters/Krzysiu/Multiply canvas size...", 
    "*", 
    [
        (PF_SLIDER, "in_width", "Width multipler:", 1, (1, 20, 1)),
        (PF_SLIDER, "in_height", "Height multipler:", 1, (1, 20, 1)),
        (PF_TOGGLE, "in_guides", "Add guide lines", False)
    ], 
    [],
    multiply_canvas_size,
    )

main()