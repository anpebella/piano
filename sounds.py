from pygame import mixer

def load_sounds(keys):
    sounds = {}
    for k in keys:
        try:
            sounds[k] = mixer.Sound(keys[k])
        except Exception as e:
            print(f"Не вдалося завантажити звук для клавіші '{k}': {e}")
    return sounds