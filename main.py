def on_gesture_eight_g():
    basic.show_icon(IconNames.NO)
    game.remove_life(1)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_a():
    global health
    basic.show_icon(IconNames.HEART)
    game.add_score(10)
    health += 2
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.HAPPY)
    game.add_score(10)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global health
    basic.show_icon(IconNames.SAD)
    game.add_score(-5)
    health += -1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

game.set_life(3)
basic.show_icon(IconNames.ASLEEP)
health = 10

def on_forever():
    global health
    if health > 0:
        basic.pause(3600000)
        health += -1
basic.forever(on_forever)

def on_forever2():
    if health > 6:
        basic.show_icon(IconNames.HAPPY)
    if health <= 6:
        basic.show_icon(IconNames.CONFUSED)
    if health <= 3:
        basic.show_icon(IconNames.SAD)
    if health <= 0:
        basic.show_icon(IconNames.SKULL)
        basic.pause(3600000)
basic.forever(on_forever2)
