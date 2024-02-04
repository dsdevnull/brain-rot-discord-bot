# importing packages
from pytube import YouTube
import os


async def getDownloadedAudio(youtubeLink):
    # url input from user
    yt = YouTube(youtubeLink)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()

    # check for destination to save file
    print("Enter the destination (leave blank for current directory)")
    destination = "./sound/"

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")
