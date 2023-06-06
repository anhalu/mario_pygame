import pygame
import os
import sys
import constant
pygame.init()

# Mario Walk
walkLeftM1 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1walking3.png'))]
walkLeftM2 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2walking3.png'))]
walkLeftM3 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3walking3.png'))]
walkLeftM4 = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4walking1.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4walking2.png')),
              pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4walking3.png'))]
walkRightM1 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1walking3.png'))]
walkRightM2 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2walking3.png'))]
walkRightM3 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3walking3.png'))]
walkRightM4 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4walking1.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4walking2.png')),
               pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4walking3.png'))]

# Mario Jump
jump_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1jumping.png'))
jump_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2jumping.png'))
jump_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3jumping.png'))
jump_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4jumping.png'))
jump_R_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1jumping.png'))
jump_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2jumping.png'))
jump_R_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3jumping.png'))
jump_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4jumping.png'))

# Mario Standing
stand_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1standing.png'))
stand_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2standing.png'))
stand_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3standing.png'))
stand_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4standing.png'))
stand_R_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1standing.png'))
stand_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2standing.png'))
stand_R_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3standing.png'))
stand_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4standing.png'))

# Mario Face_Switch
face_switch_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'l1switch.png'))
face_switch_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2switch.png'))
face_switch_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'l3switch.png'))
face_switch_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4switch.png'))
face_switch_R_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'r1switch.png'))
face_switch_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2switch.png'))
face_switch_R_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'r3switch.png'))
face_switch_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4switch.png'))

# Mario Death
death_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Mid', '1', '1death.png'))
death_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Mid', '3', '3death.png'))

# Mario Duck
duck_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2duck.png'))
duck_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4duck.png'))
duck_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2duck.png'))
duck_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4duck.png'))

# Mario Smaller
smaller_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'l2smaller.png'))
smaller_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'l4smaller.png'))
smaller_R_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'r2smaller.png'))
smaller_R_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'r4smaller.png'))

# Mario Flag Rappelling
rappelling_L_M1 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '1', 'flag', 'l1flag1.png'))
rappelling_L_M2 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '2', 'flag', 'l2flag1.png'))
rappelling_L_M3 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '3', 'flag', 'l3flag1.png'))
rappelling_L_M4 = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'flag', 'l4flag1.png'))
rappelling_R_M1 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'flag', 'r1flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '1', 'flag', 'r1flag2.png'))]
rappelling_R_M2 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'flag', 'r2flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '2', 'flag', 'r2flag2.png'))]
rappelling_R_M3 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'flag', 'r3flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '3', 'flag', 'r3flag2.png'))]
rappelling_R_M4 = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'flag', 'r4flag1.png')),
                   pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'flag', 'r4flag2.png'))]

# Mario Shooting
walkLeftM4_s = [pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4swalking1.png')),
                pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4swalking2.png')),
                pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4swalking3.png'))]
walkRightM4_s = [pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4swalking1.png')),
                 pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4swalking2.png')),
                 pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4swalking3.png'))]

jump_L_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4sjumping.png'))
jump_R_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4sjumping.png'))

face_switch_L_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Left', '4', 'shoot', 'l4sswitch.png'))
face_switch_R_M4_s = pygame.image.load(os.path.join('Images', 'Mario', 'Right', '4', 'shoot', 'r4sswitch.png'))


class Mario:
    def __init__(self):
        self.x = 40
        self.y = 185
        self.width = 16
        self.height = 17
        self.ground_level = 185
        self.vel = 2.6
        self.pot_en = 0
        self.walkCount = 0
        self.jump_count_up = 10
        self.jump_count_down = 0
        self.falling_count = 1
        self.level = 1
        self.lives = 3
        self.face_switch_timer = 0
        self.grow_time = 0
        self.shrink_time = 0
        self.blink_timer = 0
        self.squish_streak = 0
        self.rap_count = 0
        self.right = True
        self.left = False
        self.standing = True
        self.collide_l = False
        self.collide_r = False
        self.game_over = False
        self.death = False
        self.hole_falling = False
        self.reset = False
        self.face_switch = False
        self.isJump = False
        self.duck = False
        self.grow = False
        self.shrink = False
        self.blink = False
        self.shoot = False
        self.rappelling = False
        self.rap_switch = False
        self.end_jump = False
        self.end_walk = False
        self.end_m = False
        self.dis = False
        self.hitBox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        if self.walkCount + 1 >= 18:
            self.walkCount = 0
        if self.rap_count + 1 >= 20:
            self.rap_count = 0

        if self.level == 1 or self.level == 3:
            self.ground_level = constant.f_1_3
            if not self.isJump and self.pot_en == 0 and not self.death and not self.hole_falling and not self.end_m:
                self.y = constant.f_1_3
            self.width = 16
            self.height = 17
            self.hitBox = (self.x, self.y, self.width, self.height - 1)
        else:
            self.ground_level = constant.f_2_4
            if not self.isJump and self.pot_en == 0 and not self.hole_falling and not self.end_m:
                self.y = constant.f_2_4
            self.width = 16
            self.height = 32
            self.hitBox = (self.x, self.y, self.width, self.height)

        if self.level == 1:
            if self.grow:
                if self.grow_time <= 100:
                    if self.left:
                        if 0 < self.grow_time <= 20 or 40 < self.grow_time <= 60 or 80 < self.grow_time <= 100:
                            win.blit(smaller_L_M2, (self.x, self.y - 16))
                        if 20 < self.grow_time <= 40 or 60 < self.grow_time <= 80:
                            win.blit(stand_L_M2, (self.x, self.y - 16))
                    elif self.right:
                        if 0 < self.grow_time <= 20 or 40 < self.grow_time <= 60 or 80 < self.grow_time <= 100:
                            win.blit(smaller_R_M2, (self.x, self.y - 16))
                        if 20 < self.grow_time <= 40 or 60 < self.grow_time <= 80:
                            win.blit(stand_R_M2, (self.x, self.y - 16))
                    self.grow_time += 2.5
                else:
                    self.level += 1
                    self.y -= 16
                    self.grow_time = 0
                    self.grow = False
            if self.rappelling:
                win.blit(rappelling_R_M1[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M1[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M1, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M1, (self.x, self.y))
                        else:
                            win.blit(walkRightM1[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.death:
                    win.blit(death_M1, (self.x, self.y))
                elif self.isJump and not self.grow:
                    if self.left:
                        win.blit(jump_L_M1, (self.x, self.y))
                    elif self.right:
                        win.blit(jump_R_M1, (self.x, self.y))
                else:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_R_M1, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_L_M1, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        if not self.face_switch:
                            if self.left:
                                win.blit(walkLeftM1[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                win.blit(walkRightM1[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    elif not self.grow:
                        if self.right:
                            win.blit(stand_R_M1, (self.x, self.y))
                        else:
                            win.blit(stand_L_M1, (self.x, self.y))

        if self.level == 2:
            if self.shrink:
                if self.shrink_time <= 100:
                    if self.left:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_L_M2, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_L_M1, (self.x, self.y + 16))
                    elif self.right:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_R_M2, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_R_M1, (self.x, self.y + 16))
                    self.shrink_time += 3
                else:
                    self.level -= 1
                    self.y += 16
                    self.shrink_time = 0
                    self.shrink = False
            if self.rappelling:
                win.blit(rappelling_R_M2[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M2[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M2, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M2, (self.x, self.y))
                        else:
                            win.blit(walkRightM2[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.isJump and not self.duck:
                    if self.left:
                        win.blit(jump_L_M2, (self.x, self.y))
                    elif self.right:
                        win.blit(jump_R_M2, (self.x, self.y))
                elif not self.isJump and not self.duck:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_R_M2, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_L_M2, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        if not self.face_switch:
                            if self.left:
                                win.blit(walkLeftM2[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                win.blit(walkRightM2[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    elif not self.shrink:
                        if self.right:
                            win.blit(stand_R_M2, (self.x, self.y))
                        else:
                            win.blit(stand_L_M2, (self.x, self.y))
                if self.duck:
                    self.standing = False
                    if self.left:
                        win.blit(duck_L_M2, (self.x, self.y))
                    elif self.right:
                        win.blit(duck_R_M2, (self.x, self.y))
                    self.duck = False

        if self.level == 3:
            if self.rappelling:
                win.blit(rappelling_R_M3[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M3[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M3, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M3, (self.x, self.y))
                        else:
                            win.blit(walkRightM3[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.death:
                    win.blit(death_M3, (self.x, self.y))
                elif self.isJump:
                    if self.left:
                        win.blit(jump_L_M3, (self.x, self.y))
                    elif self.right:
                        win.blit(jump_R_M3, (self.x, self.y))
                else:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_R_M3, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                win.blit(face_switch_L_M3, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                        if not self.face_switch:
                            if self.left:
                                win.blit(walkLeftM3[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                win.blit(walkRightM3[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    else:
                        if self.right:
                            win.blit(stand_R_M3, (self.x, self.y))
                        else:
                            win.blit(stand_L_M3, (self.x, self.y))

        if self.level == 4:
            if self.shrink:
                if self.shrink_time <= 100:
                    if self.left:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_L_M4, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_L_M3, (self.x, self.y + 16))
                    elif self.right:
                        if 0 < self.shrink_time <= 20 or 40 < self.shrink_time <= 60 or 80 < self.shrink_time <= 100:
                            win.blit(smaller_R_M4, (self.x, self.y))
                        if 20 < self.shrink_time <= 40 or 60 < self.shrink_time <= 80:
                            win.blit(stand_R_M3, (self.x, self.y + 16))
                    self.shrink_time += 3
                else:
                    self.level -= 1
                    self.y += 16
                    self.shrink_time = 0
                    self.shrink = False
            if self.rappelling:
                win.blit(rappelling_R_M4[self.rap_count//10], (self.x, self.y))
                self.rap_count += 1
            elif self.end_m:
                if not self.rap_switch:
                    win.blit(rappelling_R_M4[0], (self.x, self.y))
                else:
                    if not self.end_jump and not self.end_walk:
                        win.blit(rappelling_L_M4, (self.x, self.y))
                    else:
                        if not self.end_walk:
                            win.blit(jump_L_M4, (self.x, self.y))
                        else:
                            win.blit(walkRightM4[self.walkCount // 6], (self.x, self.y))
                            self.walkCount += 1
            else:
                if self.isJump and not self.duck:
                    if self.left:
                        if self.shoot:
                            for x in range(300):
                                win.blit(jump_L_M4_s, (self.x, self.y))
                                pygame.display.update()
                            self.shoot = False
                        else:
                            win.blit(jump_L_M4, (self.x, self.y))
                    elif self.right:
                        if self.shoot:
                            for x in range(300):
                                win.blit(jump_R_M4_s, (self.x, self.y))
                                pygame.display.update()
                            self.shoot = False
                        else:
                            win.blit(jump_R_M4, (self.x, self.y))
                elif not self.isJump and not self.duck:
                    if not self.standing:
                        if self.face_switch and self.left:
                            if self.face_switch_timer + 1 <= 6:
                                if self.shoot:
                                    win.blit(face_switch_R_M4_s, (self.x, self.y))
                                else:
                                    win.blit(face_switch_R_M4, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                                self.shoot = False
                        elif self.face_switch and self.right:
                            if self.face_switch_timer + 1 <= 6:
                                if self.shoot:
                                    win.blit(face_switch_L_M4_s, (self.x, self.y))
                                else:
                                    win.blit(face_switch_L_M4, (self.x, self.y))
                                self.face_switch_timer += 1
                            else:
                                self.face_switch_timer = 0
                                self.face_switch = False
                                self.shoot = False
                        if not self.face_switch:
                            if self.left:
                                if self.shoot:
                                    for x in range(200):
                                        win.blit(walkLeftM4_s[self.walkCount // 6], (self.x, self.y))
                                        pygame.display.update()
                                    self.shoot = False
                                else:
                                    win.blit(walkLeftM4[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                            elif self.right:
                                if self.shoot:
                                    for x in range(200):
                                        win.blit(walkRightM4_s[self.walkCount // 6], (self.x, self.y))
                                        pygame.display.update()
                                    self.shoot = False
                                else:
                                    win.blit(walkRightM4[self.walkCount // 6], (self.x, self.y))
                                self.walkCount += 2
                    elif not self.shrink:
                        if self.right:
                            if self.shoot:
                                for x in range(500):
                                    win.blit(walkRightM4_s[2], (self.x, self.y))
                                    pygame.display.update()
                                self.shoot = False
                            else:
                                win.blit(stand_R_M4, (self.x, self.y))
                        else:
                            if self.shoot:
                                for x in range(500):
                                    win.blit(walkLeftM4_s[2], (self.x, self.y))
                                    pygame.display.update()
                                self.shoot = False
                            else:
                                win.blit(stand_L_M4, (self.x, self.y))
                if self.duck:
                    self.standing = False
                    if self.left:
                        win.blit(duck_L_M4, (self.x, self.y))
                    elif self.right:
                        win.blit(duck_R_M4, (self.x, self.y))
                    self.duck = False
        #pygame.draw.rect(win, (255, 0, 0), self.hitBox, 2)

    def land(self, obj):
        self.pot_en = obj.hitBox[3]
        if self.hitBox[1] + self.hitBox[3] > obj.hitBox[1]:
            if self.level == 1 or self.level == 3:
                self.y = obj.hitBox[1] - self.height + 1
            else:
                self.y = obj.hitBox[1] - self.height
            self.collide_r = False
            self.collide_l = False
            self.isJump = False
            self.standing = True
            self.jump_count_up = 10
            self.jump_count_down = 0

    def collide(self, obj):
        if obj.hitBox[0] < self.hitBox[0] < obj.hitBox[0] + obj.hitBox[2]:
            self.collide_l = True
        elif obj.hitBox[0] + obj.hitBox[2] > self.hitBox[0] + self.hitBox[2] > obj.hitBox[0]:
            self.collide_r = True

    def fall(self):
        if self.pot_en and not self.isJump:
            if self.y < self.ground_level:
                self.y += (self.falling_count ** 2) / 10
                self.falling_count += 0.5
            else:
                self.pot_en = 0
                self.falling_count = 1

    def enemy_damage(self):
        if self.level == 1 or self.level == 3:
            constant.s_mario_die.play()
            self.death = True
        elif self.level == 2 or self.level == 4:
            self.shrink = True

    def squish_jump(self):
        self.pot_en = 0
        self.isJump = True
        self.jump_count_up = 5
        self.jump_count_down = 0
        self.falling_count = 1
