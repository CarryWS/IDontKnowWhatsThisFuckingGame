import pygame
import time
import easygui
import random
import math
import os
#os.system('color a')
#for i in range(10):
#    print('提示：这个黑色窗口是系统控制台！关闭后游戏无法运行！')

speed = float(easygui.enterbox('输入速度:(1-99为低速，100-499为中速，500-999为中高速，1000及以上为高速，输入0则为最高速（某些特定值\
还会触发神秘彩蛋哦（迫真）))','设置速度'))
if speed!=0:
    sleep_time = 1/speed
else:
    sleep_time = 0
def play_BGM(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(start = 0.0)
#picture_path = easygui.fileopenbox('Choose a picture file:','Choose a picture file:')
pygame.init()
screen = pygame.display.set_mode((600,400))
pygame.display.set_caption('这是给人玩的？（作者：CarryWS）')

start_time = time.time()
time_mark_font = pygame.font.Font('C:\\Windows\\Fonts\\simhei.ttf',25)
time_mark = time_mark_font.render('计时器: '+str(start_time - time.time()),True,'white','black')
#elements
#text1 = pygame.image.load(picture_path)
text1 = pygame.image.load('profile.jpg')
position_text1_x = 0
position_text1_y = 0
position_text1_x_mode = 'increase'
position_text1_y_mode = 'increase'
position_text1_x_lenth = 1
position_text1_y_lenth = 1

if speed < 100 and speed != 0:
    play_BGM('LowSpeedBGM.wav')
else:
    if speed >= 100 and speed < 500:
        play_BGM('MidSpeedBGM.wav')
    else:
        if speed <= 500 and speed < 1000 and speed != 0:
            play_BGM('MidHighSpeedBGM.wav')
        else:
            if speed >= 1000 and speed != 114514:
                    play_BGM('HighSpeedBGM.wav')
            else:
                if speed == 114514:
                    play_BGM('114514SpeedBGM.wav')
                else:
                    if speed == 0:
                        play_BGM('FastestSpeedBGM.wav')

#game main loop
while True:
    if position_text1_x_mode == 'increase':
        position_text1_x = position_text1_x + position_text1_x_lenth
    if position_text1_y_mode == 'increase':
        position_text1_y = position_text1_y + position_text1_y_lenth
    if position_text1_x >= 500:
        position_text1_x_mode = 'decrease'
        position_text1_x_lenth = random.randint(100,1000)/100
    if position_text1_y >= 300:
        position_text1_y_mode = 'decrease'
        position_text1_y_lenth = random.randint(100,1000)/100
    if position_text1_x_mode == 'decrease':
        position_text1_x = position_text1_x - position_text1_x_lenth
    if position_text1_y_mode == 'decrease':
        position_text1_y = position_text1_y - position_text1_y_lenth
    if position_text1_x <= 0:
        position_text1_x_mode = 'increase'
        position_text1_x_lenth = random.randint(100,1000)/100
    if position_text1_y <= 0:
        position_text1_y_mode = 'increase'
        position_text1_y_lenth = random.randint(100,1000)/100
    position_text1 = (position_text1_x,position_text1_y)
    screen.blit(text1,position_text1)

    time_mark = time_mark_font.render('计时器: '+str(math.floor(time.time() - start_time))+'s',True,'white','black')
    screen.blit(time_mark,(0,0))
    pygame.display.flip()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
    time.sleep(sleep_time)
    #detect mouse
    mouse_pos_x = pygame.mouse.get_pos()[0]
    mouse_pos_y = pygame.mouse.get_pos()[1]
    if mouse_pos_x >= position_text1_x and mouse_pos_x <= position_text1_x + 100:
        if mouse_pos_y >= position_text1_y and mouse_pos_y <= position_text1_y + 100:
            pygame.mixer.stop()
            play_BGM('DeathSoundEffect.wav')
            last_score = math.floor(time.time() - start_time)
            easygui.msgbox('你寄了!\n最终分数： '+str(last_score)+'s','提示')
            exit()