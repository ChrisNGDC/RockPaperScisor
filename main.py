import random
import pygame

pygame.init()

# Create the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
screen_background_color = (0, 0, 0)

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Rock Paper Scisor")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# Choices
class Choices:
    def __init__(self, name, image, image_selected, selected):
        self.name = name
        self.image = image
        self.image_selected = image_selected
        self.selected = selected


rock = Choices(
    "rock",
    pygame.image.load('rock.png'),
    pygame.image.load('rock_selected.png'),
    False
)


paper = Choices(
    "paper",
    pygame.image.load('paper.png'),
    pygame.image.load('paper_selected.png'),
    False
)


scisor = Choices(
    "scisor",
    pygame.image.load('scisor.png'),
    pygame.image.load('scisor_selected.png'),
    False
)


# Positions
left_x = 240
left_y = screen_height - 64 * 2
center_x = left_x + 64 * 2
center_y = left_y
right_x = center_x + 64 * 2
right_y = center_y

# Score
score_value_wins = 0
score_value_loses = 0
score_value_draws = 0
score_font = pygame.font.Font('batmfa__.ttf', 32)
score_text_x = 10
score_text_y = 10


def show_score(x, y):
    score_wins = score_font.render("Wins : " + str(score_value_wins), True, (255, 255, 255))
    score_loses = score_font.render("Loses : " + str(score_value_loses), True, (255, 255, 255))
    score_draws = score_font.render("Draws : " + str(score_value_draws), True, (255, 255, 255))
    screen.blit(score_wins, (x, y))
    screen.blit(score_loses, (x, y + 32))
    screen.blit(score_draws, (x, y + 64))


def draw(x, y, choice):
    if choice.selected:
        screen.blit(choice.image_selected, (x, y))
    else:
        screen.blit(choice.image, (x, y))


# Logic
def winning_trade(choice):
    win_to = {
        "rock": "scisor",
        "paper": "rock",
        "scisor": "paper",
    }
    return win_to[choice]


def result(player_choice, computer_choice):
    global score_value_wins
    global score_value_loses
    global score_value_draws
    if winning_trade(player_choice) == computer_choice:
        score_value_wins += 1
    if winning_trade(computer_choice) == player_choice:
        score_value_loses += 1
    if player_choice == computer_choice:
        score_value_draws += 1


def computer_input():
    choice_options = ["rock", "paper", "scisor"]
    return random.choice(choice_options)


# Game running
running = True
order = [rock, paper, scisor]
max_choices = len(order) - 1
paper.selected = True
position = 1
while running:
    screen.fill(screen_background_color)
    screen.blit(background, (0, 0))
    show_score(score_text_x, score_text_y)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if position > 0:
                    order[position].selected = False
                    position -= 1
                    order[position].selected = True
            if event.key == pygame.K_RIGHT:
                if position < max_choices:
                    order[position].selected = False
                    position += 1
                    order[position].selected = True
            if event.key == pygame.K_SPACE:
                result(order[position].name, computer_input())

    draw(left_x, left_y, rock)
    draw(center_x, center_y, paper)
    draw(right_x, right_y, scisor)

    pygame.display.update()
