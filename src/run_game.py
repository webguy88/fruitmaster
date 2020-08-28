import pyglet
from pyglet import resource
from pyglet import clock
from pyglet.window import Window
from pyglet.window import key

from player import Player
from level1 import Level1, map1
from engine import Engine
from camera import Camera

# Resource
resource.path = ['../resources', '../resources/art', '../resources/sounds']
resource.reindex()

# Window
SCREENW = 960
SCREENH = 640
window = Window(SCREENW, SCREENH, caption="Fruit Master")


# Anchoring camera position
def position_camera(self, camera: Camera, position: tuple = (0, 0),
                    zoom: float = 1, min_pos: tuple = (None, None),
                    max_pos: tuple = (None, None)):

    zoom = min(window.width // self.DEFAULT_SIZE[0],
               window.height // self.DEFAULT_SIZE[1]) * zoom

    if self.camera.zoom != zoom:
        self.camera.zoom = zoom

        x = -window.width // 2 // zoom
        y = -window.height // 2 // zoom

        target_x = position[0]
        target_y = position[1]

        if min_pos[0] is not None:
            target_x = max(target_x, min_pos[0])
        if min_pos[1] is not None:
            target_y = max(target_y, min_pos[1])
        if max_pos[0] is not None:
            target_x = min(target_x, max_pos[0])
        if max_pos[1] is not None:
            target_y = min(target_y, max_pos[1])

        x += target_x
        y += target_y

        if self.camera.position != (x, y):
            self.camera.position = (x, y)


# Window events
@window.event
def on_draw():
    window.clear()
    camera.begin()
    engine.draw()
    player.draw()
    camera.end()


@window.event
def on_key_press(symbol, modifiers):
    engine.on_key_press(symbol, modifiers)


@window.event
def update(dt):
    engine.update(dt)
    player.update(dt)

    if engine.in_game:
        vx = vy = 0

        if keys[key.A]:
            player.change_direction(1, -170, 0)
            vx -= 170 * dt

        if keys[key.D]:
            player.change_direction(0, 170, 0)
            vx += 170 * dt

        if not is_key_pressed():
            player.change_direction(player.direction, 0, 0)

        camera.position = (camera.offset_x + vx,
                           camera.offset_y + vy)


def is_key_pressed():
    for _, v in keys.items():
        if v:
            return True

    return False


keys = key.KeyStateHandler()
window.push_handlers(keys)

player = Player()
lvl1 = Level1(1, 1, 1, 1, map1)
engine = Engine(lvl1)
camera = Camera(scroll_speed=5)

clock.schedule_interval(update, 1/30)
pyglet.app.run()
