#!/usr/bin/env python
# coding=utf-8

# Version history:
# 0.2 (09-03-2024)
# * added this block ;)
# * left-right confusion friendly dropbox choices
# * handle better incorrect formats (like one without %d)
# * new mode - Roman numerals
# * fine tuning of position

from gimpfu import *
import random

def add_number_layers(image, drawable, in_int_start, in_int_end, in_int_step, in_font, in_font_size, in_font_color, in_font_opacity, in_random_pos, in_group_name, in_bg_merge, in_bg_layer, in_font_align, in_tuning_x, in_font_valign, in_tuning_y, in_roman_numerals, in_string_format) :

    gimp.context_push()
    image.undo_group_start()

    if in_bg_merge:
        data_input_alpha = pdb.gimp_drawable_has_alpha(in_bg_layer)
    layer_group = None
    
    if in_group_name!="":
        layer_group = pdb.gimp_layer_group_new(image)
        pdb.gimp_image_insert_layer(image, layer_group, None, -1)
        pdb.gimp_item_set_name(layer_group, in_group_name)
    
    for i in xrange(int(in_int_start),int(in_int_end)+1,int(in_int_step)):
        if in_roman_numerals:
            if in_string_format!="":
                current_no = in_string_format.replace('%d', int_to_roman(i))
            else:
                current_no = int_to_roman(i)
        else:
            if in_string_format!="":
                format_copy = in_string_format
                try:
                    current_no = in_string_format % i # if there's no %d in format, it will fail...
                except:
                    current_no = format_copy # ...and break current_no variable, so it's read from copy in fail case
                    pass
            else:
                current_no = str(i)
                
        if in_bg_merge:
            bg_layer = pdb.gimp_layer_copy(in_bg_layer, data_input_alpha)
            pdb.gimp_image_insert_layer(image, bg_layer, layer_group, -1)
            
        label_layer = pdb.gimp_text_layer_new(image, current_no, in_font, in_font_size, 0)
        pdb.gimp_image_insert_layer(image, label_layer, layer_group, -1)
        pdb.gimp_text_layer_set_color(label_layer, in_font_color)
        if in_font_opacity != 100:
            pdb.gimp_layer_set_opacity(label_layer, in_font_opacity)
        
        if in_font_align==0:
            pdb.gimp_text_layer_set_justification(label_layer, TEXT_JUSTIFY_LEFT)
        if in_font_align==1:
            pdb.gimp_text_layer_set_justification(label_layer, TEXT_JUSTIFY_CENTER)
        if in_font_align==2:
            pdb.gimp_text_layer_set_justification(label_layer, TEXT_JUSTIFY_RIGHT)
            
        if in_bg_merge:
            if in_font_align==0:
                text_pos_x = bg_layer.offsets[0]
            elif in_font_align==1:
                text_pos_x = bg_layer.offsets[0] + (bg_layer.width/2) - (label_layer.width/2)
            elif in_font_align==2:
                text_pos_x = bg_layer.offsets[0] + bg_layer.width - label_layer.width                
            
            if in_font_valign==0:
                text_pos_y = bg_layer.offsets[1]
            elif in_font_valign==1:
                text_pos_y = bg_layer.offsets[1] + (bg_layer.height/2) - (label_layer.height/2)
            elif in_font_valign==2:
                text_pos_y = bg_layer.offsets[1] + bg_layer.height - label_layer.height
            
            
            text_pos_y = text_pos_y + in_tuning_y # advanced math, counting offset
            text_pos_x = text_pos_x + in_tuning_x
            pdb.gimp_layer_set_offsets(label_layer, text_pos_x, text_pos_y)
            layer_done = pdb.gimp_image_merge_down(image, label_layer, EXPAND_AS_NECESSARY)
        else:
            layer_done = label_layer
            
        if in_random_pos:
            pdb.gimp_layer_set_offsets(layer_done, random.randint(0, image.width-layer_done.width), random.randint(0, image.height-layer_done.height))
        pdb.gimp_item_set_name(layer_done, "Autonumber (\"" + current_no + "\")")
    
    image.undo_group_end()
    gimp.displays_flush()
    gimp.context_pop()

    return
    
# Um9tYW5lcyBldW50IGRvbXVzISA
def int_to_roman(num):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
        40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
        400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }
    roman_numeral = ''
    if num == 0:
        return "0"
    for value in sorted(roman_numerals.keys(), reverse=True):
        while num >= value:
            roman_numeral += roman_numerals[value]
            num -= value

    return roman_numeral
    
           
register(
    "add_number_layers",    
    "Add number layers",   
    "Add number layers",
    "Krzysztof Blachnicki", 
    "krzysiu.net", 
    "December 2015",
    "<Image>/Filters/Krzysiu/Add number layers...", 
    "*", 
    [
        (PF_SPINNER, "in_int_start", "Start number:", 0, (0, 100000, 1)),
        (PF_SPINNER, "in_int_end", "End number:", 5, (1, 100000, 1)),
        (PF_SPINNER, "in_int_step", "Step:", 1, (1, 100000, 1)),
        (PF_FONT, "in_font", "Font:", "Serif"),
        (PF_SPINNER, "in_font_size", "Font size (px):", 12, (3, 500, 1)),
        (PF_COLOR, "in_font_color", "Text color:", (0, 0, 0)),
        (PF_SLIDER, "in_font_opacity", "Text opacity (%):", 100, (1, 100, 1)),
        (PF_TOGGLE, "in_random_pos", "Randomize position of layers:", 1),
        (PF_STRING, "in_group_name", "Layer group name (leave empty to disable grouping):", ""),
        (PF_TOGGLE, "in_bg_merge", "Merge with background layer:", 0),
        (PF_LAYER, "in_bg_layer", "Background layer:", None),
        (PF_OPTION,"in_font_align", "Multiline text align / horizontal align:", 1, ["Left [▓░░]", "Center [░▓░] ", "Right [░░▓] "]),
        (PF_SPINNER, "in_tuning_x", "Offset tuning of the above (in px):", 0, (-5000, 5000, 1)),
        (PF_OPTION,"in_font_valign", "Vertical align to background:", 1, ["Top", "Middle", "Bottom"]),
        (PF_SPINNER, "in_tuning_y", "Offset tuning of the above (in px):", 0, (-5000, 5000, 1)),
        (PF_TOGGLE, "in_roman_numerals", "Use roman numerals:", 0),
        (PF_TEXT, "in_string_format", "Advanced - custom string format (%d is the number):", "")
        
    ], 
    [],
    add_number_layers,
    )

main()
