def on_gesture_shake():
    temp = input.temperature()
    basic.show_number(temp)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
