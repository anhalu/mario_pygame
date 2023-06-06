import  pygame
import os
import pygame.mixer
pygame.mixer.init()
bgX= 0
# sound
s_powerdown = pygame.mixer.Sound(os.path.join('Sounds', 'powerdown.wav'))
s_stomp = pygame.mixer.Sound(os.path.join('Sounds', 'stomp.wav'))
s_bump = pygame.mixer.Sound(os.path.join('Sounds', 'bump.wav'))
s_kick = pygame.mixer.Sound(os.path.join('Sounds', 'kick.wav'))
s_powerdown = pygame.mixer.Sound(os.path.join('Sounds', 'powerdown.wav'))
s_mario_die = pygame.mixer.Sound(os.path.join('Sounds', 'mario-die.wav'))
#
score = 0
#
ground_level = 200

f_1_3 = 185
f_2_4 = 169    # floor level - height for 1 & 3