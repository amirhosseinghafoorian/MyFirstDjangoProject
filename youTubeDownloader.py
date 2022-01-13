from pytube import YouTube


def youTubeDownloader():
    # this function requires vpn
    link = input('Enter your url : ')
    youTube = YouTube(link)

    # Title of video
    print('Title :', youTube.title)
    print('-------------------')
    items = youTube.streams

    for stream in items:
        print(stream, '\n')

    isHighest = input('do you wanna download the highest? (yes/no) : ')
    if isHighest.startswith('y'):
        ys = items.get_highest_resolution()
        ys.download()
    else:
        tag = input('Enter video tag : ')
        ys = items.get_by_itag(tag)
        ys.download()

#     ava max motto
#     https://youtu.be/1_4ELAxKrDc
