import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    containers: list[pygame.sprite.Group] = []

    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt: float):
        self.position += self.velocity * dt

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius)
