Object Oriented Programming
===========================
This game only runs in python2.6 with the default pyglet install. To run the game, execute it as follows:

    python2.6 engine.py

We'll be editing **only** the code in game.py. After every step, run and experiment with the program to see how each addition changes it.

Step 1: Let's add something to the game.
----------------------------------------
The first thing we're going to do is add boulders to our game. First, we need to _define_ what a boulder is. We create a class definition as follows:

    class Rock(GameElement):
        IMAGE = "Rock"

What this says is that we're creating a new data type called 'Rock'. It's derived from an existing data type called GameElement. 'GameElement' objects have certain behaviors we have pre-defined that are required for the game to run, but you don't have to concern yourself with them here.

The second line of the class definition says that the Rock element has a **class attribute** called 'IMAGE', currently set to rock. A class attribute is an attribute that is shared between all instances of a class. This is distinct from regular attributes, which are distinct per instance. We'll explore this idea later.

The next thing we need to do is to actually create a single rock and place it on the board. The code to create an instance of a class looks like this:

    rock = Rock()

Simply calling the class as if it were a function creates a new rock for us to use. Here, we assign it to the variable 'rock'.

As a quirk of this particular game enginer we've written, we have to register this rock with the game board so that it displays. We do that by calling GAME\_BOARD.register(). After that, the rock can then be placed on the board with the GAME\_BOARD.set\_el() method. For the purposes of this exercise, when we place objects on our game board, we put the code in the initialize() function. The full code for that looks like this. 

**DO NOT COPY/PASTE PLZ**

    def initialize():
        """Put game initialization code here"""
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(1, 1, rock)
        print "The rock is at", (rock.x, rock.y)

The set\_el function takes in three elements, the x position, the y position, and the element you're placing at that position. If you imagine the game board as a grid, the top-left position is 0,0, and the bottom right is 2,2.

Try changing the position and see how the rock moves around. Notice the ouput of the print statement here.

Step 2: Increase the board size
-------------------------------
We need a little more room to do something interesting with our game. Let's increase the board size to a 4x4 grid. We do this by updating the GAME\_WIDTH and GAME\_HEIGHT variables. The top left is still 0,0, but the bottom right is now 3,3.

Step 3: Put more stuff on the board
-----------------------------------
Let's look at how to add a couple more boulders to the game. Each rock needs to be registered and set on the GAME\_BOARD independently. Each rock also needs its own variable. Change your initialize function to look like the following.

**>:[ SRSLY NO COPY/PASTE**

    def initialize():
        """Put game initialization code here"""

        # Initialize and register rock 1
        rock1 = Rock()
        GAME_BOARD.register(rock1)
        GAME_BOARD.set_el(1, 1, rock1)

        # Initialize and register rock 2
        rock2 = Rock()
        GAME_BOARD.register(rock2)
        GAME_BOARD.set_el(2, 2, rock2)

        print "The first rock is at", (rock1.x, rock1.y)
        print "The second rock is at", (rock2.x, rock2.y)
        print "Rock 1 image", rock1.IMAGE
        print "Rock 2 image", rock2.IMAGE

Try adding more rocks and playing around with placement. See what happens when you try to place a rock outside the bounds of the game grid.

Note the .x and .y attributes of rock1 and rock2. These are 'instance' attributes (usually just 'attributes'). Notice how they are different for each rock. On the other hand, both rocks share the same IMAGE class attribute we described in step 1.

Again, class attributes are shared between all instances of the class. If we had a class called Human, we might correctly add a class attribute NUM\_OF\_EYES = 2, whereas each instance of Human would have an attribute called .name, which would be distinct between each human.

Step 4: More expansion
----------------------
We're going to expand the game board to 5x5, once again by modifying the GAME\_WIDTH and GAME\_HEIGHT variables.

    GAME_WIDTH = 5
    GAME_HEIGHT = 5

We're also going to place four rocks in a cross pattern in the center of the board. It will look something like this:

    Stars represent rocks, dots represent empty spaces

    +---+
    |.*.|
    |*.*|
    |.*.|
    +---+

In our grid, this means a rock at (2, 1), (1,2), (3, 2), and (2, 3)

This time, instead of making four separate variables for each rock, we're going to instantiate each rock in a list. First, we'll make a list of the rock positions, and an empty list for all of our rock instances/objects:

    rock_positions = [
            (2, 1),
            (1, 2),
            (3, 2),
            (2, 3) 
        ]
    rocks = []

Then, we're going to loop through our list of positions, and for each position, we'll create and register a new rock object with our GAME\_BOARD.

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

Put all together, our initialize function looks like this:

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

Note at the end, we print each individual rock out of the list. Try playing around with the number of rocks on the board, manipulating them just with the list.

Step 5: Adding a Character class
-----------------------------
Rocks are pretty cool, but this game would be way better if we had something else on the board besides rocks. We're going to add a Character class to our game. We will use this as a base for our player representation in the game (our Player Character, or PC). This class will only be instantiated once, as we only have one player. Later, you might add other game characters that aren't controlled by the player (Non-Player Characters, NPCs). Since we're going to be interacting with the player from many places, we're going to save a reference to our player in the global PLAYER variable.

The class definition for Characters look like this:

    class Character(GameElement):
        IMAGE = "Girl"

Note again that it is derived from a GameElement, and it has a class attribute called IMAGE that has the value "Girl". This tells the game engine to use the 'Girl' image.

Register it in your initialize function after you register your rocks. Place it at position (2,2).

    # In the initialize() function
    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(2, 2, PLAYER)
    print PLAYER

There are a few other images which we can use for our player character. Try one of the following:
    "Boy", "Cat", "Princess", "Horns"

Step 6: And now a message from our sponsors
-------------------------------------------
We need a way to display a message on the screen. Fortunately, you don't have to figure that out, we've added one for your. Add the following line at the end of your initialize function.

    GAME_BOARD.draw_msg("This game is wicked awesome.")

There's also a related function, GAME\_BOARD.erase\_msg().

Step 7: Keyboard interaction
----------------------------
Now it's time to make our game interactive by adding keyboard capabilities.

The thing to note about they keyboard here is that we can no longer use the raw\_input function we've been using until now. When building a game, we can't expect our user to hit enter every time they press a key. Instead, we read the _state_ of the keyboard directly.

Up until now, we've thought of the keyboard as a source of input that feeds us characters one at a time in a stream. Another way to think of the keyboard is as a giant bundle of buttons that are either active or not.

Our game engine activates the keyboard in this second manner, and makes it available to you as a giant dictionary with an entry for each key. You can access the state of each key like so:

    # This will return True if the up arrow key is being pressed
    KEYBOARD[key.UP]

Because our game engine spends a lot of time dealing with graphics, we have to give it control of our main loop. Otherwise, we'd have to draw everything ourselves. Instead, our main loop has a hook to call a function of our choice every time it runs. In this case, it's set up to call our keyboard handler which we will use to interact with everything. To take advantage of this, create a function called keyboard\_handler that looks like this:

    def keyboard_handler():
        if KEYBOARD[key.UP]:
            GAME_BOARD.draw_msg("You pressed up")
        elif KEYBOARD[key.SPACE]:
            GAME_BOARD.erase_msg()

Try adding a message for each direction key on the keyboard, ie: down, left, right.

Step 8: Motion
--------------
The way we simulate motion is by reading a key, figuring out where our character will go, then removing them from the board and setting them at their new position.

When we want to move up, our character's 'y' position decreases by 1. If it moves down, it increases. Left is -1 in the x direction, and right is +1.

The implementation looks like this:

    def keyboard_handler():
        if KEYBOARD[key.UP]:
            GAME_BOARD.draw_msg("You pressed up")
            next_y = PLAYER.y - 1
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)

Add conditions for every direction.

Step 9: Instance methods
------------------------
We're going to simplify things by adding behavior to our character object. In theory, our Character class 'encapsulates' the behavior and data related to characters in our game. In this example, our character knows its own 'x' and 'y' position. Similarly, if we ask it to move in a direction, it should also know what its new position is.

    print (PLAYER.x, PLAYER.y)
    => (1, 1)
    print PLAYER.next_pos("up")
    => (1, 0)
    print (PLAYER.x, PLAYER.y)
    => (1, 1)

Note that finding out what the next position is does not actually move the player we do that manually.
We add an instance method to our Character class like so:

    class Character(GameElement):
        IMAGE = "Girl"

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

Note the unusual parameter 'self' that seems to disappear when we call it:

    def next_pos(self, direction):

    # but when we call it later:

    PLAYER.next_pos("up")

An instance method can be thought of as being _inside_ a particular instance. From inside that instance, the method needs a variable to refer to the instance it's inside of, thus the 'self' parameter.

Update your keyboard handler to use the new .next\_pos() method. We first decide which direction the player is trying to move by checking the keyboard with a big if statement

    if KEYBOARD[key.UP]:
        direction = "up"
    if KEYBOARD[key.DOWN]:
        direction = "down"
    if KEYBOARD[key.LEFT]:
        direction = "left"
    if KEYBOARD[key.RIGHT]:
        direction = "right"

Then we feed the direction to next\_pos to find out the location the player is trying to move to.

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

Lastly, we move the player to the new location by deleting them from their old position and re-setting them in their new position:

    GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
    GAME_BOARD.set_el(next_x, next_y, PLAYER)

All together, it looks like this:

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

Run the program and see how these changes affect the game.

Step 10: Rock Solid
-------------------
Whoah, we just walked through that boulder. Not only that, but we _ate_ it, as well. That's no good. We need some way to interact with the boulder. Or, more specifically, prevent us from interacting with it.

The first thing to do is look before we move. This means, after determining our next position, checking the board to see if there's anything already there. We can use the .get\_el method on our board. In our keyboard\_handler method:

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]
    
        existing_el = GAME_BOARD.get_el(next_x, next_y)

Now, we could just see if the existing\_el is an object of type Rock by using the isinstance() function. But what if there are other things that aren't rocks that we don't want to walk through? We need a more general way to do this.

We can make this 'walkability' an intrinsic property of all Rocks by adding a new 'class attribute' to the Rock class.

    class Rock(GameElement):
        IMAGE = "Rock"
        SOLID = True

Now, every instance of Rock will have the attribute 'SOLID' set to true. Interestingly, we can have the unusual behavior of setting individual Rocks to not be solid at our discretion.

Instead of checking whether or not the existing element we're about to walk over is a rock, we can just check whether or not it's solid:

    if existing_el is None or not existing_el.SOLID:
        # If there's nothing there _or_ if the existing element is not solid, walk through
        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
        GAME_BOARD.set_el(next_x, next_y, PLAYER)

All together:

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]
    
        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)


Step 11: It's a trap!
---------------------
Uh-oh, we're trapped! We're surrounded by four solid rocks! Remember what we said when we could modify individual rocks and override the class attribute? Let's do that now. We can take a particular rock instance and change its solidity. In our initialize function, after we create and register our rocks, let's change the bottom-most one to be intangible. We can access the last rock in our list and change the .SOLID attribute. In our initialize method:

    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False

Step 12: Freedom! Sweet, boring freedom!
----------------------------------------
Woo, we can move around. That's awesome. But our game is still kinda boring. Let's add a shiny bauble to our game.

    class Gem(GameElement):
        IMAGE = "BlueGem"
        SOLID = False

Register and set the gem at (3,1) in your initialize function, as before.

    GAME_BOARD.draw_msg("This game is wicked awesome.") 
    # Add these lines
    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(3, 1, gem)

One thing to remember is that the name of our classes isn't really important. We could have easily written the following instead:

    class ShinyBauble(GameElement):

The important thing about the class definition is that we properly inherit from the GameElement class so that they behave properly in our game.

Step 13: Remembering things that happened
-----------------------------------------
When we walk over our gem, it simply disappears. We need a way to remember that we've acquired an item, so we add state to our player characters. In game parlance, we can say that our character has an inventory. This is a property of a particular character, our game character. Given that we might have multiple characters later, we make the inventory an instance attribute of our Character class.

To do this, we need to add an initializer to say that when we create a Character, it starts with an empty inventory. Our inventory can be a simple list of objects our character is carrying.

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

This is an initializer. It "sets up" our object with initial values. Here, we're telling the character that it must have an empty list as an inventory to start. 

Notice the line, 'GameElement.\_\_init\_\_(self)'. To be a proper game element, there was some behavior defined on the GameElement class to interact with the board correctly. When we add an initializer to our class, we need to tell our class that it still needs to do those things, so we call the parent class' initializer.

Next, we need a way for our player to 'interact' with an object. In fact, we want the player to interact with pretty much every object on the board. Most of the time, the interactions won'tproduce anything, but we do it anyway. In the keyboard\_handler:

    existing_el = GAME_BOARD.get_el(next_x, next_y)
    # Add after this line

    if existing_el:
        existing_el.interact(PLAYER)

Now, whenever the player tries to bump into an object, it will try to interact with our character first. The default behavior for interaction is to do nothing. This is defined on the GameElement class. We want to override the behavior when a player interacts with a Gem. We want that gem to be added to the player's inventory. It will take the following format:

    player.inventory.append(gem)

To do that, we modify the Gem class and add the 'interact' method. Whenever the gem interacts with a player, it gets added to their inventory and a message displays:

    class Gem(GameElement):
        def interact(self, player):
            player.inventory.append(self)
            GAME_BOARD.draw_msg("You just acquired a gem! You have %d items!"%(len(player.inventory)))

(Our game is getting quite big, if you can't figure out where to add these lines, check the reference implementation in game\_ref.py.)

Experiment with adding different gems that have different interaction behaviors. For example, you could print different messages, or maybe touching a certain type of gem resets the user position to the starting point.

Step 14: Get Clever, Have Fun
-----------------------------
Congratulations, you have a game. Sort of. It's not all that interesting, and it definitely could be better. You can spend some time looking at engine.py to see how it all works (be careful, there be dragons down there).

More interestingly, spend some time playing with object interactions, adding more objects and classes to your game, and fixing some bugs. Here are some ideas:

* Fix the game so it doesn't crash when you go beyond the game board boundaries.
* Add other elements to the game, keys, chests, doors
* Add conditional interactions: a door that won't open unless you have the right colored gem,
chests that won't open unless you have the right key.
* Subclass the Character class to make non-player characters that speak messages when you interact with them.
* Tricky: Add blocks that slide when you push them.

Here's a list of all the sprites (game images) that the game engine understands. Similar to our Rock, Gem, and Character classes, create one and set the IMAGE class property to the appropriate image.

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

Mostly, be clever with this and have fun! Classes, woo.
