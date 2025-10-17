from settings import act_color,white,black
from pygame import draw

def draw_key_effect(window,rect,pressed=False):
    if not pressed:
        base_color=white
    else:
        base_color=act_color
    border_color=black

    draw.rect(window,base_color,rect)
    draw.rect(window,border_color,rect,3)
