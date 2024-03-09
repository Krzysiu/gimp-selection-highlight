#!/usr/bin/env python
# coding=utf-8

from gimpfu import *
import os
import gtk

def watermark_from_svg(image, drawable, in_file_name, in_set_default, in_watermark_width, in_watermark_margin, in_placement, in_opacity, in_invert):
    
    if os.path.isfile(in_file_name)==False:
        kgpp_msgbox("The watermark file doesn't exist", "Following file doesn't exist:\n<tt>%s</tt>" % (in_file_name), gtk.MESSAGE_ERROR)
        return
        
    settingsFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "watermark-image.ini")
    
    if in_set_default:
        kgpp_msgbox("Default watermark file change", "You need to restart Gimp to apply changes.\n\nTo reset settings, remove following file:\n<tt>%s</tt>" % (settingsFile), gtk.MESSAGE_INFO)
        fh = open(settingsFile, "w")
        fh.write(in_file_name)
        fh.close() 
        

    gimp.context_push()
    image.undo_group_start()
    
    water = pdb.gimp_file_load_layer(image, in_file_name)
    pdb.gimp_image_insert_layer(image, water, None, -1)

    pdb.gimp_item_set_name(water, "SVG watermark")
    pdb.gimp_layer_set_opacity(water, in_opacity)
    
    pdb.gimp_context_set_interpolation(INTERPOLATION_LANCZOS)
    water_new_width = int(drawable.width * (in_watermark_width / 100))
    water_new_height = int(water_new_width * water.height / water.width)

    pdb.gimp_context_set_transform_resize(3)
    pdb.gimp_layer_scale(water, water_new_width, water_new_height, False)
    
    img_space_x = int(drawable.width * (in_watermark_margin / 100))
    img_space_y = int(drawable.height * (in_watermark_margin / 100))
    if in_placement==0:
        water_space_x = img_space_x
        water_space_y = img_space_y
    elif in_placement==1:
        water_space_x = drawable.width - (img_space_x + water.width)
        water_space_y = img_space_y
    elif in_placement==2:
        water_space_x = img_space_x
        water_space_y = drawable.height - (img_space_y + water.height)
    elif in_placement==3:
        water_space_x = drawable.width - (img_space_x + water.width)
        water_space_y = drawable.height - (img_space_y + water.height)
        
    pdb.gimp_layer_set_offsets(water, water_space_x, water_space_y)

    if in_invert:
        pdb.gimp_invert(water)
    
    image.undo_group_end()
    gimp.displays_flush()
    gimp.context_pop()

    return

def kgpp_msgbox(msg1, msg2, type):
    msgbox = gtk.MessageDialog(
        None, 
        gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT, 
        type, 
        gtk.BUTTONS_OK,
        msg1
    )

    msgbox.format_secondary_markup(msg2)
    msgbox.set_title("KGPP - Watermark with SVG")
    msgbox.set_position(gtk.WIN_POS_CENTER)
    msgbox.run()
    return

kgppSetFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "watermark-image.ini")
kgppWatermarkFile = os.path.join(os.path.dirname(os.path.realpath(__file__)), "watermark-image.svg")

if os.path.isfile(kgppSetFile):
    kgppSFileHandle = open(kgppSetFile, "r")
    kgppWatermarkFileCheck = kgppSFileHandle.read().strip()
    kgppSFileHandle.close() 
    if os.path.isfile(kgppWatermarkFileCheck):
        kgppWatermarkFile = kgppWatermarkFileCheck

register(
    "watermark_from_svg",    
    "Watermark file with SVG",   
    "Watermark file with SVG",
    "Krzysztof Blachnicki", 
    "krzysiu.net", 
    "April 2018",
    "<Image>/Filters/Krzysiu/Watermark file with SVG...", 
    "*", 
    [
        (PF_FILE, "in_file_name", "Watermark file:", kgppWatermarkFile),
        (PF_TOGGLE, "in_set_default", "Set this file as default:", 0),
        (PF_SPINNER, "in_watermark_width", "Watermark width (% of image):", 20, (1, 100, 1)),
        (PF_SPINNER, "in_watermark_margin", "Margin (% of image):", 1, (0, 50, 1)),
        (PF_OPTION, "in_placement", "Position:", 3, ["[▀  ]Top left","[  ▀] Top right","[▄  ] Bottom left","[  ▄] Bottom right"]),
        (PF_SPINNER, "in_opacity", "Opacity (%):", 60, (0, 100, 1)),
        (PF_TOGGLE, "in_invert", "Invert colors:", 0)
    ], 
    [],
    watermark_from_svg,
    )

main()

