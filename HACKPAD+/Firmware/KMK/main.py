from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
import board

keyboard = KMKKeyboard()

# ---- MATRIX PINS ----
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP1, board.GP2, board.GP4, board.GP6)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ---- MEDIA EXTENSION ----
keyboard.extensions.append(MediaKeys())

# ---- ENCODERS ----
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

# Encoder 1 → Volume
# Encoder 2 → Brightness
encoder_handler.pins = (
    ((board.GP7, board.GP0, None),),   # Encoder 1
    ((board.GP29, board.GP3, None),),  # Encoder 2
)

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),   # Encoder 1
    ((KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP),),  # Encoder 2
]

# ---- MACROS ----
YOUTUBE = KC.LGUI(KC.R)  # Windows+R
SCREENSHOT = KC.LGUI(KC.PRINT_SCREEN)

keyboard.keymap = [
    [
        KC.LCTL(KC.C),      # Copy
        KC.LCTL(KC.V),      # Paste
        KC.DELETE,          # Delete

        SCREENSHOT,         # Screenshot
        KC.PRINT_SCREEN,    # Print Screen
        YOUTUBE,            # Open Run (type youtube.com)

        KC.LCTL(KC.X),      # Cut
        KC.LCTL(KC.Z),      # Undo
        KC.LCTL(KC.Y),      # Redo

        KC.LGUI(KC.E),      # File Explorer
        KC.LALT(KC.F4),     # Close Window
        KC.NO               # extra slot
    ]
]

if __name__ == '__main__':
    keyboard.go()
