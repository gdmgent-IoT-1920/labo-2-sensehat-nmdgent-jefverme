from sense_hat import SenseHat
import time
import random

s = SenseHat()

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
P = (255,105, 180)

speed = float(input("snelheid"))

colors = [G, Y, B, R, W, P]
while True:
  s.clear()
  for x in range(8):
    for y in range(8):
      s.set_pixel(x, y, random.choice(colors))
      time.sleep(speed)
  