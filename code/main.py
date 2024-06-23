import pygame as pg
from bird import Bird
from pipe import Pipe
from button import Button
import random
from music_thread import start_music_thread, play_death_sfx

# Music
start_music_thread()
pg.mixer.init()

# Text style
pg.font.init()
FONT = pg.font.SysFont("Bauhaus 93", 60)
SCORE_COLOUR = (0, 0, 0) # Black

# Game inits
screen_width = 864
screen_height = 936

clock = pg.time.Clock()
fps = 60

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Flappy Abner')

# Scenario load
background = pg.image.load('images/puc_sg2.png')
ground = pg.image.load('images/ground.png')
button_image = pg.image.load('images/restart.png')

# Button
button = Button(screen_width // 2 - 50, screen_height // 2 - 100, button_image)

# Running variables
run = True
ground_scroll = 0
scroll_speed = 4
game_over = False
flying = False

pipe_gap = 200
pipe_frequency = 1500
last_pipe = pg.time.get_ticks()

score = 0
pass_pipe = False

# Bird init
bird_group = pg.sprite.Group()
abner = Bird(100, int(936 / 2))
bird_group.add(abner)

# Pipes init
pipes_group = pg.sprite.Group()

# Score
def draw_text(text, x, y):
    image = FONT.render(text, True, SCORE_COLOUR)
    screen.blit(image, (x, y))
    
def reset_game():
    pipes_group.empty()
    abner.rect.x = 100
    abner.rect.y = int(screen_height / 2)
    score = 0
    return score

while run:
    
    # Running speed
    clock.tick(fps)
    
    # Setting background
    screen.blit(background, (0,0))
    
    bird_group.draw(screen)
    bird_group.update()
    pipes_group.draw(screen)
    
    # Ground scroll
    screen.blit(ground, (ground_scroll, 768))
    
    # Score check
    if len(pipes_group) > 0:
        if bird_group.sprites()[0].rect.left > pipes_group.sprites()[0].rect.left \
        and bird_group.sprites()[0].rect.right < pipes_group.sprites()[0].rect.right \
        and pass_pipe == False:
            pass_pipe = True
            
        if pass_pipe == True:
            if bird_group.sprites()[0].rect.left > pipes_group.sprites()[0].rect.right:
                score += 1
                pass_pipe = False
                
    draw_text(str(score), int(screen_width / 2), 20)
    
    # Game Over (pipes collision)
    if pg.sprite.groupcollide(bird_group, pipes_group, False, False) or abner.rect.top < 0:
        game_over = True
        play_death_sfx()
    
    # Game Over (ground hit)
    if abner.rect.bottom >= 768:
        game_over = True
        play_death_sfx()
        
        flying = False
        
        
    if game_over == False and flying == True:
        
        # Pipes generation
        time = pg.time.get_ticks()
        if time - last_pipe > pipe_frequency:
            pipe_height = random.randint(-100, 100)
            bottom_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1, pipe_gap) 
            top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1, pipe_gap)
            pipes_group.add(bottom_pipe)
            pipes_group.add(top_pipe)
            last_pipe = time
        
        # Resets ground scroll when ground img ends
        ground_scroll -= scroll_speed
        if abs(ground_scroll) > 35:
            ground_scroll = 0
            
        pipes_group.update(scroll_speed)
        
    if game_over == True:
        mouse_position = pg.mouse.get_pos()
        if button.draw(mouse_position, screen) == True:
            game_over = False
            score = reset_game()
    
    # Ends game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            
        if event.type == pg.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True
    
    abner.update_bird(flying, game_over)
    pg.display.update()
        
pg.quit()