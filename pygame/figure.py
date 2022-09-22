import pygame
import sys
import math

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
GOLD = (255,216,0)
SILVER = (192,192,192)
COPPER = (192,112,48)

def main() :
    pygame.init()
    pygame.display.set_caption("첫번째 Pygame : 도형")
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    tmr = 0
    
    while True :
        tmr += 1
        for event in pygame.event.get() :
            # 아래 구문을 작성하지 않으면 game 이 꺼지지 않는다 ;; 
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
                
        screen.fill(BLACK)
        
        pygame.draw.line(screen, RED, [0,0], [100,200], 10)
        
        # 3번째 인자값을 True 로 하면 시작지점으로 다시 돌아온다.
        pygame.draw.lines(screen, BLUE, False, [[50,300], [150, 400], [50,500]], 10)
        
        # [x,y,w,h] 좌상단 좌표 x,y 를 기준으로 w,h길이의 사각형을 그린다. 
        pygame.draw.rect(screen, RED, [100, 100, 100, 100])
        pygame.draw.rect(screen, GREEN, [200,200,60,180], 5)
        
        pygame.draw.polygon(screen, BLUE, [[250, 400], [200, 500], [300,500]], 10)
        
        pygame.draw.circle(screen, GOLD, [400, 100], 70)
        
        # [x,y,w,h]
        pygame.draw.ellipse(screen, SILVER, [320, 260, 160, 80])
        pygame.draw.ellipse(screen, COPPER, [360, 420, 80, 160], 20)
        
        ang = math.pi * tmr/36
        
        pygame.draw.arc(screen, BLUE, [500, 100, 200, 400], 0, math.pi*2)
        pygame.draw.arc(screen, WHITE, [500, 100, 200, 400], ang, ang + math.pi/2, 8)
        
        
        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__' :
    main()
                
        