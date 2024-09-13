import pygame
import sys
import math
import random
import time
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CIRCLE_RADIUS = 100
NUM_SEGMENTS = 6
SEGMENT_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
ROTATION_SPEED = 15  # Adjust this value to control rotation speed

# Create a window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rotating Circle")

# Calculate segment angle
segment_angle = 2 * math.pi / NUM_SEGMENTS

# Initial rotation angle
rotation_angle = 0

# Random duration to stop (between 5 and 12 seconds)
stop_duration = random.uniform(5, 12)
start_time = time.time()

# Color of the stopped segment
stopped_segment_color = None

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the rotating circle
    for i in range(NUM_SEGMENTS):
        start_angle = i * segment_angle + rotation_angle
        end_angle = (i + 1) * segment_angle + rotation_angle
        pygame.draw.arc(screen, SEGMENT_COLORS[i], (SCREEN_WIDTH // 2 - CIRCLE_RADIUS, SCREEN_HEIGHT // 2 - CIRCLE_RADIUS, 2 * CIRCLE_RADIUS, 2 * CIRCLE_RADIUS), start_angle, end_angle, CIRCLE_RADIUS)

    # Draw an arrow pointing up at the center
    arrow_length = 60
    arrow_tip = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 )
    arrow_left = (arrow_tip[0] - 5, arrow_tip[1] + 10)
    arrow_right = (arrow_tip[0] + 5, arrow_tip[1] + 10)
    pygame.draw.line(screen, (0, 0, 0), arrow_tip, arrow_left, 2)
    pygame.draw.line(screen, (0, 0, 0), arrow_tip, arrow_right, 2)

    # Update rotation angle
    rotation_angle += math.radians(ROTATION_SPEED)

    # Check if it's time to stop
    if time.time() - start_time >= stop_duration:
        stopped_segment_color = SEGMENT_COLORS[int(rotation_angle / segment_angle) % NUM_SEGMENTS]
        running = False

    # Update display
    pygame.display.flip()
    clock.tick(60)  # Limit frame rate
    ROTATION_SPEED-=((ROTATION_SPEED/stop_duration)*0.05)
# Display the color of the stopped segment
font = pygame.font.Font(None, 36)
text_surface = font.render(f"Stopped Segment Color: {stopped_segment_color}", True, (0, 0, 0))
screen.blit(text_surface, (10, 10))
pygame.display.flip()

# Continue running without quitting
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()