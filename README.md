# XIAO Jiggler

Seeduino XIAO based Mouse Jiggler using Circuit Python.

### Install Instructions:
1. Download and extract `xiao_jiggler.zip` from [latest release](https://github.com/akhilharihar/xiao_jiggler/releases/latest)

2. Connect your Seeeduino XIAO to your PC and quickly short the RST pins twice. An external drive with name `Arduino` will appear on your PC.

3. Copy `jiggle.uf2` file to the `Arduino` drive. Your Seeduino XIAO will mount as a `CIRCUITPY` drive. Copy `code.py` and `boot.py` files to the `CIRCUITPY` drive.

3.  Unplug your board, and now it is ready to be used as a mouse jiggler.

By default, circuitpython programming mode (i.e., CIRCUITPY drive, USB serial) is disabled, and your board will show up only as a mouse to USB hosts. To re-enter programming mode, short pin 10 to the ground pin and reconnect to your PC.


Note: The `jiggler.uf2` firmware in this release is similar to the [Seeeduino XIAO KB](https://circuitpython.org/board/seeeduino_xiao_kb/) firmware, but will show up as a generic mouse instead of Seeeduino XIAO when connected to a PC.