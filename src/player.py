from engine import Engine
from utils import Region


class Player:

    def __init__(self):
        self.x = 120
        self.y = 120
        self.vx = 0
        self.vy = 0
        self.direction = "right"
        self.moving = False

    def draw(self):
        pass

    def detect_collision(self, hitbox):
        for obj in engine.current_screen.obj_list:
            if obj.solid and hitbox.collides(obj.hitbox):
                return obj

    def update(self, dt):
        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt

        self.x = new_x
        self.y = new_y

    def change_direction(self, direction, vx, vy):
        self.direction = direction
        self.vx = vx
        self.vy = vy

