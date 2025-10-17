from pygame import *
from settings import white, window_height, window_width, keys
from keys import create_but, blit_rect
from sounds import load_sounds

init()
win = display.set_mode((window_width, window_height))
clock = time.Clock()

pressed=set()
rects = create_but()
sounds=load_sounds(keys)
keys_list=list(keys.keys())

running = True
while running:
    x, y = mouse.get_pos()

    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type==KEYDOWN:
            k=key.name(e.key)
            if k in sounds:
                sounds[k].play()
                pressed.add(keys_list.index(k))
        if e.type==KEYUP:
            k=key.name(e.key)
            if k in keys:
                pressed.discard(keys_list.index(k))
        if e.type==MOUSEBUTTONDOWN:
            for i,rect in enumerate(rects):
                if rect.collidepoint(x,y):
                    sounds[keys_list[i]].play()
                    pressed.add(i)
        if e.type==MOUSEBUTTONUP:
            for i, rect in enumerate(rects):
                if i in pressed and rect.collidepoint(x,y):
                    pressed.discard(i)

    win.fill(white)
    blit_rect(win, rects,pressed)
    display.update()
    clock.tick(60)

quit()