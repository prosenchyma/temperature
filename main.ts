input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let temp = input.temperature()
    basic.showNumber(temp)
})
