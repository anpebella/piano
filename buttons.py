from pygame import*
from settings import *

init()

class Button:
    def __init__(self, x, y, width, height, text,img1,img2, action=None):
        self.rect = Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.img_idle = img1
        self.img_hover = img2
        self.text_color = black

    def draw(self, screen, font):
        mouse_pos = mouse.get_pos()
        # підсвітка при наведенні
        if self.rect.collidepoint(mouse_pos):
             img = self.img_hover
        else:
             img=self.img_idle
        screen.blit(img,(self.rect.topleft))

        # текст кнопки
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos) and self.action:
                self.action()
