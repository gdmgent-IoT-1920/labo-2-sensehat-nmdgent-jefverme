from sense_hat import SenseHat
import time
import random

s = SenseHat()
s.low_light = True

G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
P = (255,105, 180)

colors = [G, Y, B, R, W, P]
displayString = "Hello! We are New Media Development :)"
while True:
  s.show_message(displayString, text_colour = random.choice(colors), back_colour = random.choice(colors))
  