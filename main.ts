/** 
1.  Turn on LED pixels
2.  Display Image
3.  Scroll Text
4.  Display Heartbeat with two images
5.  Use show_icon parameters to realize the animation
6.  Add Wukong extention
7.  Control wukong lights

 */
//  1. Turn on LED Pixils
basic.showLeds(`
. . . . .
. . . . .
. . # . .
. . . . .
. . . . .
`)
// 2. basic.show_icon(IconNames.HEART)
// 3. basic.show_string("Hello!")
// 4  basic.show_icon(IconNames.SMALL_HEART)
// 5 Use loop to simulate heart beat animation
/** intruduce built in basic forever loop */
function on_forever() {
    /** python code modules are defined by indenting */
    basic.showIcon(IconNames.Heart, 750)
    basic.showIcon(IconNames.SmallHeart, 350)
}

// basic.forever(on_forever)
// 6 wukong extention - use Neopixel lights on board
/** Available for Neopixel database	Connect to micro:bit P16 port */
// similator on Pin.P0, or Pin.P1
let strip = neopixel.create(DigitalPin.P0, 4, NeoPixelMode.RGB)
strip.setPixelColor(0, NeoPixelColors.Violet)
strip.setPixelColor(1, NeoPixelColors.Green)
strip.setPixelColor(2, NeoPixelColors.Red)
strip.setPixelColor(3, NeoPixelColors.Yellow)
strip.show()
// 7 Use input buttons to control neopixel lights
//  use the global strip object with button inputs
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    strip.setPixelColor(0, NeoPixelColors.Indigo)
    strip.setPixelColor(1, NeoPixelColors.Indigo)
    strip.setPixelColor(2, NeoPixelColors.Indigo)
    strip.setPixelColor(3, NeoPixelColors.Indigo)
    strip.show()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    strip.setPixelColor(0, NeoPixelColors.Black)
    strip.setPixelColor(1, NeoPixelColors.Black)
    strip.setPixelColor(2, NeoPixelColors.Black)
    strip.setPixelColor(3, NeoPixelColors.Black)
    strip.show()
})
