import pygame,math,pygame.locals 
pygame.init()
font = pygame.font.Font('FreeSansBold.ttf', 20)
screen = pygame.display.set_mode((0,0), pygame.locals.RESIZABLE)
w, h = pygame.display.get_surface().get_size()
cx,cy= w//2 ,h//2
width=3
r=300
arcsize= r/8


boundary = 20000
# Run until the user asks to quit
running = True


input_box = pygame.Rect(100, 100, 140, 32)
speedinput = pygame.Rect(420, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
play = False
speed=False
text = '0'
speedtext='1'
done = False
delay=100
degree=int(text)

while running:
    if degree==0:
        degree=0.001
    if degree>360:
        degree /=360 
    radian = math.radians(degree)
    cosx,siny=cx+(r*math.cos(radian)),cy-(r*math.sin(radian))
    secx=cx+(r*(1/math.cos(radian)))
    cosecy=cy-(r*(1/math.sin(radian)))
    

    # Fill the background with white
    screen.fill((255, 255, 255))
    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 0), (cx,cy), r ,width)
    pygame.draw.line(screen,(0,0,0),(0,cy),(w,cy),width)
    screen.blit(font.render('+x', False, (0,0,0)),(w-50,cy-30))
    screen.blit(font.render('-x', False, (0,0,0)),(30,cy-30))
    pygame.draw.line(screen,(0,0,0),(cx,0),(cx,h),width)
    screen.blit(font.render('y', False, (0,0,0)),(cx-30,30))
    screen.blit(font.render('-y', False, (0,0,0)),(cx-30,h-100))
    pygame.draw.line(screen,(0,0,0),(cx,cy),(cosx,siny) ,width)
    
     
    pygame.draw.arc(screen, (0,0,0) , [cx-arcsize,cy-arcsize,arcsize*2,arcsize*2], 0,radian, width)
    screen.blit(font.render(f'{chr(952)} = {degree} ', False, (0,0,0)),((cx+cosx/8)-120,(cy+siny/8)-80))
    pygame.draw.line(screen,(200,0,0),(cosx,cy),(cosx,siny) ,width) #sin
    screen.blit(font.render(f'sin{chr(952)} = {math.sin(radian)} ', False, (200,0,0)),(cosx-30,(((siny-cy))/2)+500))
    pygame.draw.line(screen,(0,200,0),(cx,siny),(cosx,siny) ,width) #cos
    screen.blit(font.render(f'cos{chr(952)} = {math.cos(radian)} ', False, (0,200,0)),(((cosx-cx)/2)+800,siny-50))

    
    screen.blit(font.render(f'sec{chr(952)} = {1/math.cos(radian)} ', False, (200,200,0)),(cosx-30,cy+30))#sec
    screen.blit(font.render(f'cosec{chr(952)} = {1/math.sin(radian)} ', False, (0,200,200)),(cx-30,siny-30))#cosec
   
    if -boundary<secx<boundary:
        pygame.draw.line(screen,(0,0,200),(secx,cy),(cosx,siny) ,width) #tan
        pygame.draw.line(screen,(200,200,0),(secx,cy),(cx,cy) ,width) #sec
    else:
        pygame.draw.line(screen,(0,0,200),(w,siny),(cosx,siny) ,width) #tan
        pygame.draw.line(screen,(200,200,0),(w,cy),(cx,cy) ,width) #sec
    screen.blit(font.render(f'tan{chr(952)} = {math.tan(radian)} ', False, (0,0,200)),(cosx+30,siny+30))
    
    if -boundary<cosecy<boundary:
        pygame.draw.line(screen,(100,100,0),(cx,cosecy),(cosx,siny) ,width) #cot
        pygame.draw.line(screen,(0,200,200),(cx,cy),(cx,cosecy) ,width)#cosec
    else:
        pygame.draw.line(screen,(100,100,0),(cosx,h),(cosx,siny) ,width) #cot
        pygame.draw.line(screen,(0,200,200),(cx,h),(cosx,h) ,width)#cosec
    screen.blit(font.render(f'cot{chr(952)} = {1/math.tan(radian)} ', False, (100,100,0)),(cosx+30,siny-30))
    
    screen.blit(font.render(f'{chr(952)}', False, (0,0,0)),(80,100))
    playbutton=screen.blit(font.render(f'play', False, (0,0,0)),(80,50))

    pygame.time.delay(delay)
    # Flip the display
    pygame.display.flip()
    if play:
        degree+=0.5


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                if playbutton.collidepoint(event.pos):
                    # Toggle the active variable.
                    play = not play
                else:
                    play = False
                if speedinput.collidepoint(event.pos):
                    # Toggle the active variable.
                    speed = not speed
                else:
                    speed = False
                # Change the current color of the input box.
                 
                if active or speed :
                    color = color_active 
                else :
                    color_inactive
        
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                
                    degree=int(text)
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
            if speed:
                if event.key == pygame.K_RETURN:
                    if not speedtext.isdigit():
                        speedtext='1'
                    
                    delay=1000//(1+int(speedtext))
                elif event.key == pygame.K_BACKSPACE:
                    speedtext = speedtext[:-1]
                else:
                    speedtext += event.unicode
    txt_surface = font.render(text, True, color)
    # Resize the box if the text is too long.
    #width1 = max(200, txt_surface.get_width()+10)
    #input_box.w = width1
    # Blit the text.
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    # Blit the input_box rect.
    pygame.draw.rect(screen, color, input_box, 2)
    screen.blit(font.render('speed (0 -1000)', False, (0,0,0)),(250,100))
    screen.blit(font.render(speedtext, True, color), (speedinput.x+5, speedinput.y+5))
    pygame.draw.rect(screen, color, speedinput, 2)
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()