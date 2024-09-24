import math
from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print("circle")

    cx, cy, r = 800 / 2, 600 / 2, 200
    for deg in range(0,360,5):
        x = cx + r * math.cos(deg/360 * 2 * math.pi)
        y = cy + r * math.sin(deg/360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        update_canvas()
        delay(0.01)
        get_events()


def run_rectangle():
    print("rectangle")

    for i in range (750 , 50-1, -10):
        x = i
        y = 540
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        delay(0.01)
        get_events()
    for i in range (540 , 80-1 , -10):
        x = 50
        y = i
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        delay(0.01)
        get_events()
    for i in range(50, 750 + 1, +10):
        x = i
        y = 80
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        delay(0.01)
        get_events()
    for i in range(80,540+1, +10):
        x = 750
        y = i
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        update_canvas()
        delay(0.01)
        get_events()
    pass

while True:
    run_rectangle()
    run_circle()

close_canvas()