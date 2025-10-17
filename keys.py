from pygame import *
from settings import *
from effects import draw_key_effect

def create_but(x=start_x, y=start_y, width=but_width, height=but_height):
    rects = []
    for key in keys.keys():
        rect = Rect(x, y, width, height)
        x += 90
        rects.append(rect)
    return rects


def blit_rect(window, rects, pressed_rect):
    for i,rect in enumerate(rects):
        pressed=i in pressed_rect
        draw_key_effect(window,rect,pressed)
