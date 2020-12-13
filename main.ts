input.onButtonPressed(Button.A, function () {
    if (next == 1) {
        next += 1
    } else {
        next = 0
    }
})
input.onButtonPressed(Button.AB, function () {
    if (next == 0) {
        next += 1
    } else {
        next = 0
    }
})
input.onButtonPressed(Button.B, function () {
    if (next == 2) {
        next = 0
        game_index += 1
    } else {
        next = 0
    }
})
input.onGesture(Gesture.Shake, function () {
    if (game_index == 1) {
        basic.showString("yay")
    }
})
let game_index = 0
let next = 0
basic.showString("mga v1")
let games = ["name", "shake"]
next = 0
game_index = 0
basic.forever(function () {
    if (game_index == games.length) {
        game_index = 0
    }
    if (game_index == 0) {
        basic.showString("retronbv")
    }
    if (game_index == 1) {
        basic.showString("s")
    }
})
