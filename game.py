import pygame
import time
import random

pygame.init()

# window size

window_height = 650
window_width  = 600

#color definitions

black = (0,0,0)
white = (255,255,255)
red	  = (255,0,0)
green = (0,255,0)
blue  = (0,0,255)
background = (144,146,150)


# window settings
game_window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Racer")
clock  = pygame.time.Clock()

carImg = pygame.image.load('car2.png')


def hurdles(hurdle_x,hurdle_y,hurdle_width,hurdle_height,color):
	pygame.draw.rect(game_window,color,[hurdle_x,hurdle_y,hurdle_width,hurdle_height])


def car(x,y):
	game_window.blit(carImg,(x,y))


def text_objects(text,font):
	textSurface = font.render(text,True,red)
	return textSurface , textSurface.get_rect()


def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',80)
	TextSurf,TextRect = text_objects(text,largeText)
	TextRect.center = ((window_width/2),(window_height/2))
	game_window.blit(TextSurf,TextRect)

	pygame.display.update()
	time.sleep(2)
	game_loop()


def crash():
	message_display("You crashed")

def game_loop():
	fps =60
	score = 0
	x = (window_height*0.48)
	y = (window_width * 0.90)

	
	x_change = 0

	hurdle_startx = random.randrange(0,window_width)
	hurdle_starty = -600
	hurdle_speed  = 7
	hurdle_width =60
	hurdle_height = 60

	gameExit = False


	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -5

				if event.key == pygame.K_RIGHT:
					x_change = 5

			if event.type == pygame.KEYUP:
				x_change = 0
			

		x += x_change

		game_window.fill(black)

		hurdles(hurdle_startx,hurdle_starty,hurdle_width,hurdle_height,blue)
		hurdle_starty += hurdle_speed

		car(x,y)

		if x > window_width - 45 or x < 0:
			crash()

		if hurdle_starty >  
		if hurdle_starty > window_height:
			hurdle_starty = 0 - hurdle_height
			hurdle_startx = random.randrange(0,window_width-hurdle_width)
 			
 			score += 10
			fps+=10

		pygame.display.update()

		if fps>250:
			fps =250

		clock.tick(fps)
		print(fps)

game_loop()
pygame.quit()
quit()
