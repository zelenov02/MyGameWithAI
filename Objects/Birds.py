import random
import os

import pygame
import config


class Birds:
    frames = None
    name = None
    color = None
    ROTATION_MAX_ANGLE = 25
    ROTATION_SPEED = 20
    ANIMATION_STEP = 5
    AVAILABLE_COLORS = ('red', 'blue', 'yellow')
    GRAVITY = 0.025
    FLAP_POWER = -0.5
    CLOCK = pygame.time.Clock()

    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color if color in self.AVAILABLE_COLORS else random.choice(self.AVAILABLE_COLORS)
        self.x = x
        self.y = y
        self.angle = 0
        self.speed = 0
        self.height = self.y
        self.anim_step = 0
        self.cframe = None

        self.load_frame()

    def load_frame(self):
        self.frames = [
            pygame.transform.scale_by(pygame.image.load(os.path.join(
                config.TEXTURES_DIRECTORY, self.color.lower() + 'bird-' + str(x) + '.png')), 1.0)
            for x in range(1, 4)]
        self.cframe = self.frames[0]

    def jumping(self):
        self.speed = self.FLAP_POWER
        self.height = self.y

    def moves(self):
        self.speed += self.GRAVITY

        drop = self.speed

        if drop >= 6:
            drop = (drop/abc(drop)) * 6

        self.y += drop

        if drop < 0 or self.y < self.height + 50:
            if self.angle < self.ROTATION_MAX_ANGLE:
                self.angle = self.ROTATION_MAX_ANGLE
        else:
            if self.angle > -90:
                self.angle -= self.ROTATION_SPEED

