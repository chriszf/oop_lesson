Objects
=======

1. Create a rock class

class Rock(GameElement):
    IMAGE = "Rock"

def initialize():
    """Put game initialization code here"""
    rock = Rock()
    GAME_BOARD.register(rock)
    GAME_BOARD.set_el(1, 1, rock)
    print "The rock is at", (rock.x, rock.y)

Try changing the position and see how the rock moves around

2. Increase the board size,
change 'GAME__WIDTH' and 'GAME__HEIGHT' variables to 4 and 4

    def initialize():
        """Put game initialization code here"""
        rock1 = Rock()
        rock2 = Rock()
        GAME_BOARD.register(rock1)
        GAME_BOARD.register(rock2)
        GAME_BOARD.set_el(1, 1, rock1)
        GAME_BOARD.set_el(2, 2, rock2)
        print "The first rock is at", (rock1.x, rock1.y)
        print "The second rock is at", (rock2.x, rock2.y)

3. Add 2 more rocks, fill out the map

4. Expand the game board even more to 5x5, place 4 rocks at (3, 1), (2, 2), (4, 2), and (3, 3)

Rather than using a variable for each rock, we'll use a list:

def initialize():
    """Put game initialization code here"""
    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
            (2, 3) 
        ]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    for rock in rocks:
        print rock

5. Create a Player class, also a GameElement

    class Character(GameElement):
        IMAGE = "Girl"
    

Register it after you registered your rocks.

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

Try switching your image to one of the following:
    "Boy", "Cat", "Princess", "Horns"

6. Interlude, drawing a message:
After creating all of your objects, put a greeting on the screen:

    GAME_BOARD.draw_msg("This game is wicked awesome.")

7. Now that we can draw messages, we can see about the keyboard

7. Create a function, named keyboard__handler, that ooks like this __

    def keyboard_handler():
        if KEYBOARD[key.UP]:
            GAME_BOARD.draw_msg("You pressed up")

Add a message for each of the arrow keys inside the keyboard_handler function _

8. Now, time to move our character, when the user presses up, we want our critter to move up, ie: the y position goes down by one. Update your keyboard handler function to look like this:

    def keyboard_handler():
        if KEYBOARD[key.UP]:
            GAME_BOARD.draw_msg("You pressed up")
            next_y = PLAYER.y - 1
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

Add conditions for every direction

9. We're going to simplify things, add behavior to the character. To the character class, add a next_pos function:

    class Character(GameElement):
        IMAGE = "Cat"

        def next_pos(self, direction):
            if direction == "up":
                return (self.x, self.y-1)
            elif direction == "down":
                return (self.x, self.y+1)
            elif direction == "left":
                return (self.x-1, self.y)
            elif direction == "right":
                return (self.x+1, self.y)
            return None

Modify your keyboard handler function to look like this:

    def keyboard_handler():
        direction = None

        if KEYBOARD[key.UP]:
            direction = "up"
        if KEYBOARD[key.DOWN]:
            direction = "down"
        if KEYBOARD[key.LEFT]:
            direction = "left"
        if KEYBOARD[key.RIGHT]:
            direction = "right"

        if direction:
            next_location = PLAYER.next_pos(direction)
            next_x = next_location[0]
            next_y = next_location[1]

            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)

10. Things are slightly better, but now, we need to make sure we don't go through rocks.

Modify the rock class:

    class Rock(GameElement):
        IMAGE = "Rock"
        SOLID = True

Change the 'if direction' statement in your keyboard_handler

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]
    
        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)


11. Uh-oh, we're trapped! Let's get rid of a rock.Remove the last rock from our rock position list.

    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
        ]

12. Woo, we can move around. That's awesome. But we're still kinda boring. Let's add a gem to the system.

    class Gem(GameElement):
        IMAGE = "BlueGem"
        SOLID = False

At the end of your initialize function, add the following:

    GAME_BOARD.draw_msg("This game is wicked awesome.") 
    # Add these lines
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

13. Uh-oh, our gem just disappears without a trace! We need to make sure we remember that we've touched and picked up the gem. Before we walk over and erase it, we should 'interact' with the gem.

Modify your keyboard_handler as such:

        existing_el = GAME_BOARD.get_el(next_x, next_y)
        # Add after this line

        if existing_el:
            existing_el.INTERACT(player)

Now, modify your Character class, add an initializer

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

And add the following method to your gem class

    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You just acquired a gem!")

Now modify the game to have more gems and have the message print out how many gems you have acquired so far.

13. Things to do:
Fix the game so it doesn't crash when you go beyond the game board boundaries.
Make the game board bigger and add more obstacles that aren't just rocks.
Add conditional interactions: a door that won't open unless you have the right colored gem,
treasure that won't open unless you have the right key.
Tricky: Add blocks that slide when you push them.

Here are some more tiles that the game understands. Make a class for the object you want, and set its IMAGE attribute to one of the following:

            Wall
            Block
            GrassBlock
            StoneBlock
            ShortTree
            TallTree
            Rock
            Chest
            DoorClosed
            DoorOpen
            BlueGem
            GreenGem
            OrangeGem
            Heart
            Key
            Boy
            Cat
            Horns
            Girl
            Princess
