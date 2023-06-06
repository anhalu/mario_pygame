import pygame
import os
import sys
import constant
pygame.init()

# goomba
goomba = [pygame.image.load(os.path.join('Images', 'Enemies', 'goomba', 'g1.png')),
          pygame.image.load(os.path.join('Images', 'Enemies', 'goomba', 'g2.png'))]
inv_goomba = pygame.transform.rotate(goomba[0], 180)
squished_goomba = pygame.image.load(os.path.join('Images', 'Enemies', 'goomba', 'dead.png'))

# koopa troopa
koopa_troopa_L = [pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'l1.png')),
                  pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'l2.png'))]
koopa_troopa_R = [pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'r1.png')),
                  pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'r2.png'))]
koopa_troopa_shell = [pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'shell_mid.png')),
                     pygame.image.load(os.path.join('Images', 'Enemies', 'koopa troopa', 'shell.png'))]
inv_koopa_troopa = pygame.transform.rotate(koopa_troopa_shell[1], 180)


class Goomba:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.move = False
        self.dir = -1
        self.switch = False
        self.fall_count = 1
        self.walkCount = 0
        self.hit = False
        self.squished = False
        self.dis_time = 0
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.hit and not self.squished:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0
            win.blit(goomba[self.walkCount//15], (self.x + constant.bgX, self.y))
            self.walkCount += 1
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        else:
            if self.squished:
                win.blit(squished_goomba, (self.x + constant.bgX, self.y))
            elif self.hit:
                win.blit(inv_goomba, (self.x + constant.bgX, self.y))


class Koopa_Troopa:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 24
        self.move = False
        self.dir = -1
        self.switch = False
        self.fall_count = 1
        self.walkCount = 0
        self.hit = False
        self.hole_coll = False
        self.shell = False
        self.shell_tr_timer = 0
        self.shell_stop = False
        self.shell_slide = False
        self.goom_domino = 0
        self.dis_time = 0
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.hit and not self.shell:
            if self.walkCount + 1 >= 30:
                self.walkCount = 0
            win.blit(koopa_troopa_L[self.walkCount//15], (self.x + constant.bgX, self.y))
            self.walkCount += 1
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        else:
            self.hitBox = (self.x + constant.bgX, self.y, self.width, 16)
            if self.shell and not self.hit:
                if self.shell_tr_timer <= 10:
                    win.blit(koopa_troopa_shell[0], (self.x + constant.bgX, self.y + 1))
                    self.shell_tr_timer += 1
                else:
                    win.blit(koopa_troopa_shell[1], (self.x + constant.bgX, self.y + 1))
            elif self.hit:
                win.blit(inv_koopa_troopa, (self.x + constant.bgX, self.y))
