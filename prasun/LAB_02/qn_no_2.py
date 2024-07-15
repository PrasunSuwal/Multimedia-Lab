# A Program to produce animation effect of triangle transformation into square and then into circle:

import pygame
import time

def main():
    pygame.init()
    gd = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Polygon Animation")

    poly = [(250, 200), (200, 300), (300, 300), (250, 200)]
    color = (0, 0, 255)
    fill_color = (255, 0, 0)

    # Draw the initial polygon
    pygame.draw.polygon(gd, fill_color, poly)
    pygame.display.flip()
    time.sleep(1)

    # Animate the polygon
    for c in range(1, 51):
        poly[0] = (poly[0][0] - 1, poly[0][1])
        poly[3] = (poly[3][0] + 1, poly[3][1])
        gd.fill((255, 255, 255))
        pygame.draw.polygon(gd, fill_color, poly)
        pygame.display.flip()
        time.sleep(0.1)

    # Draw the circles
    for c in range(1, 26):
        pygame.draw.circle(gd, (0, 255, 0), (250, 250), 75 - c)
        pygame.display.flip()
        time.sleep(0.009)

    time.sleep(1)
    pygame.quit()

if __name__ == "__main__":
    main()