import pyglet
from pyglet.window import key
from core import GameElement

SCREEN_X = 800
SCREEN_Y = 700

game_window = pyglet.window.Window(SCREEN_X, SCREEN_Y)

pyglet.resource.path = ["images/"]
pyglet.resource.reindex()

# Custom student changes
import game

IMAGES = {}
TILE_WIDTH = 0
TILE_HEIGHT = 0

def setup_images():
    filenames = {
            "Wall": "Wall Block.png",
            "Block": "Plain Block.png",
            "GrassBlock": "Grass Block.png",
            "StoneBlock": "Stone Block.png",
            "ShortTree": "Tree Short.png",
            "TallTree": "Tree Tall.png",
            "Rock": "Rock.png",
            "Chest": "Chest Closed.png",
            "DoorClosed": "Door Tall Closed.png",
            "DoorOpen": "Door Tall Open.png",
            "BlueGem": "Gem Blue.png",
            "GreenGem": "Gem Green.png",
            "OrangeGem": "Gem Orange.png",
            "Heart": "Heart.png",
            "Key": "Key.png",
            "Boy": "Character Boy.png",
            "Cat": "Character Cat Girl.png",
            "Horns": "Character Horn Girl.png",
            "Girl": "Character Pink Girl.png",
            "Princess": "Character Princess Girl.png"
            }

    for k,v in filenames.items():
        i = pyglet.resource.image(v)
#        i.anchor_x = i.width/2
        i.anchor_y = i.height
        IMAGES[k] = i

    global TILE_WIDTH, TILE_HEIGHT
    TILE_WIDTH = i.width
    TILE_HEIGHT = i.height

class Board(object):
    def __init__(self, width = 3, height = 3):
        self.width = width
        self.height = height

        # Screen center - half of board width
        board_width_px = width * TILE_WIDTH
        # Board height is half what we think because we stack tiles
        board_height_px = height * TILE_HEIGHT/2
        self.offset_x = ((SCREEN_X-board_width_px)/2.0)
        self.offset_y = ((SCREEN_Y-board_height_px)/2.0)
        self.offset_y = -SCREEN_Y/2 + board_height_px/2 + TILE_HEIGHT/4


        # Make a map with a stoneblock border and filled with grass
        game_map = []
        inner_width = width-2
        for i in range(height):
            if i == 0 or i == height-1:
                # On the boundaries
                game_map.append(["Block"] * width)
            else:
                row = ["Block"] + (["GrassBlock"] * inner_width) + ["Block"]
                game_map.append(row)
        
        self.base_board = game_map
        self.content_layer = []
        row = [ None ] * width
        for y in range(height):
            self.content_layer.append(list(row))

        self.message = pyglet.text.Label(text = "", x=10, y=SCREEN_Y-30)
        self.bg_sprites = []

        for y in range(height):
            for x in range(width):
                img_idx = game_map[y][x]
                image = IMAGES[img_idx]

                sprite = pyglet.sprite.Sprite(image)
                self.draw_bg(sprite, x, y)
                self.bg_sprites.append(sprite)

    def draw_msg(self, message):
        self.message.text = message
        pass

    def erase_msg(self):
        self.message.text = None
        pass

    def draw_bg(self, sprite, x_pos, y_pos):
        # x_pos and y_pos in board coordinates
        x_px = x_pos * sprite.width
        y_px = SCREEN_Y - (y_pos * sprite.height / 2)
        sprite.set_position(
                x_px + self.offset_x,
                y_px + self.offset_y)

    def draw_active(self, sprite, x_pos, y_pos):
        # x_pos and y_pos in board coordinates
        # Active layer is 1/4 sprite width above bg layer
        x_px = x_pos * sprite.width
        y_px = SCREEN_Y - (y_pos * sprite.height /2) + (sprite.height/4)

        sprite.set_position(
                x_px + self.offset_x,
                y_px + self.offset_y)
        sprite.draw()

    def check_bounds(self, x, y):
        if not (0 <= x < self.width):
            raise IndexError("%r is out of bounds of the board width: %d"%(x, self.width))
        if not (0 <= y < self.height):
            raise IndexError("%r is out of bounds of the board height: %d"%(y, self.width))

    def get_el(self, x, y):
        self.check_bounds(x, y)
        return self.content_layer[y][x]

    def set_el(self, x, y, el):
        self.check_bounds(x, y)
        el.x = x
        el.y = y
        self.content_layer[y][x] = el

    def del_el(self, x, y):
        self.check_bounds(x, y)
        self.content_layer[y][x] = None

    def register(self, el):
        image_file = IMAGES[el.IMAGE]
        el.board = self
        el.sprite = pyglet.sprite.Sprite(image_file)
        update_list.append(el)

    def draw(self):
        # Y is inverted
        # Draw the background
        for sprite in self.bg_sprites:
            sprite.draw()

        # Draw the label if it exists:
        if self.message:
            self.message.draw()
        # Draw the content layer
        for y in range(self.height):
            for x in range(self.width):
                el = self.content_layer[y][x]
                if el:
                    self.draw_active(el.sprite, x, y)


class Obstacle(GameElement):
    pass

def update(dt):
    for el in update_list:
        el.update(dt)

draw_list = []
update_list = []

@game_window.event
def on_draw():
    game_window.clear()
    for el in draw_list:
        el.draw()

def run():
    # Attempt to use custom board 
    global board
    global player
    setup_images()
    try:
        board = Board(game.GAME_WIDTH, game.GAME_HEIGHT)
    except (AttributeError) as e:
        board = Board()
        
    game.GAME_BOARD = board

    """
    try:
        board.register(player)
        update_list.append(player)
    except (AttributeError) as e:
        print "No player"
        player = None
    """

    # Set up an fps display
    try:
        if game.DEBUG == True:
            fps_display = pyglet.clock.ClockDisplay()
            draw_list.append(fps_display)
    except AttributeError:
        pass

    # Add the board and the fps display to the draw list
    draw_list.append(board)

    # Add the keyboard handler if it's ready
    key_handler = key.KeyStateHandler()
    game.KEYBOARD = key_handler
    game_window.push_handlers(key_handler)

    try:
        handler = game.keyboard_handler
        pyglet.clock.schedule_interval((lambda dt: handler), 1/10.0)
    except AttributeError:
        pass
        
    # Set up the update clock
    pyglet.clock.schedule_interval(update, 1/10.)
    game.initialize()
    pyglet.app.run()

class UpdateWrapper(object):
    def __init__(self, fn):
        self.fn = fn
    def update(self, dt):
        self.fn()

if __name__ == "__main__":
    run()
