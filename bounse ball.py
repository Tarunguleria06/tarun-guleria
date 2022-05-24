import sys, pygame
pygame.init()
a=200
b=200
size = 400,400
speed = [1, 1]
background = 255, 255, 255
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Bouncing ball")


bg = pygame.image.load("1.jpg").convert()


while True:
    a+=1
    b-=1

    if a>380 or a<10:
        a=10
    if b>380 or b<10:
        b=300

    
    screen.blit(bg,[0,0])
    pygame.draw.circle(screen,"red",(200,a),20)
    pygame.draw.circle(screen,"black",(100,b),20)
    pygame.time.delay(4)
	
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
  
    pygame.display.update()

    