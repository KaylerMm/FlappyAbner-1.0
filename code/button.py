import pygame as pg
class Button():
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw(self, position, screen):
        action = False
        
        if self.rect.collidepoint(position):
            if pg.mouse.get_pressed()[0] == 1:
                action = True
                
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action