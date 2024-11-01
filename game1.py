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

# Define global variables to track the current question and game state
current_screen = "lesson_1"
current_question_index = 0
questions = [
    {"question": "What is a variable?", "choices": ["A type of fruit", "A container that holds data"], "answer": 1},
    {"question": "What does a loop do?", "choices": ["Repeat code", "Stop code"], "answer": 0},
    {"question": "What is a function?", "choices": ["A piece of reusable code", "A snack"], "answer": 0},
]
total_questions = len(questions)
click_processed = False  # Variable to track if a click has been processed
feedback = ""  # Store feedback message
show_feedback = False  # Flag to indicate if feedback is being displayed
timer_started = False  # Tracks if the timer for feedback is started

# Function to render text
def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to dynamically calculate button size and render buttons
def draw_button(text, x, y, color, text_color, index=None):
    text_surface = font.render(text, True, text_color)
    text_width, text_height = text_surface.get_size()  # Get text size
    padding = 20  # Add padding around the text
    button_width = text_width + padding * 2
    button_height = text_height + padding

    pygame.draw.rect(screen, color, (x, y, button_width, button_height))
    screen.blit(text_surface, (x + padding, y + padding // 2))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global click_processed, show_feedback

    if x + button_width > mouse[0] > x and y + button_height > mouse[1] > y:
        pygame.draw.rect(screen, (0, 0, 255), (x, y, button_width, button_height), 3)  # Highlight on hover
        if click[0] == 1 and not click_processed and index is not None and not show_feedback:
            click_processed = True  # Register that the click has been processed
            check_answer(index)  # Call the check_answer function with the current index

# Game-specific functions
def start_lesson_1():
    screen.fill(WHITE)
    render_text("Lesson 1: Variables", font, BLACK, 50, 100)
    render_text("A variable is a container that holds data.", font, BLACK, 50, 150)
    draw_button("Next", 600, 500, BLACK, WHITE, index=None)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    global click_processed
    if 600 + 100 > mouse[0] > 600 and 500 + 50 > mouse[1] > 500:
        if click[0] == 1 and not click_processed:
            click_processed = True
            go_to_quiz()

# Go to the quiz screen with the first question
def go_to_quiz():
    global current_screen
    current_screen = "quiz"

# Quiz function to display the current question and choices
def quiz():
    global current_question_index, feedback, show_feedback, click_processed

    screen.fill(WHITE)

    if show_feedback:
        render_text(feedback, font, GREEN if "Correct" in feedback else RED, 600, 10)
        return  # Stop rendering buttons when feedback is being shown

    # Display the next question if available
    if current_question_index < total_questions:
        question_data = questions[current_question_index]
        render_text(question_data["question"], font, BLACK, 100, 100)
        for i, choice in enumerate(question_data["choices"]):
            draw_button(choice, 150, 200 + i * 100, BLACK, WHITE, index=i)
    else:
        render_text("You completed the quiz!", font, GREEN, 100, 100)
        draw_button("Home", 600, 500, BLACK, WHITE, index=None)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 + 100 > mouse[0] > 600 and 500 + 50 > mouse[1] > 500:
            if click[0] == 1 and not click_processed:
                click_processed = True
                go_home()

# Check whether the player's answer is correct
def check_answer(i):
    global current_question_index, feedback, show_feedback, timer_started

    if i == questions[current_question_index]["answer"]:
        feedback = "Correct, +$10"
        current_question_index += 1  # Move to the next question
    else:
        feedback = "Wrong answer! Try again."

    show_feedback = True  # Indicate that feedback is being shown
    timer_started = True  # Feedback timer will start on the next loop

# Function to go back to the main menu (or home)
def go_home():
    global current_screen, current_question_index
    current_screen = "lesson_1"  # Restart the lesson
    current_question_index = 0  # Reset question index

# This function will handle the current game screen (lesson, quiz, etc.)
def handle_game1():
    global current_screen
    if current_screen == "lesson_1":
        start_lesson_1()  # Render the lesson screen
    elif current_screen == "quiz":
        quiz()  # Render the quiz screen
    elif current_screen == "finished":
        screen.fill(WHITE)
        render_text("Quiz Finished! Well Done!", font, GREEN, 300, 250)
        draw_button("Home", 600, 500, BLACK, WHITE)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 600 + 100 > mouse[0] > 600 and 500 + 50 > mouse[1] > 500:
            if click[0] == 1 and not click_processed:
                click_processed = True
                go_home()

# Main loop
def game_loop():
    global click_processed, show_feedback, timer_started

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # If timer is started and feedback is being shown, clear it after 2 seconds
        if show_feedback and timer_started:
            pygame.time.delay(2000)  # 2-second delay to show feedback
            show_feedback = False
            timer_started = False
            click_processed = False  # Reset click state

        handle_game1()
        pygame.display.update()

        clock.tick(60)  # Control the frame rate

# Start the game
if __name__ == "__main__":
    game_loop()
