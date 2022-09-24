import pygame
import sys

WHITE = (255,255,255)
BLACK = (0,0,0)
CYAN  = (0,255,255)

def main() :
    pygame.init()
    pygame.display.set_caption('첫번째 pygame : 사운드 출력')
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 40)
    
    try :
        # BGM 이 재생상태 또는 정지상태 중 하나이다.
        pygame.mixer.music.load('pygame\sound\pygame_bgm.ogg')
        # BGM 을 재생시킬수 있다. 즉 중복재생 가능하다.
        se = pygame.mixer.Sound('pygame\sound\pygame_se.ogg')
    except :
        print('ogg file 이 맞지 않거나, 오디오 기기와 접속되어 있지 않습니다.')
        
    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
                
        key = pygame.key.get_pressed()
        # p를 눌렀을 때 BGM 이 정지 중이라면
        if key[pygame.K_p] and pygame.mixer.music.get_busy() == False:
            # BGM 재생
            pygame.mixer.music.play(-1)
        # s를 눌렀을 떄 BGM 이 재생중이라면
        if key[pygame.K_s] and pygame.mixer.music.get_busy() == True:
            # BGM 정지
            pygame.mixer.music.stop()
            
        if key[pygame.K_SPACE] :
            se.play()
        
        # 재생시간    
        pos = pygame.mixer.music.get_pos()

        txt1 = font.render(f"BGM pos : {pos}", True, WHITE)
        txt2 = font.render("[P]lay bgm : [S]top bgm : [Space] se", True, CYAN)
        
        screen.fill(BLACK)
        screen.blit(txt1, [100,100])
        screen.blit(txt2, [100,200])
        pygame.display.update()
        clock.tick(10)
        
if __name__ == '__main__' :
    main()