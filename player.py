import glob
import sys
import time
from random import shuffle

import pygame

mp3_list = glob.glob("*.mp3") #testの中のmp3をリスト化
shuffle(mp3_list) #リストをシャッフル

print(mp3_list)

pygame.mixer.init()


print("ctrl+c stop")
for mp3 in mp3_list:
    pygame.mixer.music.load(mp3)
    pygame.mixer.music.play() 
    print(mp3)
    try:
        while pygame.mixer.music.get_busy(): 
            pygame.time.Clock().tick(1)
    except KeyboardInterrupt:
        pass
print("end")
pygame.mixer.music.stop() # 再生の終了