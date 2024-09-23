import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers: list[pygame.sprite.Group] = []

    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        for velocity in [self.velocity.rotate(angle), self.velocity.rotate(-angle)]:
            child = Asteroid(
                self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
            )
            child.velocity = velocity * 1.2
