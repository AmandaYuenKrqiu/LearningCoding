import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((800, 600))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Function to render text
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to render buttons
def draw_button(text, x, y, width, height, color, text_color, action=None):
    pygame.draw.rect(screen, color, (x, y, width, height))
    render_text(text, font, text_color, x + 10, y + 10)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, width, height), 3)  # Highlight on hover
        if click[0] == 1 and action is not None:
            action()

# Game-specific functions
def start_lesson_2():
    screen.fill(WHITE)
    render_text("Lesson 2: Loops", font, BLACK, 50, 100)
    render_text("A loop allows you to repeat code.", font, BLACK, 50, 150)
    draw_button("Next", 600, 500, 100, 50, GREEN, WHITE, quiz_2)

def quiz_2():
    screen.fill(WHITE)
    render_text("What does a loop do?", font, BLACK, 100, 100)
    draw_button("Repeat code", 150, 200, 300, 50, GREEN, WHITE, correct_answer)
    draw_button("Do nothing", 150, 300, 300, 50, RED, WHITE, wrong_answer)

# Correct answer action
def correct_answer():
    screen.fill(WHITE)
    render_text("Correct!", font, GREEN, 300, 250)

# Wrong answer action
def wrong_answer():
    screen.fill(WHITE)
    render_text("Wrong answer!", font, RED, 300, 250)

# Main function to start game 2
def start_game():
    current_screen = "lesson_2"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if current_screen == "lesson_2":
            start_lesson_2()

        pygame.display.update()
