from pygame import *
from settings import *
from effects import draw_key_effect

def create_but(num_keys,x=start_x, y=start_y, width=but_width, height=but_height):
    rects = []
    for key in range(num_keys):
        rect = Rect(x, y, width, height)
        x += 80
        rects.append(rect)
    return rects

def blit_rect(window, rects, pressed_rect,x,y):
    for i,rect in enumerate(rects):
        pressed=i in pressed_rect
        draw_key_effect(window,rect,x,y,i,pressed)
        rect_text = fonte.render(text[i], True, 'black')
        window.blit(rect_text,(rect.x+10,rect.y+100))

