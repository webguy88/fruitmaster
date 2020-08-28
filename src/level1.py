from level import Level

map1 = [
    [0],
    [0]
]


class Level1(Level):

    def __init__(self, w, h, tile_w, tile_h, buffer):
        self.obj_list = []
        self.w = w
        self.h = h
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.buffer = buffer

    def on_key_press(self, symbol, modifiers):
        pass

    def what_is(self, x, y):
        return self.buffer[y // self.tile_h][x // self.tile_w]

