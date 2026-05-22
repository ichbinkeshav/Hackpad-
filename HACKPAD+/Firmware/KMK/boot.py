import board
import digitalio
import storage
import usb_cdc
import usb_hid
import time

# ---- MATRIX PINS ----
cols = [board.GP26, board.GP27, board.GP28]  # C1 C2 C3
rows = [board.GP1, board.GP2, board.GP4, board.GP6]  # R1 R2 R3 R4

# Setup columns as input pullups
col_ios = []
for pin in cols:
    col = digitalio.DigitalInOut(pin)
    col.direction = digitalio.Direction.INPUT
    col.pull = digitalio.Pull.UP
    col_ios.append(col)

# Setup rows as output low
row_ios = []
for pin in rows:
    row = digitalio.DigitalInOut(pin)
    row.direction = digitalio.Direction.OUTPUT
    row.value = False
    row_ios.append(row)

time.sleep(0.1)

key_pressed = False

# Scan matrix once
for row in row_ios:
    row.value = False
    for col in col_ios:
        if not col.value:  # Active LOW
            key_pressed = True
    row.value = True

if key_pressed:
    # SAFE MODE (no keyboard)
    storage.enable_usb_drive()
    usb_hid.disable()
else:
    # Normal keyboard mode
    storage.disable_usb_drive()
