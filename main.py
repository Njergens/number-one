def on_button_pressed_a():
    basic.show_string("Welcome!")
    for index in range(4):
        basic.show_icon(IconNames.SMALL_HEART)
        basic.show_icon(IconNames.HEART)
    for index2 in range(3):
        basic.show_leds("""
            . . # . .
            . # . # .
            # . . . #
            . # . # .
            . . # . .
            """)
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
input.on_button_pressed(Button.A, on_button_pressed_a)
