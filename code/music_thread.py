import threading
import pygame as pg

def play_music():
    pg.mixer.init()
    pg.mixer.music.load('sounds/theme.mp3')
    pg.mixer.music.play(-1)
    
def play_death_sfx():
    sfx = pg.mixer.Sound('sounds/death_sfx.mp3')
    sfx.play()
    
def stop_music():
    pg.mixer.music.stop()
    
def start_music_thread():
    music_thread = threading.Thread(target= play_music)
    music_thread.start()
    
def start_sfx_thread():
    sfx = threading.Thread(target= play_death_sfx)
    sfx.start()
    
def stop_music_thread():
    stop_music()
    pg.mixer.quit()