import board
import storage
import touchio

USB_access = False

# Capacitive touch on D3
touch = touchio.TouchIn(board.D3)

# Test printing to Boot.txt
if (touch.raw_value > 3000):
    print("Pin Touched", end="\t")
    USB_access = not USB_access
print("A2 touch: %d" % touch.raw_value, end="\t")

# If the touch pin is touched during boot-up (USB_access = True) CircuitPython can write to the drive via USB (Mu, etc.)
# If the touch pin is not touched during boot-up (USB_access = False) CircuitPython can write to the drive from program code
storage.remount("/", USB_access)