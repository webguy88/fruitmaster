from utils import Region
from resources import black_spr
from pyglet import clock


class Engine:

    def __init__(self, current_screen):
        self.in_game = True
        self.opacity = 0
        self.on_exit = False
        self.current_screen = current_screen
        self.next_screen = current_screen

    def draw(self):
        self.current_screen.draw()

        if self.on_exit:
            self.opacity = self.opacity + 30
            black_spr.opacity = min(self.opacity, 255)
            black_spr.draw()

    def on_key_press(self, symbol, modifiers):
        self.current_screen.on_key_press(symbol, modifiers)

    def update(self, dt):
        self.current_screen.update(dt)

    def set_current_screen(self, current_screen):
        self.current_screen = self.next_screen

    def set_next_screen(self, next_screen):
        clock.schedule_once(self.set_current_screen, 0.2)
        self.next_screen = next_screen
        self.on_exit = True

    def enter(self):
        self.current_screen.enter()
        self.opacity = 0
        self.on_exit = False
