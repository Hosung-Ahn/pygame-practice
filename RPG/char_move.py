import pygame
import sys
import random

from dungeon_maker import make_dungeon

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

pl_r = 4
pl_c = 4

imgWall = pygame.image.load("RPG/images/wall.png")
imgFloor = pygame.image.load("RPG/images/floor.png")
imgPlayer = pygame.image.load("RPG/images/player.png")

def draw_dungeon(bg) :
    bg.fill(BLACK)
    for r in range(-5,6) :
        for c in range(-5, 6) :
            # 화면 좌표
            gr = (r+5) * 16
            gc = (c+5) * 16
            
            # 게임상 좌표
            pr = pl_r + r
            pc = pl_c + c
            if 0 <= pr < DR and 0 <= pc < DC :
                if dungeon[pr][pc] == 0 : 
                    bg.blit(imgFloor, [gc,gr])
                if dungeon[pr][pc] == 9 :
                    bg.blit(imgWall, [gc,gr])
            if r == 0 and c == 0 :
                bg.blit(imgPlayer, [gc, gr-8])
                
def move_player() :
    global pl_r, pl_c
    key = pygame.key.get_pressed()
    
    if key[pygame.K_UP] and dungeon[pl_r-1][pl_c] != 9 : pl_r -= 1
    if key[pygame.K_DOWN] and dungeon[pl_r+1][pl_c] != 9 : pl_r += 1
    if key[pygame.K_LEFT] and dungeon[pl_r][pl_c-1] != 9 : pl_c -= 1
    if key[pygame.K_RIGHT] and dungeon[pl_r][pl_c+1] != 9 : pl_c += 1
    
        
                
            

def main() :
    pygame.init()
    pygame.display.set_caption("던전 내 걷기")
    screen = pygame.display.set_mode((176, 176))
    clock = pygame.time.Clock()
    
    make_dungeon(dungeon)
    
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
                
        draw_dungeon(screen)
        move_player()
        pygame.display.update()
        clock.tick(10)
    
if __name__ == '__main__' :
    main()