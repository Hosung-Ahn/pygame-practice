import pygame
import sys
import random

from maze_maker import make_maze

BLACK = (0,0,0)
CYAN = (0,255,255)
GRAY = (96,96,96)

R = 9
C = 11
L = 48
maze = [[0 for _ in range(C)] for _ in range(R)]

DR = R*3
DC = C*3
dungeon = [[0 for _ in range(DC)] for _ in range(DR)]

imgWall = pygame.image.load("RPG/images/wall.png")
imgFloor = pygame.image.load("RPG/images/floor.png")

def make_dungeon() :
    dr = [0,1,0,-1] 
    dc = [-1,0,1,0]
    
    make_maze(maze)
    
    for r in range(DR) :
        for c in range(DC) :
            dungeon[r][c] = 9
            
    for r in range(1, R-1) :
        for c in range(1, C-1) : 
            gr = r*3 + 1
            gc = c*3 + 1
            if maze[r][c] == 0 : 
                if random.randint(0,99) < 20 :
                    for i in range(-1,2) :
                        for j in range(-1,2) :
                            dungeon[gr+i][gc+j] = 0
                else :
                    dungeon[gr][gc] = 0
                    for d in range(4) :
                        if maze[r+dr[d]][c+dc[d]] == 0 :
                            dungeon[gr+dr[d]][gc+dc[d]] = 0
                
    
def main() :
    pygame.init()
    pygame.display.set_caption("던전 생성")
    screen = pygame.display.set_mode((1056, 432))
    clock = pygame.time.Clock()
    
    make_dungeon()
    
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    make_dungeon()
                    
            for r in range(R) :
                for c in range(C) :
                    if maze[r][c] == 0 :
                        pygame.draw.rect(screen, CYAN, [c*L, r*L, L,L])
                    else :
                        pygame.draw.rect(screen, GRAY, [c*L, r*L, L,L])
                        
            for r in range(DR) :
                for c in range(DC) :
                    if dungeon[r][c] == 0 :
                        screen.blit(imgFloor, [c*16+528, r*16])
                    if dungeon[r][c] == 9 :
                        screen.blit(imgWall, [c*16+528, r*16])
                        
        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__' :
    main()