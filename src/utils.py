import pyglet
from pyglet.gl import gl


class Rect:

    def __init__(self, x, y, w, h):
        self.set(x, y, w, h)

    def draw(self):
        pyglet.graphics.draw(4, gl.GL_QUADS, self._quad)

    def set(self, x=None, y=None, w=None, h=None):
        self._x = self._x if x is None else x
        self._y = self._y if y is None else y
        self._w = self._w if w is None else w
        self._h = self._h if h is None else h
        self._quad = ('v2f', (self._x, self._y,
                              self._x + self._w, self._y,
                              self._x + self._w, self._y + self._h,
                              self._x, self._y + self._h))

    def __repr__(self):
        return f"Rect(x={self._x}, y={self._y}, w={self._w}, h={self._h})"


class Region:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def contain(self, x, y):
        inside_x = False
        inside_y = False

        if x >= self.x and x <= (self.x + self.w):
            inside_x = True

        if y >= self.y and y <= (self.y + self.h):
            inside_y = True

        if inside_x and inside_y:
            return True
        else:
            return False

    def collides(self, r2):
        if self.x < r2.x + r2.width and \
           self.x + self.w > r2.x and \
           self.y < r2.y + r2.height and \
           self.y + self.h > r2.y:
               return True

    def draw(self):
        r = Rect(self.x, self.y, self.w, self.h)
        r.draw()


class SceneObject:

    def __init__(self, id, solid, name, x, y, w=0, h=0, spr=None, visible=True):
        self.id = id
        self.solid = solid
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.spr = spr
        self.visible = visible

        if spr is not None:
            self.spr.x = self.x
            self.spr.y = self.y

        if spr is not None and w == 0 and h == 0:
            self.hitbox = Region(self.x - self.spr.width // 2,
                                 self.y - self.spr.height // 2,
                                 self.spr.width,
                                 self.spr.height)

        else:
            self.hitbox = Region(self.x - self.w // 2,
                                 self.y - self.h // 2,
                                 self.w,
                                 self.h)


class Screen:

    def __init__(self):
        pass

    def draw(self):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def update(self, dt):
        pass

    def enter(self):
        pass


def center_image(img):
    img.anchor_x = img.width // 2
    img.anchor_y = img.height // 2


def center_images(i_list):
    for img in i_list:
        img.anchor_x = img.width // 2
        img.anchor_y = img.height // 2

