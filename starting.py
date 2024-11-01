import pygame
import sys

# Initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Python Coding for Kids')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)

# Define global variables for game state
progress = {"lesson": 1, "score": 0}
lesson_text = ""
current_screen = "main_menu"  # Start with main menu

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
        pygame.draw.rect(screen, BLUE, (x, y, width, height), 3)  # Highlight on hover
        if click[0] == 1 and action is not None:
            action()

# Function to display main menu
def main_menu():
    global current_screen
    screen.fill(WHITE)
    render_text("Python Coding for Kids", title_font, BLACK, 200, 100)
    draw_button("Start Lesson 1", 300, 250, 200, 50, GREEN, WHITE, start_lesson_1)

# Function to display lesson 1
def start_lesson_1():
    global lesson_text, current_screen
    current_screen = "lesson_1"
    lesson_text = "Lesson 1: Variables - A variable is a container that holds data."
    
def lesson_1():
    screen.fill(WHITE)
    render_text(lesson_text, font, BLACK, 50, 100)
    draw_button("Next", 600, 500, 100, 50, GREEN, WHITE, quiz_1)

# Function to display quiz 1
def quiz_1():
    global current_screen
    current_screen = "quiz_1"
    
def quiz_screen_1():
    screen.fill(WHITE)
    render_text("What is a variable?", font, BLACK, 100, 100)
    draw_button("A type of fruit", 150, 200, 300, 50, RED, WHITE, wrong_answer)
    draw_button("A container that holds data", 150, 300, 300, 50, GREEN, WHITE, correct_answer)

# Function for correct answer
def correct_answer():
    global progress, current_screen
    progress['score'] += 10
    progress['lesson'] = 2
    current_screen = "progress"

# Function for wrong answer
def wrong_answer():
    global current_screen
    current_screen = "progress"

# Function to display progress
def progress_screen():
    screen.fill(WHITE)
    render_text(f"Your score: {progress['score']}", font, BLACK, 100, 100)
    draw_button("Next Lesson", 300, 400, 200, 50, GREEN, WHITE, main_menu)

# Main loop
def game_loop():
    global current_screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if current_screen == "main_menu":
            main_menu()
        elif current_screen == "lesson_1":
            lesson_1()
        elif current_screen == "quiz_1":
            quiz_screen_1()
        elif current_screen == "progress":
            progress_screen()

        pygame.display.update()

if __name__ == "__main__":
    game_loop()
