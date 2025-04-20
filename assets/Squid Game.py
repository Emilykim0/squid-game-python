
# 필요한 모듈 불러오기
import pygame,sys

# import * 에서 '*'은 all과 같은 의미
from pygame.locals import *

#-----------------------------------------------------------------------------------------
# 시작 화면 함수
def game_start():  
    ## [1] 화면 크기 600*800
    start_screen_w=600
    start_screen_h=800
    start_screen = pygame.display.set_mode((start_screen_w,start_screen_h))

    ## [2] 게임 창 제목 설정
    pygame.display.set_caption("무궁화 꽃이 피었습니다")

    ## [3] 제목 이미지
    ## 오징어 게임 글자 object 만들기
    squidText_w=120
    squidText_h=50
    # pygame.Rect(left,top,width,height) - 객체의 위치와 크기
    squidText_object=pygame.Rect(start_screen_w-squidText_w-25,25,squidText_w,squidText_h)
    # 이미지 불러오기
    squidText_img=pygame.image.load('squid text_1.png')
    # 이미지를 객체 크기에 맞춰 조정하기
    squidText_img=pygame.transform.scale(squidText_img,(squidText_w,squidText_h))
    
    ## 무궁화 글자 object 만들기
    mugungText_w=550
    mugungText_h=220
    mugungText_object=pygame.Rect(25,25,mugungText_w,mugungText_h)
    mugungText_img=pygame.image.load('squid text_.png')
    mugungText_img=pygame.transform.scale(mugungText_img,(mugungText_w,mugungText_h))

    ## [4] 폰트 설정
    # 색깔 변수
    black=(0,0,0)
    pink=(237,27,118)
    white=(255,255,255)
    
    pygame.font.init()

    start_font_title = pygame.font.SysFont('malgungothic',30,True) ## 소제목 폰트 설정
    start_font_content = start_font6 = pygame.font.SysFont('malgungothic',25,True) ## 본문 폰트 설정
    
    start_msg1= "[ 게임 방법 ]"
    start_msg1_object=start_font_title.render(start_msg1,True,pink)
    
    start_msg2= "[ 게임 시작 ]"
    start_msg2_object=start_font_title.render(start_msg2,True,pink)
    
    # render() 함수는 줄바꿈이 안됨 -> list, for문 사용해서 blit하기
    start_msg3List= ["▶ 방향키(←,↑,↓,→)로 이동하세요!","▶ 영희가 돌아보면 멈춰야 합니다!","▶ 30초 안에 결승선을 통과하면 성공입니다!"]
    
    start_msg4= "게임을 시작하려면 Space 바를 누르세요."
    start_msg4_object=start_font_content.render(start_msg4,True,black)
    
    ## [5] 사운드 설정하기
    ## 다음 코드 세트로 묶어서 사용
    pygame.mixer.pre_init(22050,-16,2,512)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050,-16,2,512)

    ## [6] 배경 음악 설정
    start_bgm=pygame.mixer.music
    start_bgm.load("Way Back then.mp3")
    start_bgm.play(-1) # 연속 재생
    start_bgm.set_volume(0.5) # 소리 범위: 가장 큰소리 1 ~ 가장 작은소리 0.1
    

    ## 루프
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                return
            
        start_screen.fill(white)
        
        ## 제목 그리기 - 이미지 2개
        start_screen.blit(mugungText_img,mugungText_object)
        start_screen.blit(squidText_img,squidText_object)
        
        ## 글자 그리기
        start_screen.blit(start_msg1_object,(25,300))
        start_screen.blit(start_msg2_object,(25,550))
        
        ## !!! 여러줄 글자 그리기 !!! enumerate(리스트) -> (인덱스,리스트 요소)
        for i, start_msg3 in enumerate(start_msg3List):
            start_msg3_object=start_font_content.render(start_msg3,True,black) 
            start_screen.blit(start_msg3_object,(25,350+i*50)) ## y축을 인덱스 별로 증가하게 만들기
            
        start_screen.blit(start_msg4_object,(25,600))
        
        pygame.display.update()
        
    
#-----------------------------------------------------------------------------------------

# 성공재시작 화면 함수
def game_sucess():
    ## [1] 화면 만들기 600*800
    sucess_screen_w=600
    sucess_screen_h=800
    sucess_screen = pygame.display.set_mode((sucess_screen_w,sucess_screen_h))
    
    # 색깔 변수 저장하기
    pink=(237,27,118)
    white=(255,255,255)
    black=(0,0,0)
    
    ## [2] 폰트 설정
    pygame.font.init()
    sucess_font1=pygame.font.SysFont('malgungothic',150,True)
    sucess_msg1="성 공 !"
    sucess_msg1_object=sucess_font1.render(sucess_msg1,True,pink)
    sucess_msg1_rect = sucess_msg1_object.get_rect() # object를 사각형으로
    sucess_msg1_rect.center = (300,300) # 메시지 사각 객체의 중심 위치를 지정
    
    sucess_font2=pygame.font.SysFont('malgungothic',30,True)
    sucess_msg2="다시 시작하려면 Space 바를 누르세요"
    sucess_msg2_object=sucess_font2.render(sucess_msg2,True,black)
    sucess_msg2_rect = sucess_msg2_object.get_rect() # object를 사각형으로
    sucess_msg2_rect.center = (300,450) 
    
    ## [3] 사운드 설정하기
    ## 다음 코드 세트로 묶어서 사용
    pygame.mixer.pre_init(22050,-16,2,512)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050,-16,2,512)

    ## [3] 배경 음악 설정
    # pygame.mixer.music -> 한번에 한 음원
    # pygame.mixer.Sound(file) -> 여러 음원, Sound는 클래쓰
    ## 오징어 게임 bgm
    sucess_bgm1=pygame.mixer.Sound("Way Back then.mp3")
    sucess_bgm1.play(-1) # 연속 재생
    sucess_bgm1.set_volume(0.5) # 소리 범위: 가장 큰소리 1 ~ 가장 작은소리 0.1
    
    ## 돈 올라가는 bgm 1번만(기본값)
    sucess_bgm2=pygame.mixer.Sound("money.mp3")
    sucess_bgm2.play() 
    sucess_bgm2.set_volume(0.8)
    
    ## 루프
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and event.key == K_SPACE:
                game_play()
        sucess_screen.fill(white)
        sucess_screen.blit(sucess_msg1_object,sucess_msg1_rect)
        sucess_screen.blit(sucess_msg2_object,sucess_msg2_rect)
        
        pygame.display.update()
        
#-----------------------------------------------------------------------------------------
# 실패재시작 화면 함수
def game_fail():
    ## [1] 화면 만들기 600*800
    fail_screen_w=600
    fail_screen_h=800
    fail_screen = pygame.display.set_mode((fail_screen_w,fail_screen_h))
    
    # 색깔 변수 저장하기
    pink=(237,27,118)
    black=(0,0,0)
    
    ## [2] 폰트 설정
    pygame.font.init()
    fail_font1=pygame.font.SysFont('malgungothic',150,True)
    fail_msg1="실 패 !"
    fail_msg1_object=fail_font1.render(fail_msg1,True,pink)
    fail_msg1_rect = fail_msg1_object.get_rect() # object를 사각형으로
    fail_msg1_rect.center = (300,300) # 메시지 사각 객체의 중심 위치를 지정
    
    fail_font2=pygame.font.SysFont('malgungothic',30,True)
    fail_msg2="다시 시도하려면 Space 바를 누르세요"
    fail_msg2_object=fail_font2.render(fail_msg2,True,pink)
    fail_msg2_rect = fail_msg2_object.get_rect() # object를 사각형으로
    fail_msg2_rect.center = (300,450) 

    ## [3] 사운드 설정하기
    ## 다음 코드 세트로 묶어서 사용
    pygame.mixer.pre_init(22050,-16,2,512)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050,-16,2,512)

    ## [3] 배경 음악 설정
    ## 총소리 bgm
    fail_bgm=pygame.mixer.music
    fail_bgm.load("총소리 효과음.mp3")
    fail_bgm.play(1) # 연속 재생
    fail_bgm.set_volume(0.5)

    ## 루프
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == KEYDOWN and event.key == K_SPACE:
                game_play()

        fail_screen.fill(black)
        fail_screen.blit(fail_msg1_object,fail_msg1_rect)
        fail_screen.blit(fail_msg2_object,fail_msg2_rect)
        
        pygame.display.update()

 
#-----------------------------------------------------------------------------------------
# 게임 시작 함수
def game_play():
    ## 게임은 항상 초기화를 시켜줘야함!!
    pygame.init()

    ## [1] 화면 크기 600*800 ----------------------------------------------------------------
    screen_width=600
    screen_height=800
    screen = pygame.display.set_mode((screen_width,screen_height))


    ## [2] 게임 창 제목 설정-------------------------------------------------------------------
    pygame.display.set_caption("무궁화 꽃이 피었습니다")

    ## [3] 배경 이미지 정하기------------------------------------------------------------------
    backgraoundImg = pygame.image.load('backgroundImg.png')
    ## 배경이미지를 게임창 크기에 맞춰 변형 후 저장
    backgraoundImg = pygame.transform.scale(backgraoundImg,(screen_width,screen_height))

    ## [4] 플레이어 object 만들기--------------------------------------------------------------------
    player_w=50
    player_h=70
    # pygame.Rect(left,top,width,height) - 객체의 위치와 크기
    player_object=pygame.Rect((screen_width-player_w)/2,screen_height-player_h,player_w,player_h)
    # 이미지 불러오기
    player_img=pygame.image.load('player.png')
    # 이미지를 객체 크기에 맞춰 조정하기
    player_img=pygame.transform.scale(player_img,(player_w,player_h))


    ## [5] 관리자 object 만들기 - 오른쪽 왼쪽 ---------------------------------------------------------
    manager_w=(screen_width-80)/2
    manager_h=100

    # 객체의 위치와 크기
    managerL_object=pygame.Rect(0,120,manager_w,manager_h) ## 왼쪽
    managerR_object=pygame.Rect(screen_width-manager_w,120,manager_w,manager_h) ## 오른쪽
    # 이미지 불러오기
    managerL_img=pygame.image.load('manager2.png')
    managerR_img=pygame.image.load('manager2.png')
    # 이미지를 객체 크기에 맞춰 조정하기
    managerL_img=pygame.transform.scale(managerL_img,(manager_w,manager_h))
    managerR_img=pygame.transform.scale(managerR_img,(manager_w,manager_h))

    ## [6] 영희 object 만들기-----------------------------------------------------------------------
    # 영희 크기
    yeonghee_w=200
    yeonghee_h=200
    
    ## 영희 object
    yeonghee_object=pygame.Rect((screen_width-yeonghee_w)/2,20,yeonghee_w,yeonghee_h)
    
    ## 그림 가져오기 및 조정 - 앞영희
    yeongheeF_img=pygame.image.load('yeonghee_F.png')
    yeongheeF_img=pygame.transform.scale(yeongheeF_img,(yeonghee_w,yeonghee_h))

    ## 그림 가져오기 및 조정 - 앞영희
    yeongheeB_img=pygame.image.load('yeonghee_B.png')
    yeongheeB_img=pygame.transform.scale(yeongheeB_img,(yeonghee_w,yeonghee_h))

    ## [7] 벌 object 만들기--------------------------------------------------------------------
    bee_w=50
    bee_h=50

    ## 오른쪽 벌 - 왼쪽에서 오른쪽으로 이동
    beeR_object = pygame.Rect(0,350,bee_w,bee_h)
    beeR_img=pygame.image.load("bee2.png")
    beeR_img=pygame.transform.scale(beeR_img,(bee_w,bee_h))
    
    ## 왼쪽 벌 - 오른쪽에서 왼쪽으로 이동   
    beeL_object = pygame.Rect(screen_width-bee_w,600,bee_w,bee_h)   
    beeL_img=pygame.image.load("bee1.png")
    beeL_img=pygame.transform.scale(beeL_img,(bee_w,bee_h))
        

    ## [8] 폰트 object 생성-------------------------------------------------------------------------
    pygame.font.init()
    font=pygame.font.SysFont('Arial',30,True) # 'Arial'체, 크기 30, bold

    ## [9] 시간 변수들 설정---------------------------------------------------------------------------
    total_time=30
    start_time=pygame.time.get_ticks() # 게임루프 밖에 있어서 한번 정해지면 변경되지 않는 고정 값

    ## [10] 사운드 설정하기-------------------------------------------------------------------------
    ## 다음 코드 세트로 묶어서 사용
    pygame.mixer.pre_init(22050,-16,2,512)
    pygame.init()
    pygame.mixer.quit()
    pygame.mixer.init(22050,-16,2,512)

    ## [11] 배경 음악 설정-------------------------------------------------------------------------
    game_bgm=pygame.mixer.music
    game_bgm.load("무궁화.mp3")
    game_bgm.play(-1) # 연속 재생
    game_bgm.set_volume(0.5) # 소리 범위: 가장 큰소리 1 ~ 가장 작은소리 0.1


    # 게임 설정 변수----------------------------------------------------------------------------------
    clock=pygame.time.Clock()
    player_speed=0.05
    bee_speed=0.1

    #-----------------------------------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------
    ## 게임 루프
    while True:
        # [필수] 1초에 몇 프레임으로 보여질 것인지 결정
        dt=clock.tick(60)
        # [필수] 게임 종료 조건 - 창을 닫기 버튼(X)을 누를 경우
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # [1] 키보드 객체 만들기
        KeyInput=pygame.key.get_pressed()
        ## 상하좌우 움직이기, 벽에 닿으면 움직이지 않기 즉, 벽에 닿기 전까지 움직이기
        ## elif 말고 if 문으로만 구성해야 방향키를 동시에 눌렀을 때 동시에 움직임 가능 - 부드러운 움직임
        ## 왼쪽 이동은 좌표 x값이 작아져야하니 (-) , 오른쪽 이동은 좌표 x값이 커져야 하니 (+)
        ## 위로 이동은 좌표 y값이 작아져야하니 (-) , 아래로 이동은 좌표 y값이 커져야 하니 (+)
        if KeyInput[K_LEFT] and player_object.left>=0: 
            player_object.left -= player_speed*dt # dt를 곱해줘야 각 컴퓨터에서 동일한 속도로 부드럽게 움직임
        if KeyInput[K_RIGHT] and player_object.right<=screen_width:
            player_object.right += player_speed*dt 
        if KeyInput[K_UP] and player_object.top>=0: 
            player_object.top -= player_speed*dt # dt를 곱해줘야 각 컴퓨터에서 동일한 속도로 부드럽게 움직임
        if KeyInput[K_DOWN] and player_object.bottom<=screen_height:
            player_object.bottom += player_speed*dt     
        
        
        # [2] 게임 창에 배경사진 그리기
        screen.blit(backgraoundImg,(0,0))
        # [3] 플레이어 그리기
        screen.blit(player_img,player_object)
        # [4] 관리자 그리기
        screen.blit(managerR_img,managerR_object)
        screen.blit(managerL_img,managerL_object)
        # [5]결승선 그리기 - y좌표 210
        pygame.draw.line(screen, (0,0,0), (0, 210), (screen_width, 210), width=1)
        
        # [6] 벌 그리기 및 움직이기 
        # 왼->오 벌
        beeR_object.x += bee_speed*dt
        screen.blit(beeR_img,beeR_object)
        # 화면을 벗어나면 x,y좌표 초기화
        if beeR_object.right > screen_width:
            beeR_object.update(0,350,bee_w,bee_h)
        
        # 오->왼 벌
        beeL_object.x -= bee_speed*dt
        screen.blit(beeL_img,beeL_object)
        # 화면을 벗어나면 x,y좌표 초기화
        if beeL_object.left < 0:
            beeL_object.update(screen_width-bee_w,600,bee_w,bee_h)
          
        # [7-1] 경과 시간 계산
        ## elapsed_time의 pygame.time.get_ticks()는 게임 루프 안에서 정의 되었기 때문에 계속 업그레이드 되는 값.
        ## 1000ms -> 1초, 나눗셈을 하면 float 타입
        elapsed_time=(pygame.time.get_ticks() - start_time)/1000 
        ## 시간이 0보다 작아지지 않도록 -> max(0,시간)
        remain_time=max(0,int(total_time-elapsed_time))
        
        # [7-2] 타이머 그리기
        ## render() 함수 -> 글자 디자인 설정 
        time_msg=font.render(f"TIMER: {remain_time}s",True,(255,0,0))
        ## time_msg의 가로 길이 가져오기 -> get_width()
        screen.blit(time_msg,((screen_width-time_msg.get_width())/2,0))
        
        
        # [8] [무궁화 꽃이 피었습니다 게임 룰]----------------------------------
        
        # (1) 영희 그리기 및 bgm 넣었다 끄기 및 돌아봤을 떄 key감지 되면 탈락
        # - 반복문 : 5초동안 영희뒤 -> 3초동안 영희 앞
        
        ## 8초 주기로 상태 변경 -> 8로 나눈 나머지 값(0~7) 이용하기
        time_yh=elapsed_time%8
        
        # 5초동안 영희 뒷모습
        if time_yh <= 5:
            screen.blit(yeongheeB_img,yeonghee_object)
            # 음악이 정지되어 있다면, 다시 재생
            if not pygame.mixer.music.get_busy(): 
                game_bgm.play(-1)
                         
        # 3초 동안 영희 앞모습 -> 멈춰라!
        else:
            screen.blit(yeongheeF_img,yeonghee_object)
            game_bgm.stop()
            # key를 누르면 -> 게임 실패     
            for event in pygame.key.get_pressed(): # 눌려져 있으면
                if KeyInput[K_DOWN] or KeyInput[K_UP] or KeyInput[K_LEFT] or KeyInput[K_RIGHT] :
                    game_fail()
            
            
        # (2) 남은 시간에 따른 게임 룰   
        # remain_time >0 일 떄
        if remain_time > 0:
            # player가 결승선에 도달하면 게임 성공
            if player_object.bottom <= 210: # 결승선 y축 210
                game_bgm.stop()
                game_sucess()
                       
        # player가 시간이 다되었을 떄 -> 결승선 밑이면 게임 실패
        if remain_time==0:
            if player_object.bottom > 210:
                game_fail()
            
        # (3) 벌에 충돌하면 실패
        if player_object.colliderect(beeR_object) or player_object.colliderect(beeL_object):
            game_fail()
        
        
        # [필수] 게임은 항상 화면이 업데이트 되어야함!!
        pygame.display.update()

game_start()
game_play()

