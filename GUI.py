import pygame as pg
import pygame_textinput as pgt
import sys
from collections import deque
from Client import Client, NETWORK_EVENT
from Server import Server

# ----- Game constants -----
WIDTH, HEIGHT = 1280, 720
SCREENRECT = pg.Rect(0, 0, WIDTH, HEIGHT)

# Colors
WHITE = (255, 255, 255)
LIGHT_GRAY = (235, 235, 235)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLACK = (0, 0, 0)
RED = (200, 40, 40)
GREEN = (40, 160, 80)

# Simple app states
STATE_MENU = "menu"
STATE_CLIENT = "state_client"
STATE_SERVER = "state_server"


def draw_button(screen, rect, text, fill, font):
    pg.draw.rect(screen, fill, rect, border_radius=12)
    pg.draw.rect(screen, BLACK, rect, 2, border_radius=12)
    txt = font.render(text, True, BLACK)
    screen.blit(txt, txt.get_rect(center=rect.center))


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Clue-Less")
    clock = pg.time.Clock()
    font = pg.font.Font(None, 48)
    small = pg.font.Font(None, 28)

    state = STATE_MENU
    username = "User"
    host = "127.0.0.1"
    port = 5555

    # Buttons
    join_btn = pg.Rect(360, 300, 180, 60)
    host_btn = pg.Rect(720, 300, 180, 60)

    red_btn = pg.Rect(360, 300, 180, 100)
    green_btn = pg.Rect(720, 300, 180, 100)
    back_btn = pg.Rect(30, 30, 100, 40)

    # Network threads
    client_thread = None
    server_thread = None

    # State display
    red_count = 0
    green_count = 0

    running = True
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                if state in (STATE_CLIENT, STATE_SERVER):
                    state = STATE_MENU
                    if client_thread:
                        client_thread.stop()
                        client_thread = None
                    if server_thread:
                        server_thread.stop()
                        server_thread = None
                else:
                    running = False
            elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
                if state == STATE_MENU:
                    if join_btn.collidepoint(e.pos):
                        client_thread = Client(username, host, port)
                        client_thread.start()
                        state = STATE_CLIENT
                    elif host_btn.collidepoint(e.pos):
                        server_thread = Server(host, port)
                        server_thread.start()
                        state = STATE_SERVER
                elif state == STATE_CLIENT:
                    if red_btn.collidepoint(e.pos):
                        client_thread.send_text(f"{username}|RED")
                    elif green_btn.collidepoint(e.pos):
                        client_thread.send_text(f"{username}|GREEN")
                    elif back_btn.collidepoint(e.pos):
                        state = STATE_MENU
                        client_thread.stop()
                        client_thread = None
                elif state == STATE_SERVER:
                    if back_btn.collidepoint(e.pos):
                        state = STATE_MENU
                        server_thread.stop()
                        server_thread = None

            elif e.type == NETWORK_EVENT and state == STATE_CLIENT:
                sender, text = e.payload
                # Example text: "RED:5|GREEN:3"
                if text.startswith("RED:"):
                    parts = text.split("|")
                    red_count = int(parts[0].split(":")[1])
                    green_count = int(parts[1].split(":")[1])

        # Draw
        screen.fill(WHITE)
        if state == STATE_MENU:
            title = font.render("Clue-Less", True, BLACK)
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))
            draw_button(screen, join_btn, "Join", GRAY, small)
            draw_button(screen, host_btn, "Host", GRAY, small)

        elif state == STATE_CLIENT:
            draw_button(screen, back_btn, "Back", GRAY, small)
            draw_button(screen, red_btn, "RED", RED, font)
            draw_button(screen, green_btn, "GREEN", GREEN, font)

            # Display current counts
            ctext = font.render(f"Red: {red_count}   Green: {green_count}", True, BLACK)
            screen.blit(ctext, (WIDTH // 2 - ctext.get_width() // 2, 150))

        elif state == STATE_SERVER:
            draw_button(screen, back_btn, "Back", GRAY, small)
            title = font.render("Server Counts", True, BLACK)
            screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 150))

            if server_thread:
                r = server_thread.counts["RED"]
                g = server_thread.counts["GREEN"]
                ctext = font.render(f"Red: {r}   Green: {g}", True, BLACK)
                screen.blit(ctext, (WIDTH // 2 - ctext.get_width() // 2, 250))

        pg.display.flip()
        clock.tick(60)

    if client_thread:
        client_thread.stop()
    if server_thread:
        server_thread.stop()
    pg.quit()


if __name__ == "__main__":
    main()
