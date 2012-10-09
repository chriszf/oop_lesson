import pyglet

game_window = pyglet.window.Window(800, 600)

pyglet.resource.path = ["../images"]
pyglet.resource.reindex()

@game_window.event
def on_draw():
    game_window.clear()

def run():
    pyglet.app.run()
