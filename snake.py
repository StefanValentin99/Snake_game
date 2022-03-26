import pygame
import time
import random

pygame.init()

# Used colors
blue = (0, 0, 150)
yellow = (255, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)

display_height = display_width = 800 # dimensions of the display
snake_body = 20 # dimensions of snake body

# Initializing the display

display = pygame.display.set_mode((display_width, display_height))
#display.fill(blue) # setting blue color for the screen
pygame.display.set_caption("Snake Game by Stefan")

# Create clock object to help track time 
clock = pygame.time.Clock()

# Initializing the font for writed stuff
font = pygame.font.Font('freesansbold.ttf', 30)

def game_loop():
    ct = 0
    display.fill(blue)
    pygame.display.update()
    game_running = True
    game_over = False

    # Initializing coordinates for the snake: x and y

    x = display_height / 2 
    y = display_width / 2

    score = 0
    # ?

    snake = []
    snake_length = 1

    # ?
 
    x_new = y_new = 0   # aditional coordinates used to remember last coordinates

    # Initializing coordinates for food and radius 

    radius = snake_body / 3 
    x_food = random.randrange(float(snake_body / 2), float(display_height-snake_body / 2), snake_body)
    y_food = random.randrange(float(snake_body / 2), float(display_width-snake_body / 2), snake_body)

    while game_running: # while game is still running
        while game_over == True: # when you lose
            display.fill(black)
            message1 = pygame.font.Font.render(font, "You lost! :((", True, red)
            message2 = pygame.font.Font.render(font, "Press 'q' to quit or 'r' to retry!", True, red)
            display.blit(message1, [80, display_height/4])
            display.blit(message2, [80, display_height/4 + 40])
            pygame.display.update() # update the display in order to get the options 

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: # if you press q key, the game will close itself
                        game_running = False
                        game_over = False
                    if event.key == pygame.K_r: # if you press r key, the game will reinitialize itself
                        game_loop()
        
        for event in pygame.event.get():  # Making the controls for the snake
            if event.type == pygame.QUIT:
                game_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    x_new = 0
                    y_new = -snake_body
                if event.key == pygame.K_DOWN:
                    x_new = 0
                    y_new = snake_body
                if event.key == pygame.K_RIGHT:
                    x_new = snake_body
                    y_new = 0
                if event.key == pygame.K_LEFT:
                    x_new = -snake_body
                    y_new = 0
        
        if x < 0 or x >= display_width or y < 0 or y >= display_height:
            game_over = True

        x += x_new # We need to update the coordinates of the snake
        y += y_new
        display.fill(blue) # Fill the display in blue so we won't see the precedent coordinates of the snake

        snake_head = []

        pygame.draw.rect(display, yellow, (x, y, snake_body, snake_body)) # generating a snake title
        
        snake_head.append(x)
        snake_head.append(y)
        snake.append(snake_head)

        if len(snake) > snake_length: 
            del snake[0]

        pygame.draw.circle(display, red, (x_food, y_food), radius)  # generating food 

        if x == (x_food - snake_body / 2) and y == (y_food - snake_body / 2):
            x_food = random.randrange(float(snake_body / 2), float(display_height-snake_body / 2), snake_body)
            y_food = random.randrange(float(snake_body / 2), float(display_width-snake_body / 2), snake_body)

            snake_length += 1
            score += 1

        for new in snake[:-1]:      # everytime the snake eat, it should grow one title
            pygame.draw.rect(display, yellow, (new[0], new[1], snake_body, snake_body))
               
            
        message3 = pygame.font.Font.render(font, 'Your score: ' + str(score), True, white)
        display.blit(message3, [0, 0])     
        pygame.display.update()
        
        for body in snake[:-1]:    # if the snake's head coordinates are the same with a set from its body, the game will stop
            if snake[-1] == body: # here snake[-1] is the head of the snake
                game_over = True


        clock.tick(20) # refreshes/second
    
    pygame.quit()
    quit

game_loop()