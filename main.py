from pytube import YouTube

path_for_mp3_files = r'D:\mp3'



def save_mp3():
    while True:
        video = input("Введите ссылку на видео для конвертации в мп3 формат >>>  ")
        if "https://www.youtube" not in video:
            print("Введите правильную ссылку на видео youtube")
        else:
            yt= YouTube(video)
            print(yt.title)
            print(yt.thumbnail_url)
            stream = yt.streams.get_by_itag(140)
            stream.download(output_path=path_for_mp3_files, filename=f'{yt.title}.mp3')


            print(f'[INFO] КОНВЕРТАЦИЯ ВЫПОЛНЕНА. ВАШ ФАЙЛ {yt.title}.mp3 НАХОДИТСЯ В {path_for_mp3_files} ')
            break
save_mp3()
