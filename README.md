# gimp-plugin-pack

For the installation, requiments, list of plugins with description, usage and example images visit [Gimp Plugin Pack wiki](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki)

## Basic plugin list
+ [Highlight selection](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Highlight-selection) <sub>`select-highlight.py`</sub> - fill selection with color and border it
+ [Render cloudy background](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Render-cloudy-background) <sub>`cloudy-background.py`</sub> - renders random clouds/gradients in chosen color, very nice for backgrounds
+ [Dreamy picture](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Dreamy-picture) <sub>`dreamy-picture.py`</sub> - variation of Orton effect - creates dream alike pictures - glowing objects with intense colors
+ [Add number layers](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Add-number-layers) <sub>`add-number-layers.py`</sub> - generates layers with numbers - possible aligning, formatting (like *001*), applying background for generated layers, Roman numerals and a lot more
+ [Animate hue](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Animate-hue) <sub>`animate-hue.py`</sub> - generates colorized layers, which are ready to use for GIF animation
+ [Watermark file with SVG](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Watermark-file-with-SVG) <sub>`watermark-image.py` + example: `watermark-image.svg`</sub> - adds SVG watermark to image with relative size and margins
+ [SVG to multisize icon](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/SVG-to-multisize-icon) <sub>`svg-to-multisize-icon.py`</sub> - imports SVG file to create multisize icon. It utilizes the vector imaging power by importing different sizes - not just resizing in Gimp
+ [Bounce animation](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Bounce-animation) <sub>`bonuce-animation.py`</sub> - converts animation to infinite loop (e.g. `1 2 3 4 <sub>1 2 3 4 1 2...</sub>` to `1 2 3 4 <sub>3 2 1 2 3 4 3...</sub>`
+ [Multiply canvas size](https://github.com/Krzysiu/krzysiu-gimp-plugin-pack/wiki/Multiply-canvas-size) <sub>`multiply-canvas-size.py`</sub> - multiplies canvas size (e.g. width x2, height x3) and optionally adds guide lines

## Changelog
### Icons:
+ :beetle: bug fix
+ :hatching_chick: new plugin
+ :arrow_down: minor change
+ :arrow_up: major change

### 22 October 2024
+ :arrow_up: **Highlight selection** simplify process: ability to reuse background color as border
+ :arrow_down: **Watermark image** set default mode to overlay and opacity 100 (much better for watermarking than previous normal/60)
+ :arrow_down: clean up change log
+ :arrow_down: added asset with current version 

### 1 Jun 2024
+ :arrow_up: **Watermark image** ability to set blending mode (try overlay!)

### 15 March 2024
+ :arrow_up: **Watermark image** beta feature: automatically set watermark color (white/black)

### 9 March 2024
+ :arrow_down: **Watermark image** cosmetic changes for people suffering left-right confusion
+ :beetle: **Multiply canvas size** not obeying guide line settings

### 14 January 2019
+ :hatching_chick: **Multiply canvas size**

### 13 September 2018
+ :hatching_chick: **Bounce animation**
+ :arrow_down: removed debug procedures from **Watermark file with SVG**

### 03 May 2018
+ :hatching_chick: **SVG to multisize icon**

### 05 April 2018
+ :hatching_chick: **Watermark file with SVG**

### 20 March 2016
+ :hatching_chick: **Animate hue**

### 10 December 2015
+ :hatching_chick: :hatching_chick: **Dreamy picture** and **Add number layers**
+ :arrow_down: fixed bug in Render cloudy background
