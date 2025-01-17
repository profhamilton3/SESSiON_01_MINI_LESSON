'''
1.  Turn on LED pixels
2.  Display Image
3.  Scroll Text
4.  Display Heartbeat with two images
5.  Use show_icon parameters to realize the animation
6.  Add Wukong extention
7.  Control wukong lights
'''

# 1. Turn on LED Pixils in the grid
basic.show_leds("""
. . . . .
. # . # .
. . # . .
# . . . #
. # # # .
""")

#2. basic.show_icon(IconNames.HEART)
#3. basic.show_string("Hello!")
#4  basic.show_icon(IconNames.SMALL_HEART)
#5 Use loop to simulate heart beat animation
''' intruduce built in basic forever loop'''
def on_forever():
    ''' python code modules are defined by indenting'''
    basic.show_icon(IconNames.HEART,750)
    basic.show_icon(IconNames.SMALL_HEART, 350)

#basic.forever(on_forever)

#6 wukong extention - use Neopixel lights on board
'''Available for Neopixel database	Connect to micro:bit P16 port'''
#similator on Pin.P0, or Pin.P1
strip = neopixel.create(DigitalPin.P0, 4, NeoPixelMode.RGB)
strip.set_pixel_color(0, NeoPixelColors.VIOLET)
strip.set_pixel_color(1, NeoPixelColors.GREEN)
strip.set_pixel_color(2, NeoPixelColors.RED)
strip.set_pixel_color(3, NeoPixelColors.YELLOW)
strip.show()


#7 Use input buttons to control neopixel lights
# use the global strip object with button inputs
def on_button_pressed_a():
    strip.set_pixel_color(0, NeoPixelColors.INDIGO)
    strip.set_pixel_color(1, NeoPixelColors.INDIGO)
    strip.set_pixel_color(2, NeoPixelColors.INDIGO)
    strip.set_pixel_color(3, NeoPixelColors.INDIGO)
    strip.show()

input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    strip.set_pixel_color(0, NeoPixelColors.BLACK)
    strip.set_pixel_color(1, NeoPixelColors.BLACK)
    strip.set_pixel_color(2, NeoPixelColors.BLACK)
    strip.set_pixel_color(3, NeoPixelColors.BLACK)
    strip.show()
input.on_button_pressed(Button.B, on_button_pressed_b)
