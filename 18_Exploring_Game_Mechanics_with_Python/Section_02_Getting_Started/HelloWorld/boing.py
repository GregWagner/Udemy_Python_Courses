import pygame as pg
import math, sys, random
from enum import Enum

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 480
TITLE: str = "Breakin' Balls"

HALF_WIDTH = SCREEN_WIDTH // 2
HALF_HEIGHT = SCREEN_HEIGHT // 2
PLAYER_SPEED = 6
MAX_AI_SPEED = 6


def normalized(x: float, y: float) -> tuple[float, float]
    length: int = math.hypot(x, y)
    return x / length, y / length


def sign(x: float) -> int:
    return -1 if x < 0 else 1

class Impact(Actor):
    def __init__(self, pos):
        super().__init__("blank", pos)
        self.time: int = 0

    def update(self):
        self.image: str = "impact" + str(self.time // 2)
        self.time += 1

class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball", pos)
        self.x, self.y = HALF_WIDTH, HALF_HEIGHT
        self.dx, self.dy = dx, 0
        self.speed = 5

    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y += self.dy

