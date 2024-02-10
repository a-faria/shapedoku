import pygame

# def main():
    # initialize the pygame module
pygame.init()
pygame.display.set_caption("SudoShape")

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
# Predefined some colors
BLUE  = (0, 153, 153)
YELLOW = (220, 220, 0)
RED   = (255, 0, 0)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

WHITE = (255, 255, 255)
font1 = pygame.font.SysFont("comicsans", 40)

x = 0
y = 0
dif = 400 / 4
val = 0
grid =[
    [1, 0, 0, 4],
    [2, 1, 4, 3],
    [4, 3, 1, 0],
    [3, 0, 2, 1]
]
input_shp = [1,2,3,4]

# create a surface on screen that has the size of 240 x 180
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
running = True
img = pygame.image.load('icon.png')
# screen.fill(WHITE)
# screen.blit(img, (33,33))
# pygame.display.flip()
# Highlight the cell selected


def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif
     

def draw_box():
	for i in range(2):
		pygame.draw.line(screen, (RED), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 3)
		pygame.draw.line(screen, (RED), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 3) 

def draw():
    for i in range(4):
        for j in range(4):
            if grid[j][i]!= 0:
                pygame.draw.rect(screen, (BLUE), (i * dif, j * dif, dif + 1, dif + 1))

                # print("bo")
                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[j][i]), 1, (BLACK))
                screen.blit(text1, (i * dif + 40, j * dif + 20)) #display text spacing settings
        pygame.draw.rect(screen, (YELLOW), (i * dif, 400, dif + 1, dif + 1))
        text1 = font1.render(str(input_shp[i]), 1, (BLACK))
        screen.blit(text1, (i * dif + 40, 400 + 20)) 
    # Draw lines horizontally and vertically to form grid		 
    for i in range(6):

        thick = 3
        pygame.draw.line(screen, (GREEN), (0, i * dif), (400, i * dif), thick)
        pygame.draw.line(screen, (GREEN), (i * dif, 0), (i * dif, 500), thick)	

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Get the mouse position to insert number 
    if event.type == pygame.MOUSEBUTTONDOWN:
        flag1 = 1
        pos = pygame.mouse.get_pos()
        get_cord(pos)
    draw()
    draw_box()
    pygame.display.update()

# if __name__=="__main__":
#     main()