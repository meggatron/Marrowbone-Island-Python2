# Marrowbone2-009-backgrounds/game/gui.py

from game.sprites import PlayerSprite
from game import player

import pygame

screen = None
font = None
last_lines = []
all_sprites = None
player_sprite = None
background = None
player_visible = False

TEXT_TOP = 20
STORY_TOP = 70
CHOICE_TOP = 170
PLAY_AREA_TOP = 220


def start():
    global screen
    global font
    global player_sprite
    global all_sprites

    pygame.init()

    screen = pygame.display.set_mode(
        (0, 0),
        pygame.FULLSCREEN
    )
    pygame.display.set_caption("Marrowbone Island")

    font = pygame.font.SysFont("Arial", 28)

    set_background("assets/images/dock.png")

    width, height = screen.get_size()

    player_sprite = PlayerSprite(
        width // 2,
        int(height * 0.70)
    )

    all_sprites = pygame.sprite.Group(player_sprite)


def set_background(image_path=None):
    global background

    if image_path is None:
        background = None
        return

    background = pygame.image.load(
        image_path
    ).convert()

    background = pygame.transform.scale(
        background,
        screen.get_size()
    )


def draw_text(lines, input_text=None):
    if background is not None:
        screen.blit(background, (0, 0))
    else:
        screen.fill((222,222,222))

    inventory_text = "Inventory: " + (
        ", ".join(sorted(player.inventory))
        if player.inventory
        else "empty"
    )

    inventory_surface = font.render(
        inventory_text,
        True,
        pygame.Color("black")
    )
    screen.blit(inventory_surface, (40, TEXT_TOP))

    for i, line in enumerate(lines):
        line_surface = font.render(
            line,
            True,
            pygame.Color("black")
        )
        screen.blit(
            line_surface,
            (40, STORY_TOP + i * 35)
        )

    if input_text is not None:
        input_surface = font.render(
            "> " + input_text,
            True,
            pygame.Color("black")
        )
        screen.blit(
            input_surface,
            (40, CHOICE_TOP)
        )

    if player_visible:
        all_sprites.update()
        all_sprites.draw(screen)

    pygame.display.flip()


def display(text):
    global last_lines

    last_lines = text.strip().split("\n")

    player_sprite.talk()

    draw_text(last_lines)


def get_input(prompt):
    global last_lines

    input_text = ""
    clock = pygame.time.Clock()

    prompt_lines = prompt.strip().split("\n")

    visible_lines = (
        last_lines
        + [""]
        + prompt_lines
    )

    while True:
        # Draw background
        if background is not None:
            screen.blit(background, (0, 0))
        else:
            screen.fill((222,222,222))

        # Inventory
        inventory_text = "Inventory: " + (
            ", ".join(sorted(player.inventory))
            if player.inventory
            else "empty"
        )

        inventory_surface = font.render(
            inventory_text,
            True,
            pygame.Color("black")
        )

        screen.blit(
            inventory_surface,
            (40, TEXT_TOP)
        )

        # Story + prompt
        for i, line in enumerate(visible_lines):
            line_surface = font.render(
                line,
                True,
                pygame.Color("black")
            )

            screen.blit(
                line_surface,
                (40, STORY_TOP + i * 35)
            )

        # Put input BELOW all the text
        input_y = STORY_TOP + len(visible_lines) * 35 + 10

        input_surface = font.render(
            "> " + input_text,
            True,
            pygame.Color("black")
        )

        screen.blit(
            input_surface,
            (40, input_y)
        )

        if player_visible:
            all_sprites.update()
            all_sprites.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    quit()

                elif event.key == pygame.K_RETURN:
                    return input_text.lower().strip()

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    input_text += event.unicode

        clock.tick(30)


def choose(
    west=None,
    east=None,
    north=None,
    south=None
):
    clock = pygame.time.Clock()

    width, height = screen.get_size()
    play_area_top = int(height * 0.35)

    # Invisible collision zones
    west_rect = pygame.Rect(
        0,
        play_area_top,
        int(width * 0.20),
        height - play_area_top
    )

    east_rect = pygame.Rect(
        int(width * 0.80),
        play_area_top,
        int(width * 0.20),
        height - play_area_top
    )

    north_rect = pygame.Rect(
        int(width * 0.35),
        play_area_top,
        int(width * 0.30),
        int(height * 0.18)
    )

    south_rect = pygame.Rect(
        int(width * 0.35),
        int(height * 0.82),
        int(width * 0.30),
        int(height * 0.18)
    )

    while True:
        # Background
        if background is not None:
            screen.blit(background, (0, 0))
        else:
            screen.fill((222,222,222))

        # Inventory
        inventory_text = "Inventory: " + (
            ", ".join(sorted(player.inventory))
            if player.inventory
            else "empty"
        )

        inventory_surface = font.render(
            inventory_text,
            True,
            pygame.Color("black")
        )

        screen.blit(
            inventory_surface,
            (40, TEXT_TOP)
        )

        # Story text
        for i, line in enumerate(last_lines):
            line_surface = font.render(
                line,
                True,
                pygame.Color("black")
            )

            screen.blit(
                line_surface,
                (40, STORY_TOP + i * 35)
            )

        # Choices appear below the story text
        choice_y = STORY_TOP + len(last_lines) * 35 + 20

        # West
        if west is not None:
            west_surface = font.render(
                "← " + west,
                True,
                pygame.Color("black")
            )

            screen.blit(
                west_surface,
                (40, choice_y)
            )

        # East
        if east is not None:
            east_surface = font.render(
                east + " →",
                True,
                pygame.Color("black")
            )

            east_text_rect = east_surface.get_rect(
                topright=(width - 40, choice_y)
            )

            screen.blit(
                east_surface,
                east_text_rect
            )

        # North
        if north is not None:
            north_surface = font.render(
                "↑ " + north,
                True,
                pygame.Color("black")
            )

            north_text_rect = north_surface.get_rect(
                midtop=(width // 2, choice_y)
            )

            screen.blit(
                north_surface,
                north_text_rect
            )

        # South
        if south is not None:
            south_surface = font.render(
                "↓ " + south,
                True,
                pygame.Color("black")
            )

            south_text_rect = south_surface.get_rect(
                midtop=(width // 2, choice_y + 35)
            )

            screen.blit(
                south_surface,
                south_text_rect
            )

        # Update and draw player
        all_sprites.update()
        all_sprites.draw(screen)

        # Check collisions
        if west is not None:
            if player_sprite.rect.colliderect(west_rect):
                return "west"

        if east is not None:
            if player_sprite.rect.colliderect(east_rect):
                return "east"

        if north is not None:
            if player_sprite.rect.colliderect(north_rect):
                return "north"

        if south is not None:
            if player_sprite.rect.colliderect(south_rect):
                return "south"

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        pygame.display.flip()
        clock.tick(60)

def reset_player():
    width, height = screen.get_size()

    player_sprite.rect.center = (
        width // 2,
        int(height * 0.70)
    )


def pause(ms):
    clock = pygame.time.Clock()
    elapsed = 0

    while elapsed < ms:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()

        clock.tick(60)
        elapsed += clock.get_time()


def hide_player():
    global player_visible
    player_visible = False


def show_player():
    global player_visible
    player_visible = True

def clear_text():
    global last_lines
    last_lines = []

def quit():
    pygame.quit()
    raise SystemExit