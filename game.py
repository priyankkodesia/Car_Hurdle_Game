import pygame
import time
pygame.init()

# window size

window_height = 800
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

	x = (window_height*0.45)
	y = (window_width * 0.8)

	gameExit = False
	x_change = 0

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
		car(x,y)

		if x > window_width - 45 or x < 0:
			crash()

		pygame.display.update()
		clock.tick(60)

game_loop()
pygame.quit()
quit()
