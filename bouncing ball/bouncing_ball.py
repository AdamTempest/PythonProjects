import sys, pygame, time
pygame.init()

size = width, height = 1000, 500
speed = [1,1]
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

def play():
	with open('bounce sound.ogg') as file:
		pygame.mixer.music.load(file,'ogg')
		pygame.mixer.music.play()
		time.sleep(0.2)
		pygame.mixer.music.unload()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)

	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		play()

	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		play()

	screen.fill(black)
	screen.blit(ball,ballrect)
	pygame.display.flip()