import pyglet
from engine import Engine
from utils import Region
from utils import center_images
from pyglet import resource
from pyglet import sprite

resource.path = ['../resources', '../resources/art', '../resources/sound']
resource.reindex()


class Player:

    idle_right_frames = [
            resource.image('guy_idle_right1.png'),
            resource.image('guy_idle_right2.png'),
            resource.image('guy_idle_right3.png'),
            resource.image('guy_idle_right4.png')
         ]

    idle_left_frames = [
            resource.image('guy_idle_left1.png'),
            resource.image('guy_idle_left2.png'),
            resource.image('guy_idle_left3.png'),
            resource.image('guy_idle_left4.png')
        ]

    center_images(idle_right_frames)
    center_images(idle_left_frames)

    idle_right = pyglet.image.Animation.from_image_sequence(idle_right_frames,
                                                            duration=0.1,
                                                            loop=True)

    idle_left = pyglet.image.Animation.from_image_sequence(idle_left_frames,
                                                           duration=0.1,
                                                           loop=True)

    def __init__(self):
        self.x = 120
        self.y = 120
        self.vx = 0
        self.vy = 0
        self.direction = "right"
        self.i_right = sprite.Sprite(self.idle_right)
        self.i_left = sprite.Sprite(self.idle_left)
        self.spr = self.i_right
        self.moving = False

    def draw(self):
        self.spr.draw()

    def detect_collision(self, hitbox):
        for obj in engine.current_screen.obj_list:
            if obj.solid and hitbox.collides(obj.hitbox):
                return obj

    def update(self, dt):
        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt

        self.x = new_x
        self.y = new_y
        self.spr.x = self.x
        self.spr.y = self.y

        if not self.moving and \
           self.direction == "right" or self.direction == 0:
            self.spr = self.i_right

        if not self.moving and \
           self.direction == "left" or self.direction == 1:
            self.spr = self.i_left

    def change_direction(self, direction, vx, vy):
        self.direction = direction
        self.vx = vx
        self.vy = vy

