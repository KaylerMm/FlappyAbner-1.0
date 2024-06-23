import pygame as pg
from pygame.sprite import Group

class Bird(pg.sprite.Sprite):
    def __init__(self, x, y) -> None:
        pg.sprite.Sprite.__init__(self)
        
        self.images = []
        self.index = 0
        self.counter = 0
        self.speed = 0
        
        for i in range(1,4):
            image = pg.image.load(f'images/fatty_abner{i}.png')
            self.images.append(image)
        
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y] # type: ignore
        self.click = False
        
        
    def update_bird(self, flying, game_over):
        
        if flying == True:
            # Gravity effect
            self.speed += 0.5
            
            if self.speed > 8:
                self.speed = 8
            
            if self.rect.bottom < 768:
                self.rect.y += int(self.speed)
                
        if game_over == False:
            
            # Flapping
            if pg.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                self.speed = -10
            
            # Falling
            if pg.mouse.get_pressed()[0] == 0:
                self.click = False
        
            # Animation
            self.counter += 1
            flap_cooldown = 5
            
            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
        
                if self.index >= len(self.images):
                    self.index = 0
            
                    self.image = self.images[self.index]
                
                # Bird rotation
                    self.image = pg.transform.rotate(self.images[self.index], self.speed * -2)
                else:
                    self.image = pg.transform.rotate(self.images[self.index], -90)

