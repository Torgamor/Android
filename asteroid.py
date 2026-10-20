from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20, 50)
            rotate_vector = self.velocity.rotate(random_angle)
            rotate_vector2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = rotate_vector * 1.2
            new_asteroid2.velocity = rotate_vector2 * 1.2
