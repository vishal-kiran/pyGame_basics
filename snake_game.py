import pygame,sys
import random
pygame.init()
fps = 5
clock = pygame.time.Clock()

windowWidth = 500

windowHeight = 500

game_window = pygame.display.set_mode((windowWidth,windowHeight))
background = pygame.image.load('snake.jpg')

snakePosition = [[100,50],[90,50],[80,50]]
block = [100,50]
foodPosition = [random.randrange(0,windowWidth,10), random.randrange(0,windowHeight,10)]

snakeColor = pygame.Color(0,255,0)
foodColor = pygame.Color(255,0,0) # r,g,b

direction = "right"

while True:
    game_window.blit(background,(0,0))
    pygame.draw.rect(game_window, foodColor, [foodPosition[0], foodPosition[1], 10, 10])
    
    for i in snakePosition:
        pygame.draw.rect(game_window, snakeColor, [i[0], i[1], 10, 10])
       
    # Moving the snake forward
    snakePosition.insert(0,list(block)) # Adding an block at the end of the list/array
     # Delete the first block
    if block[0] == foodPosition[0] and block[1] == foodPosition[1]:
       foodPosition = [random.randrange(0,windowWidth,10), random.randrange(0,windowHeight,10)]
    else :
       snakePosition.pop()   
    # Activating the cross button...
    if block[0]<0 or block[0]>windowWidth:
        pygame.quit()
        sys.exit()
    if block[1]<0 or block[1]>windowHeight :
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_a:
                direction = "left"
            if event.key == pygame.K_d:
                direction = "right"
            if event.key == pygame.K_w:
                direction = "up"
            if event.key == pygame.K_s:
                direction = "down"  

    if direction == "right":
        block[0] += 10
    if direction == "left":
        block[0] -= 10
    if direction == "up":
        block[1] -= 10
    if direction == "down":
        block[1] += 10    

    clock.tick(fps)
    pygame.display.update()
