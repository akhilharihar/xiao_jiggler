from digitalio import DigitalInOut, Direction, Pull
import board
import time
import usb_hid
from adafruit_hid.mouse import Mouse

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

btn_usb_state = DigitalInOut(board.D10)
btn_usb_state.direction = Direction.INPUT
btn_usb_state.pull = Pull.UP

led.value = not btn_usb_state.value

mouse = Mouse(usb_hid.devices)
delta = 2

while True:
    if btn_usb_state.value:
        mouse.move(delta)
        time.sleep(1)
        mouse.move(-delta)
        time.sleep(1)
