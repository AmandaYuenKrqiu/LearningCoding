import pygame
import sys
import game1
import game2
from character import Character  # Import Character from character.py

# Initialize pygame
pygame.init()

# Set screen size
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Python Coding for Kids')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define fonts
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 48)

# Create the character instance
player_character = Character()

# Define the current screen
current_screen = "main_menu"  # Start at the main menu

# Function to render text
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to render buttons, with centered positioning
def draw_button(text, center_x, y, width, height, color, text_color, action=None):
    x = center_x - width // 2  # Center the button horizontally
    pygame.draw.rect(screen, color, (x, y, width, height))  # Draw the button
    
    # Adjust font size dynamically to fit the button width
    temp_font = font
    while temp_font.size(text)[0] > width - 20 and temp_font.size(text)[1] < height - 10:
        temp_font = pygame.font.Font(None, temp_font.get_height() - 2)  # Reduce font size
    
    # Render the text and center it in the button
    text_surface = temp_font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

    # Check for hover and clicks
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, BLUE, (x, y, width, height), 3)  # Highlight on hover
        if click[0] == 1 and action is not None:
            action()

# Function to display the main menu
def main_menu():
    screen.fill(WHITE)

    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Set button dimensions
    button_width = 200
    button_height = 50
    button_spacing = 30  # Spacing between buttons

    # Calculate vertical position to center buttons
    total_buttons_height = (button_height * 3) + (button_spacing * 2)
    start_y = (screen_height - total_buttons_height) // 2

    # Draw buttons centered horizontally and spaced vertically
    draw_button("Play Game 1", screen_width // 2, start_y, button_width, button_height, BLACK, WHITE, start_game1)
    draw_button("Play Game 2", screen_width // 2, start_y + button_height + button_spacing, button_width, button_height, BLACK, WHITE, start_game2)
    draw_button("Customize Character", screen_width // 2, start_y + 2 * (button_height + button_spacing), button_width, button_height, BLACK, WHITE, customize_character)

# Start Game 1
def start_game1():
    global current_screen
    pygame.time.delay(200)  # Add a slight delay to prevent multiple clicks
    current_screen = "game1"

# Start Game 2
def start_game2():
    global current_screen
    pygame.time.delay(200)  # Add a slight delay to prevent multiple clicks
    current_screen = "game2"

# Customize Character
def customize_character():
    global current_screen
    current_screen = "character"

# Character customization screen
def character_customization():
    screen.fill(WHITE)
    render_text("Customize Your Character", title_font, BLACK, 200, 100)
    render_text(f"Hair Color: {player_character.hair_color}", font, BLACK, 200, 200)
    render_text(f"Outfit: {player_character.outfit}", font, BLACK, 200, 250)
    
    draw_button("Change Hair to Blonde", 300, 350, 200, 50, GREEN, WHITE, lambda: change_hair("Blonde"))
    draw_button("Change Outfit to Sporty", 300, 450, 200, 50, GREEN, WHITE, lambda: change_outfit("Sporty"))
    draw_button("Home", 600, 500, 100, 50, GREEN, WHITE, go_home)

    pygame.display.update()

# Character customization functions
def change_hair(color):
    player_character.change_hair_color(color)

def change_outfit(outfit):
    player_character.change_outfit(outfit)

def go_home():
    global current_screen
    current_screen = "main_menu"  # Return to the main menu when Home is clicked

# Function to handle the main loop and switch between screens
# In main.py
def game_loop():
    global current_screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Check the current screen and render accordingly
        if current_screen == "main_menu":
            main_menu()
        elif current_screen == "game1":
            game1.handle_game1()  # Correctly transition to game1 and manage its flow
        elif current_screen == "game2":
            game2.game_loop()
        elif current_screen == "character":
            character_customization()

        pygame.display.update()

if __name__ == "__main__":
    game_loop()
