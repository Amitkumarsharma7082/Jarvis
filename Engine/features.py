import pygame
import eel

# frontend access the backend function
@eel.expose
def playAssistantSound():
    pygame.mixer.init()
    pygame.mixer.music.load("www/assets/audio/start_sound.mp3")
    pygame.mixer.music.play()
