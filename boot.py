from digitalio import DigitalInOut, Direction, Pull
import board
import storage
import usb_midi
import usb_cdc
import usb_hid

btn_usb_state = DigitalInOut(board.D10)
btn_usb_state.direction = Direction.INPUT
btn_usb_state.pull = Pull.UP

if btn_usb_state.value:
    # Executed when button at pin 10 is pressed
    print("Developer mode disabled")
    storage.disable_usb_drive()
    usb_cdc.disable()
    usb_midi.disable()
    usb_hid.enable((usb_hid.Device.MOUSE))
else:
    print("Developer mode enabled")
