from settings import act_color,white,black
from pygame import draw

def draw_key_effect(window,rect,x,y,index=0,pressed=False):
    if not pressed:
        base_color=img[index]
    if pressed or rect.collidepoint(x,y):
        base_color=hover[index]
    window.blit(base_color,(rect.x,rect.y))

