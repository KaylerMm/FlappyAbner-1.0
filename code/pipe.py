import pygame as pg

class Pipe(pg.sprite.Sprite):
    def __init__(self, x, y, position, pipe_gap) -> None:
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load('images/pipe3.png')
        self.rect = self.image.get_rect()
        
        # Top
        if position == 1:
            self.image = pg.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pipe_gap / 2)] # type: ignore
        
        # Bottom
        if position == -1:
            self.rect.topleft = [x, y + int(pipe_gap / 2)] # type: ignore
            
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
        
        if self.rect.right < 0:
            self.kill()