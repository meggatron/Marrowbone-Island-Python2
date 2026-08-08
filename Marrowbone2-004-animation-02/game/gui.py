from game.sprites import PlayerSprite

import pygame

screen = None
font = None
last_lines = []
all_sprites = None



def start():
    global screen
    global font
    global player_sprite
    global all_sprites

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Marrowbone Island")

    font = pygame.font.SysFont("Arial", 28)

    player_sprite = PlayerSprite(600, 400)
    all_sprites = pygame.sprite.Group(player_sprite)

def draw_text(lines, input_text=None):
    screen.fill((10, 100, 120))

    all_sprites.update()
    all_sprites.draw(screen)

    for i, line in enumerate(lines):
        line_surface = font.render(line, True, pygame.Color("white"))
        screen.blit(line_surface, (40, 60 + i * 35))

    if input_text is not None:
        input_surface = font.render("> " + input_text, True, pygame.Color("lime"))
        screen.blit(input_surface, (40, 430))

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
    visible_lines = last_lines + [""] + prompt_lines

    while True:
        draw_text(visible_lines, input_text)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text.lower().strip()
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        clock.tick(30)


def pause(ms):
    clock = pygame.time.Clock()
    elapsed = 0

    while elapsed < ms:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        clock.tick(60)
        elapsed += clock.get_time()


def quit():
    pygame.quit()
    raise SystemExit