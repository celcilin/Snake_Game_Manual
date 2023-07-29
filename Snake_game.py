import pygame 
import time
import random

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
lgreen = (80,255,10)
red = (255,0,0)
blue = (10,80,255)

win_width = 600
win_height = 400

speed = 10

dis = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

block_size = 20

# font = pygame.font.init()
font_style = pygame.font.SysFont(None,50)

clock = pygame.time.Clock()

def draw_snake(snake,size):
    # print(snake,"s1na")
    for x in snake:
        # print(x)
        if x == snake[:-1]:
            pygame.draw.rect(dis,green,[x[0],x[1],size,size])
        else:
            pygame.draw.rect(dis,black,[x[0],x[1],size,size])

def message(msg,color):
    text = font.render("Score: " + str(msg), True, color)
    dis.blit(text, [0, 0])
    # dis.blit(mess , [win_width//2 , win_height//2])


def gameLoop():

    
    score = 0

    x1 = win_width // 2 
    y1 = win_height // 2

    x1_change = 0
    y1_change = 0

    snake = []
    len_of_snake = 1

    foodx = round(random.randrange(0,win_width - block_size) // block_size ) * block_size
    foody = round(random.randrange(0,win_height - block_size) // block_size ) * block_size

    game_over = False
    game_quit = False

    while not game_quit:


        while game_over:

            for evn in pygame.event.get():

                if evn.type == pygame.QUIT:
                    game_quit = True
                    game_over = False

                if evn.type == pygame.KEYDOWN:
                    if evn.key == pygame.K_c:
                        gameLoop()

                    elif evn.key == pygame.K_q:
                        game_quit = True
                        game_over = False




        for evn in pygame.event.get():

            if evn.type == pygame.QUIT:
                    game_quit = True

            if evn.type  == pygame.KEYDOWN:
                if evn.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

                elif evn.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0

                elif evn.key == pygame.K_LEFT:
                    y1_change = 0
                    x1_change = -block_size

                elif evn.key == pygame.K_RIGHT:
                    y1_change = 0
                    x1_change = block_size

        if x1 >= win_width or x1<0 or y1 >= win_height or y1<0:
            game_over = True
                
        x1 += x1_change
        y1 += y1_change

        dis.fill(blue)

        # pygame.draw.rect(dis,green,[x1,y1,block_size,block_size])
        pygame.draw.rect(dis,red,[foodx,foody,block_size,block_size])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake.append(snake_Head)

        if len(snake) > len_of_snake:
            del snake[0]

        for x in snake[:-1]:
            if x == snake_Head:
                game_over = True

        draw_snake(snake,block_size)
        
        message(score,white)

        pygame.display.update()

        # print(x1,foodx,y1,foody)
        if x1 == foodx and y1 == foody:
            len_of_snake += 1
            score += 1
            foodx = round(random.randrange(0,win_width - block_size) // block_size ) * block_size
            foody = round(random.randrange(0,win_height - block_size) // block_size ) * block_size
            f = [[foodx,foody]] 
            if f in snake:
                foodx = round(random.randrange(0,win_width - block_size) // block_size ) * block_size
                foody = round(random.randrange(0,win_height - block_size) // block_size ) * block_size
            # print(score)
            



        clock.tick(speed)

    # message("Lost",red)
    # time.sleep(2)
    pygame.quit()
    quit()

gameLoop()