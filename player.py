"""
音楽プレイヤー

pygame.mixer.musicを利用
日本語ドキュメント
http://westplain.sakuraweb.com/translate/pygame/Music.cgi#pygame.mixer.music.pause
"""
import concurrent.futures
import glob
import os
import sys
import time
from random import shuffle

from pygame import mixer

DIR_PATH = "music\\"

class Player:
    def __init__(self):
        self.mp3_list = glob.glob(DIR_PATH + "*.mp3") #testの中のmp3をリスト化
        shuffle(self.mp3_list) #リストをシャッフル
        print(self.mp3_list)

        mixer.init()

        self.in_pause = False

        print("ctrl+c stop")
    
    #TODO:playとloopに分ける
    def loop(self):
        for mp3 in self.mp3_list:
            mixer.music.load(mp3)
            mixer.music.play() 
            print(os.path.splitext(os.path.basename(mp3))[0])
            while mixer.music.get_busy() or self.in_pause:
                time.sleep(1)
    
    def back(self):
        pass

    def skip(self):
        self.unpause()
        mixer.music.stop()
    
    def pause(self):
        self.in_pause = True
        mixer.music.pause()
    
    def unpause(self):
        if self.in_pause:
            self.in_pause = False
            mixer.music.unpause()

    def rewind(self):
        self.unpause()
        mixer.music.rewind()

    def end(self):
        print("end")
        mixer.music.stop()
        sys.exit()

def main():
    player = Player() 
    
    """
    スレッドプール(python 3.2以降)
    https://qiita.com/castaneai/items/9cc33817419896667f34
    """
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(player.loop)
    while True:
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            s = input("入力 skip, end, pause, unpause, rewind:")
            if s == "skip":
                player.skip()
            elif s == "end":
                player.end()
            elif s == "pause":
                player.pause()
            elif s == "unpause":
                player.unpause()
            elif s == "rewind":
                player.rewind()
            else:
                print("キーエラー。終了します")
                player.end()
                break
    

if __name__ == '__main__':
    main()
