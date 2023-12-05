import sys
import time

from core.objects import app, win

x = 100
y = 100
while True:
    win.paintEvent("")
    print(win.objects[0].x)
    win.objects[0].x += 100
    win.objects[0].y += 100



    x = input()
    if x == "a":
        break