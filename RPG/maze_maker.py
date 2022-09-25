import pygame
import sys
import random

CYAN = (0,255,255)
GRAY = (96,96,96)

R = 9
C = 11
L = 48

maze = [[0 for _ in range(C)] for _ in range(R)]

def make_maze() :
    dr = [0,1,0,-1]
    dc = [-1,0,1,0]
    
    for r in range(R) :
        for c in range(C) :
            maze[r][c] = 0
    
    for r in range(R) :
        maze[r][0] = 1
        maze[r][C-1] = 1
    for c in range(C) :
        maze[0][c] = 1
        maze[R-1][c] = 1
        
    for r in range(2,R-2,2) :
        for c in range(2,C-2,2) :
            maze[r][c] = 1
            if c > 2 : 
                d = random.randint(0,2)
            else :
                d = random.randint(0,3)
                
            maze[r+dr[d]][c+dc[d]] = 1
    
def main() :
    pygame.init()
    pygame.display.set_caption("미로 생성")
    screen = pygame.display.set_mode((528, 432))
    clock = pygame.time.Clock()
    
    make_maze()
    
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_SPACE :
                    make_maze()
                    
            for r in range(R) :
                for c in range(C) :
                    if maze[r][c] == 0 :
                        pygame.draw.rect(screen, CYAN, [c*L, r*L, L,L])
                    else :
                        pygame.draw.rect(screen, GRAY, [c*L, r*L, L,L])
                        
        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__' :
    main()
