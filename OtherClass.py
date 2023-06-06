import pygame
import os
import sys
import  constant

pygame.init()

# Heading coin
t_coins_i = [pygame.image.load(os.path.join('Images', 'Items', 'coins', 'title coin icon', 't_coin_1.png')),
             pygame.image.load(os.path.join('Images', 'Items', 'coins', 'title coin icon', 't_coin_2.png')),
             pygame.image.load(os.path.join('Images', 'Items', 'coins', 'title coin icon', 't_coin_3.png'))]


# pipes
pipes = [pygame.image.load(os.path.join('Images', 'Items', 'pipes', 'p1.png')),
         pygame.image.load(os.path.join('Images', 'Items', 'pipes', 'p2.png')),
         pygame.image.load(os.path.join('Images', 'Items', 'pipes', 'p3.png'))]

# floor block
floor_blocks = pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'floor_block.png'))

# brick
bricks = pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block.png'))
brick_break_pieces = [pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p1.png')),
                      pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p2.png')),
                      pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p3.png')),
                      pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'brick_block_break_p4.png'))]

# mystery boxes
mystery_boxes = [pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'coin_box_1.png')),
                 pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'coin_box_2.png')),
                 pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'coin_box_3.png'))]

# empty box
empty_box = pygame.image.load(os.path.join('Images', 'Items', 'blocks', 'empty_box.png'))

# coins
coins_i = [pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_1.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_2.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_3.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'coins', 'coin_4.png'))]

# mushroom
mushroom = pygame.image.load(os.path.join('Images', 'Items', 'mushroom', 'mushroom.png'))

# 1up mushroom
l_mushroom = pygame.image.load(os.path.join('Images', 'Items', '1up', '1up.png'))

# flower
flowers = [pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_1.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_2.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_3.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'flower', 'flower_4.png'))]

# flag
pole_i = pygame.image.load(os.path.join('Images', 'Items', 'flags', 'pole.png'))
cloth_i = pygame.image.load(os.path.join('Images', 'Items', 'flags', 'flag.png'))
victory_flag = pygame.image.load(os.path.join('Images', 'Items', 'flags', 'victory_flag.png'))

# castle
castle = pygame.image.load(os.path.join('Images', 'Items', 'castle', 'castle1.png'))


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------PIPE CLASS--------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class pipe:
    def __init__(self, x, level):
        self.x = x
        self.y = 168
        self.width = 32
        self.height = 32
        self.level = level
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        if self.level == 1:
            self.y = 168
            self.height = 32
            win.blit(pipes[0], (self.x + constant.bgX, self.y))
        if self.level == 2:
            self.y = 152
            self.height = 48
            win.blit(pipes[1], (self.x + constant.bgX, self.y))
        if self.level == 3:
            self.y = 136
            self.height = 64
            win.blit(pipes[2], (self.x + constant.bgX, self.y))
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------HOLE CLASS--------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

class hole:
    def __init__(self, x, width):
        self.x = x
        self.width = width


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------FLOOR BLOCK CLASS----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class floor_block:
    def __init__(self, x, y, hb):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.hb = hb
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(floor_blocks, (self.x + constant.bgX, self.y))
        if self.hb == 1:
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        elif self.hb == 4:
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height*4)
        elif self.hb == 8:
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height*8)
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------BRICK BLOCK CLASS----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class brick:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.type = type
        self.empty = False
        self.coin_counter = 10
        self.block_push = False
        self.push_count = 4
        self.broken = False
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.broken and not self.type == 'c':
            win.blit(bricks, (self.x + constant.bgX, self.y))
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        if self.type == 'c':
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
            if not self.empty:
                win.blit(bricks, (self.x + constant.bgX, self.y))
            else:
                win.blit(empty_box, (self.x + constant.bgX, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

# chưa cắt
class broken_brick:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 8
        self.piece = piece
        if self.piece == 0 or self.piece == 1:
            self.fall_u = 8
        elif self.piece == 2 or self.piece == 3:
            self.fall_u = 6
        self.fall_lr = 5
        self.fall_d = 4

    def draw(self, win):
        win.blit(brick_break_pieces[self.piece], (self.x + constant.bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------MYSTERY BOX CLASS----------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class mystery_box:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.type = type
        self.empty = False
        self.block_push = False
        self.push_count = 3
        self.timer = 0
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        if not self.empty:
            if self.timer + 1 >= 45:
                self.timer = 0
            if self.timer <= 25:
                win.blit(mystery_boxes[0], (self.x + constant.bgX, self.y))
            elif 25 < self.timer <= 35:
                win.blit(mystery_boxes[1], (self.x + constant.bgX, self.y))
            elif 35 < self.timer <= 45:
                win.blit(mystery_boxes[2], (self.x + constant.bgX, self.y))
            self.timer += 1
        else:
            win.blit(empty_box, (self.x + constant.bgX, self.y))
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)


# --------------------------------------------------------------------------------------------------------------------- #
# ----------------------------------------------INVISIBLE BOX CLASS---------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class invisible_box:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.type = type
        self.empty = False
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        if self.empty:
            win.blit(empty_box, (self.x + constant.bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------FLAG CLASSES------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class pole:
    def __init__(self):
        self.x = 3173
        self.y = 32
        self.height = 152
        self. width = 8
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(pole_i, (self.x + constant.bgX, self.y))
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)


class cloth:
    def __init__(self):
        self.x = 3160
        self.y = 40
        self.height = 16
        self. width = 16
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(cloth_i, (self.x + constant.bgX, self.y))
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)


# --------------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------------CASTLE CLASS------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Castle:
    def __init__(self):
        self.x = 3232
        self.y = 120                                                                                                                  

    def draw(self, win):
        win.blit(castle, (self.x + constant.bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------VIC FLAG CLASS------------------------------------------------------ #
# --------------------------------------------------------------------------------------------------------------------- #


class v_Flag:
    def __init__(self):
        self.x = 3264
        self.y = 125

    def draw(self, win):
        win.blit(victory_flag, (self.x + constant.bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# ---------------------------------------------------COIN CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 0
        self.jump_h = 9

    def draw(self, win):
        if self.timer + 1 >= 24:
            self.timer = 0
        win.blit(coins_i[self.timer//6], (self.x + constant.bgX, self.y))
        self.timer += 1


class title_Coin:
    def __init__(self):
        self.x = 118
        self.y = 21
        self.timer = 0

    def draw(self, win):
        if self.timer + 1 >= 45:
            self.timer = 0
        if self.timer <= 25:
            win.blit(t_coins_i[0], (self.x, self.y))
        elif 25 < self.timer <= 35:
            win.blit(t_coins_i[1], (self.x, self.y))
        elif 35 < self.timer <= 45:
            win.blit(t_coins_i[2], (self.x, self.y))
        self.timer += 1


# --------------------------------------------------------------------------------------------------------------------- #
# ------------------------------------------------MUSHROOM CLASS------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Mushroom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.rise = True
        self.dir = 1
        self.switch = False
        self.fall_count = 1
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        win.blit(mushroom, (self.x + constant.bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------1UP MUSHROOM CLASS---------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class L_Mushroom:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.rise = True
        self.fall_count = 1
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        win.blit(l_mushroom, (self.x + constant.bgX, self.y))


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------FLOWER CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #


class Flower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.rise = True
        self.timer = 0
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        if self.timer + 1 >= 36:
            self.timer = 0
        win.blit(flowers[self.timer//9], (self.x + constant.bgX, self.y))
        self.timer += 1


# --------------------------------------------------------------------------------------------------------------------- #
# -------------------------------------------------BULLET CLASS-------------------------------------------------------- #
# --------------------------------------------------------------------------------------------------------------------- #

bullets = [pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b1.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b2.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b3.png')),
           pygame.image.load(os.path.join('Images', 'Items', 'Mario Bullets', 'b4.png'))]

b_hits = [pygame.image.load(os.path.join('Images', 'Items', 'Bullet hit', 'bh1.png')),
          pygame.image.load(os.path.join('Images', 'Items', 'Bullet hit', 'bh2.png')),
          pygame.image.load(os.path.join('Images', 'Items', 'Bullet hit', 'bh3.png'))]
class Bullet:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.width = 8
        self.height = 9
        self.dir = dir
        self.bounce_h = 7
        self.bounce = False
        self.hit = False
        self.timer_b = 0
        self.timer_h = 0
        self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)

    def draw(self, win):
        if not self.hit:
            if self.timer_b >= 36:
                self.timer_b = 0
            win.blit(bullets[self.timer_b//9], (self.x + constant.bgX, self.y))
            self.timer_b += 1
            self.hitBox = (self.x + constant.bgX, self.y, self.width, self.height)
        else:
            if self.timer_h < 26:
                self.timer_h += 1
                if 0 <= self.timer_h < 9:
                    win.blit(b_hits[0], (self.x + constant.bgX, self.y))
                elif 9 <= self.timer_h < 18:
                    win.blit(b_hits[1], (self.x - 2 + constant.bgX, self.y - 3))
                elif 18 <= self.timer_h < 26:
                    win.blit(b_hits[2], (self.x - 4 + constant.bgX, self.y - 4))

