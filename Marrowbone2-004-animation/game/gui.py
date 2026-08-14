# Marrowbone2-004-pygame-GUI/game/gui.py


# import our PlayerSprite Class from sprites.py
from game.sprites import PlayerSprite

# import the pygame library
import pygame


# GUI variables
# these start empty and get their values when start() runs
screen = None
font = None
last_lines = []
all_sprites = None


# start pygame and set up everything we need for the game window
def start():
    global screen, font
    global all_sprites

    # initialize pygame
    pygame.init()

    # create an 800 x 600 pixel game window
    screen = pygame.display.set_mode((800, 600))

    # set the title at the top of the window
    pygame.display.set_caption("Marrowbone Island")

    # create the font we will use for game text
    font = pygame.font.SysFont("Arial", 28)

    # create one PlayerSprite at x 600, y 400
    player_sprite = PlayerSprite(600, 400)

    # put our player sprite into a pygame sprite Group
    # Groups let us update and draw sprites together
    all_sprites = pygame.sprite.Group(player_sprite)


# draw the background, sprite, and text on the screen
def draw_text(lines, input_text=None):

    # fill the whole screen with our dark blue background
    screen.fill((10, 20, 40))

    # run the update() method for every sprite in the Group
    # this is what lets our PlayerSprite check for movement and animate
    all_sprites.update()

    # draw every sprite in the Group
    all_sprites.draw(screen)

    # loop through each line of text
    # enumerate() gives us both the line number i and the line itself
    for i, line in enumerate(lines):

        # turn the text into something pygame can draw
        line_surface = font.render(line, True, pygame.Color("white"))

        # blit means draw one Surface onto another Surface
        # i * 35 moves each new line farther down the screen
        screen.blit(line_surface, (40, 60 + i * 35))

    # if the player is currently typing, draw their input
    if input_text is not None:
        input_surface = font.render(
            "> " + input_text,
            True,
            pygame.Color("lime")
        )
        screen.blit(input_surface, (40, 430))

    #####################################
    # IMPORTANT TYPO CHECK FROM YESTERDAY
    # this line should be outside the if statement above
    # flip updates the display so we can actually see what we just drew
    pygame.display.flip()


# display text in the game window
def display(text):
    global last_lines

    # remove extra whitespace and split text wherever there is a new line
    # save those lines so we can keep displaying them
    last_lines = text.strip().split("\n")

    # draw those lines on the screen
    draw_text(last_lines)


# get typed input from the player
def get_input(prompt):
    global last_lines

    # start with an empty string for whatever the player types
    input_text = ""

    # create a pygame Clock to control how fast this loop runs
    clock = pygame.time.Clock()

    # split the prompt into separate lines
    prompt_lines = prompt.strip().split("\n")

    # combine the previous text, a blank line, and the new prompt
    visible_lines = last_lines + [""] + prompt_lines

    # keep checking for input until the player presses return
    while True:

        # redraw the screen with whatever the player has typed so far
        draw_text(visible_lines, input_text)

        # get pygame events like closing the window or pressing a key
        for event in pygame.event.get():

            # if the player closes the window, quit the game
            if event.type == pygame.QUIT:
                quit()

            # check whether the event was a key press
            if event.type == pygame.KEYDOWN:

                # IMPORTANT TYPO CHECK FROM YESTERDAY
                # this must be event.key, not event.kev
                if event.key == pygame.K_RETURN:

                    # return the player's answer
                    # lower() makes it lowercase
                    # strip() removes extra spaces
                    return input_text.lower().strip()

                # remove the last character when backspace is pressed
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                # otherwise add the typed character to input_text
                else:
                    input_text += event.unicode

        # limit this input loop to 30 updates per second
        clock.tick(30)


# pause the game for a number of milliseconds
def pause(ms):

    # create a Clock to measure time
    clock = pygame.time.Clock()

    # start our elapsed time at zero
    elapsed = 0

    # keep looping until the requested amount of time has passed
    while elapsed < ms:

        # still check events while paused so the window does not freeze
        for event in pygame.event.get():

            # allow the player to close the game during a pause
            if event.type == pygame.QUIT:
                quit()

        # IMPORTANT TYPO CHECK FROM YESTERDAY
        # these two lines belong outside the for loop and if statement above

        # limit this loop to about 60 updates per second
        clock.tick(60)

        # add the time since the last tick to our elapsed time
        elapsed += clock.get_time()


# shut down pygame and stop the Python program
def quit():

    # shut down pygame
    pygame.quit()

    # stop the Python program
    raise SystemExit