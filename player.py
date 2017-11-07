import glob
import os
import sys
import time
from random import shuffle

from pygame import mixer

DIR_PATH = ""

class Player:
    def __init__(self):
        self.mp3_list = glob.glob(DIR_PATH + "*.mp3") #testの中のmp3をリスト化
        shuffle(self.mp3_list) #リストをシャッフル
        print(self.mp3_list)

        mixer.init()
        print("ctrl+c stop")
    
    def loop(self):
        for mp3 in self.mp3_list:
            mixer.music.load(mp3)
            mixer.music.play() 
            print(os.path.splitext(os.path.basename(mp3))[0])
            try:
                while mixer.music.get_busy(): 
                    time.sleep(1)
            except KeyboardInterrupt:
                self.end()
    
    def skip(self):
        mixer.music.stop()

    def end(self):
        print("end")
        mixer.music.stop()
        sys.exit()

def main():
    Player().loop()

if __name__ == '__main__':
    main()
