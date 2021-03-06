import pyglet
from engine import Engine
from utils import Region
from utils import center_images
from pyglet import resource
from pyglet import sprite
from level1 import Level1, map1

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

    walk_right_frames = [
            resource.image('guy_walk_right1.png'),
            resource.image('guy_walk_right2.png'),
            resource.image('guy_walk_right3.png'),
            resource.image('guy_walk_right4.png'),
            resource.image('guy_walk_right5.png'),
            resource.image('guy_walk_right6.png'),
            resource.image('guy_walk_right7.png'),
            resource.image('guy_walk_right8.png'),
            resource.image('guy_walk_right9.png')
    ]

    walk_left_frames = [
            resource.image('guy_walk_left1.png'),
            resource.image('guy_walk_left2.png'),
            resource.image('guy_walk_left3.png'),
            resource.image('guy_walk_left4.png'),
            resource.image('guy_walk_left5.png'),
            resource.image('guy_walk_left6.png'),
            resource.image('guy_walk_left7.png'),
            resource.image('guy_walk_left8.png'),
            resource.image('guy_walk_left9.png')
    ]

    center_images(idle_right_frames)
    center_images(idle_left_frames)
    center_images(walk_right_frames)
    center_images(walk_left_frames)

    idle_right = pyglet.image.Animation.from_image_sequence(idle_right_frames,
                                                            duration=0.1,
                                                            loop=True)

    idle_left = pyglet.image.Animation.from_image_sequence(idle_left_frames,
                                                           duration=0.1,
                                                           loop=True)

    walk_right = pyglet.image.Animation.from_image_sequence(walk_right_frames,
                                                            duration=0.1,
                                                            loop=True)

    walk_left = pyglet.image.Animation.from_image_sequence(walk_left_frames,
                                                           duration=0.1,
                                                           loop=True)

    def __init__(self):
        self.x = 480
        self.y = 320
        self.vx = 0
        self.vy = 0
        self.direction = "right"
        self.i_right = sprite.Sprite(self.idle_right)
        self.i_left = sprite.Sprite(self.idle_left)
        self.w_right = sprite.Sprite(self.walk_right)
        self.w_left = sprite.Sprite(self.walk_left)
        self.hitbox = Region(self.x, self.y, 54, 112)
        self.spr = self.i_right
        self.moving = False

    def draw(self):
        self.spr.draw()
        self.hitbox.draw()

    def detect_collision(self, hitbox):
        for obj in engine.current_screen.obj_list:
            if obj.solid and hitbox.collides(obj.hitbox):
                return obj

    def update(self, dt):
        new_x = self.x + self.vx * dt
        new_y = self.y + self.vy * dt
        new_hitbox = Region(x=new_x - 54 // 2,
                            y=new_y - 112 // 2,
                            w=48,
                            h=102)

        obj_hit = self.detect_collision(new_hitbox)

        if obj_hit is not None:
            self.vx = 0
            self.vy = 0
            self.spr = self.i_right if self.direction == 0 else self.i_left
            self.spr.x = self.x
            self.spr.y = self.y
            return

        if obj_hit is None:
            self.vy -= 5

        # Check sprite
        if not self.moving and \
           self.direction == "right" or self.direction == 0:
            self.spr = self.i_right

        if not self.moving and \
           self.direction == "left" or self.direction == 1:
            self.spr = self.i_left

        if self.moving and \
           self.direction == "right" or self.direction == 0:
            self.spr = self.w_right

        if self.moving and \
           self.direction == "left" or self.direction == 1:
            self.spr = self.w_left

        self.x = new_x
        self.y = new_y
        self.spr.x = self.x
        self.spr.y = self.y
        self.hitbox = new_hitbox

    def change_direction(self, direction, vx):
        self.direction = direction
        self.vx = vx


lvl1 = Level1(6, 6, 64, 64, map1)
engine = Engine(lvl1)
