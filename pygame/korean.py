import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0,0,0)

def main() :
    pygame.init()
    pygame.display.set_caption("Pygame 에서 한국말 표시하기")
    screen = pygame.display.set_mode((800,600))
    clock  = pygame.time.Clock()
    
    # 다음 font 를 사용하면 한국어가 표시된다.
    font = pygame.font.SysFont("malgungothic", 80)
    # 별도 font 사용시
    # font = pygame.font.Font("{font_path}/{font_name}.ttf", 80)
    tmr = 0
    
    while True :
        tmr += 1
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        
        txt = font.render("한국어 표시 : " + str(tmr), True, WHITE)
        screen.fill(BLACK)
        screen.blit(txt, [100,200])
        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__' :
    main()
    