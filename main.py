def on_button_pressed_a():
    global next2
    if next2 == 1:
        next2 += 1
    else:
        next2 = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global next2
    if next2 == 0:
        next2 += 1
    else:
        next2 = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global next2, game_index
    if next2 == 2:
        next2 = 0
        game_index += 1
    else:
        next2 = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    if game_index == 1:
        basic.show_string("yay")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

game_index = 0
next2 = 0
games = ["name", "shake"]
next2 = 0
game_index = 0

def on_forever():
    global game_index
    if game_index == len(games):
        game_index = 0
    if game_index == 0:
        basic.show_string("retronbv")
    if game_index == 1:
        basic.show_string("s")
basic.forever(on_forever)
