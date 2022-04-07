input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    game.addScore(10)
    health += 2
})
input.onButtonPressed(Button.B, function () {
    game.removeLife(5)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Sad)
    game.addScore(-5)
    health += -1
})
game.setLife(99)
basic.showIcon(IconNames.Asleep)
let health = 10
basic.forever(function () {
    if (health > 0) {
        basic.pause(3600000)
        health += -1
    }
})
basic.forever(function () {
    if (health > 6) {
        basic.showIcon(IconNames.Happy)
    }
    if (health <= 6) {
        basic.showIcon(IconNames.Confused)
    }
    if (health <= 3) {
        basic.showIcon(IconNames.Sad)
    }
    if (health <= 0) {
        basic.showIcon(IconNames.Skull)
        game.removeLife(95)
    }
})
