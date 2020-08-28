from resources import black, grass_tile


class Level:

    def __init__(self, w, h, tile_w, tile_h, buffer):
        self.w = w
        self.h = h
        self.tile_w = tile_w
        self.tile_h = tile_h
        self.buffer = buffer

    def set_buffer(self, w, h, buf):
        self.w = w
        self.h = h
        self.buffer = buf

    def place(self, x, y, tile_id):
        self.buffer[y][x] = tile_id

    def get(self, x, y):
        return self.buffer[y][x]

    def draw(self):
        for r in range(0, self.h):
            for c in range(0, self.w):
                img = ' '
                tile = self.buffer[r][c]
                if tile == 0:
                    img = black

                if tile == 1:
                    img = grass_tile

                img.blit(c * img.width, (self.h - 1 - r) * img.height)

    def what_is(self, x, y):
        return self.buffer[y // self.tile_h][x // self.tile_w]

    def update(self, dt):
        pass

    def on_key_press(self, symbol, modifiers):
        pass
