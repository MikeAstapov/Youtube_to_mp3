"""Модуль для преобразования видео с ютуб в мп3 файл. Создан по просьбе приятеля , для скачивания аудиокниг,
которые на данный момент доступны только в озвучке на ютубе."""
from time import time

from pytube import YouTube

path_for_mp3_files = r'D:\mp3'
testtesttest

def save_mp3():
    while True:
        video = input("Введите ссылку на видео для конвертации в мп3 формат >>>  ")
        if "https://www.youtube" not in video:
            print("Введите правильную ссылку на видео youtube")
        else:
            start = time()
            yt = YouTube(video)
            print('Название: ', yt.title)
            print('Ссылка на фото ', yt.thumbnail_url)
            stream = yt.streams.get_by_itag(140)
            stream.download(output_path=path_for_mp3_files, filename=f'{yt.title}.mp3')

            end = time() - start
            print(f'[INFO] КОНВЕРТАЦИЯ ВЫПОЛНЕНА. ВАШ ФАЙЛ {yt.title}.mp3 НАХОДИТСЯ В {path_for_mp3_files} ')
            print(f'Работа скрипта заняла {end:.2f} секунд')
            break


save_mp3()
