import pyglet
from pyglet import resource
from pyglet import sprite
from pyglet.gl import gl

gl.glEnable(gl.GL_TEXTURE_2D)
gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
pyglet.image.Texture.default_mag_filter = gl.GL_NEAREST
pyglet.image.Texture.default_min_filter = gl.GL_NEAREST

resource.path = ['../resources', '../resources/art', '../resources/sounds']
resource.reindex()

black = resource.image('black.png')
black_spr = sprite.Sprite(black, x=0, y=0)
grass_tile = resource.image('tile_test.png')
grass_spr = sprite.Sprite(grass_tile)
