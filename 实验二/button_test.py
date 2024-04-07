from gpiozero import LED,Button
from time import sleep
from signal import pause

led = LED(3)
button = Button(12)

button.when_pressed = led.off
button.when_released = led.on

pause()
# while True:
#     if button.is_pressed:
#         print("Button is pressed")
#     else:
#         print("Button is not pressed")
#     sleep(1)