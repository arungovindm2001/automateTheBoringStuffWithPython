## 1. What is an RGBA value?

An RGBA value is a group of numbers that specify the amount of red, green, blue, and alpha in a color. Each of these component values is an integer from 0 (none at all) to 255 (the maximum).

## 2. How can you get the RGBA value of 'CornflowerBlue' from the Pillow module?

`ImageColor.getcolor('CornflowerBlue', 'RGBA')`

## 3. What is a box tuple?

A box tuple is a tuple of four integer coordinates that represent a rectangular region in an image i.e. the left-edge x-coordinate, the top-edge y-coordinate, the width, and the height, respectively.

## 4. What function returns an Image object for, say, an image file named zophie.png?

`Image.open('zophie.png')`

## 5. How can you find out the width and height of an Image object’s image?

`Image.open(<Image-File>).size`<br />
This gives a tuple of two integers - the width and the height of the image respectively.<br />
For example:<br />
(816, 1088) where 816 is the width and 1088 is the height.

## 6. What method would you call to get Image object for a 100×100 image, excluding the lower-left quarter of it?

`<Image Object>.crop((0, 50, 50, 50))`

## 7. After making changes to an Image object, how could you save it as an image file?

`<Image Object>.save(<new_filename.png>)`

## 8. What module contains Pillow’s shape-drawing code?

The `ImageDraw` module

## 9. Image objects do not have drawing methods. What kind of object does? How do you get this kind of object?

`ImageDraw` objects have different shape drawing methods like `point()`, `line()`, `rectangle()`, `ellipse()`, `polygon()`. We give coordinates as arguments (fill and outline too but they are optional) to these methods.

