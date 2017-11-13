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
        self.music_index = -1
    
    def play(self):
        while self.music_index < len(self.mp3_list)-1:
            print(self.music_index)
            print(len(self.mp3_list))
            self.music_index += 1
            mp3 = self.mp3_list[self.music_index]
            mixer.music.load(mp3)
            mixer.music.play() 
            print(os.path.splitext(os.path.basename(mp3))[0])
            while mixer.music.get_busy() or self.in_pause:
                time.sleep(1)
        print("aaaa")
        self.end()
    
    def back(self):
        if self.music_index < 1:
            return
        self.unpause()
        self.music_index -= 2 #1個前＝最初から　2個前＝前の曲
        mixer.music.stop()

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
        mixer.quit()

def main():
    player = Player() 
    
    """
    スレッドプール(python 3.2以降)
    https://qiita.com/castaneai/items/9cc33817419896667f34
    """
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(player.play)
    print("ctrl+c stop")
    while True:
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            s = input("入力 skip, end, pause, unpause, rewind, back:")
            if s == "skip":
                player.skip()
            elif s == "end":
                player.end()
                return
            elif s == "pause":
                player.pause()
            elif s == "unpause":
                player.unpause()
            elif s == "rewind":
                player.rewind()
            elif s == "back":
                player.back()
            else:
                print("キーエラー。終了します")
                player.end()
                return
    

if __name__ == '__main__':
    main()
