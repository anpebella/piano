from pygame import *
from settings import *
from keys import create_but, blit_rect
from sounds import load_sounds
from buttons import Button
from settings_menu import SettingsMenu

init()
win = display.set_mode((window_width, window_height))
clock = time.Clock()

pressed=set()

sounds=load_sounds(keys)
num_keys=len(keys)
keys_list = list(keys.keys())[:num_keys]
rects = create_but(num_keys)
screen_mode='main'
settings_menu=None
current_volume=1.0

def apply_settings(volume: float, key_count: int):
    global current_volume, num_keys, keys_list, rects, pressed
    current_volume = float(max(0.0, min(1.0, volume)))
    for s in sounds.values():
        try:
            s.set_volume(current_volume)
        except Exception:
            pass
    key_count = max(1, min(len(keys), int(key_count)))
    if key_count != num_keys:
        num_keys = key_count
        keys_list = list(keys.keys())[:num_keys]
        rects = create_but(num_keys)
        # прибрати "зажаті" індекси, яких більше немає
        pressed = {i for i in pressed if i < num_keys}

def _back_to_main():
    global screen_mode, settings_menu
    screen_mode = "main"
    settings_menu = None

def open_settings():
    global screen_mode, settings_menu
    screen_mode = "settings"
    settings_menu = SettingsMenu(
        win.get_rect(),
        initial_volume=current_volume,
        initial_keys=num_keys,
        min_keys=1,
        max_keys=len(keys),
        on_change=apply_settings,
        on_back=lambda: _back_to_main(),
    )
set_rect=Button(10,10,50,50,'',set_img,set_hover,open_settings)

running = True
while running:
    x, y = mouse.get_pos()
    win.fill(white)

    for e in event.get():
        if e.type == QUIT:
            running = False
        if screen_mode == "settings" and settings_menu:
            settings_menu.handle_event(e)
        else:
            set_rect.handle_event(e)
            if e.type == KEYDOWN:
                k = key.name(e.key)
                if k in sounds:
                    sounds[k].play()
                    pressed.add(keys_list.index(k))
            if e.type == KEYUP:
                k = key.name(e.key)
                if k in keys:
                    pressed.discard(keys_list.index(k))
            if e.type == MOUSEBUTTONDOWN:
                for i, rect in enumerate(rects):
                    if rect.collidepoint(x, y):
                        sounds[keys_list[i]].play()
                        pressed.add(i)
            if e.type == MOUSEBUTTONUP:
                for i, rect in enumerate(rects):
                    if i in pressed and rect.collidepoint(x, y):
                        pressed.discard(i)
    if screen_mode == "settings" and settings_menu:
        settings_menu.draw(win, fonte)
    else:
        blit_rect(win, rects, pressed,x,y)
        set_rect.draw(win, fonte)
    display.update()
    clock.tick(60)

quit()


quit()
