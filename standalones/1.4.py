import cairo

WIDTH, HEIGHT = 256, 256

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)

ctx.translate(0.1, 0.1)

points = (
    (0,10,80,10),  
    (80, 10, 70, 40),
    (70,40, 40, 70),
    (40, 70,10,40),
    (10,40,0,10),
)

for point in points:
    x1,y1,x2,y2 = point
    ctx.move_to(x1/100, y1/100)
    ctx.line_to(x2/100,y2/100)
    
for point in points:
    x1,y1,x2,y2 = point
    ctx.move_to(x1/100, y1/100)
    ctx.arc(x1/100, y1/100, 0.1, 0, 360)

ctx.set_source_rgb(0.6, 0.6, 0.6)
ctx.set_line_width(0.01)
ctx.stroke()
surface.write_to_png("1_4.png")