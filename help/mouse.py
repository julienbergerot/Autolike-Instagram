from pynput.mouse import Button, Controller
import time

time.sleep(2)
mouse = Controller()

print(mouse.position)