from pyglet import resource
from pyglet import sprite

resource.path = ['../resources', '../resources/art', '../resources/sounds']
resource.reindex()

black = resource.image('black.png')
black_spr = sprite.Sprite(black, x=0, y=0)
grass_tile = resource.image('tile_test.png')
grass_spr = resource.image(grass_tile)
