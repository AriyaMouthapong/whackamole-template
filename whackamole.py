import pygame
import random
# comment

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:

        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 512)))
        clock = pygame.time.Clock()
        running = True
        randomx = 0
        randomy = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")
            for i in range(1, 20):
                pygame.draw.line(screen, "black", start_pos=(i * 32, 0), end_pos=(i * 32, 512))

            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    "black",
                    start_pos=(0, i * 32),
                    end_pos=(640, i * 32)
                )
            screen.blit(mole_image, mole_image.get_rect(topleft=(randomx*32,randomy*32)))
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                x = x//32
                y = y//32
                if (randomx, randomy) == (x,y):
                    randomx = random.randrange(0,20)
                    randomy = random.randrange(0, 15)
                    screen.blit(mole_image, mole_image.get_rect(topleft=(randomx, randomy)))

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
