from pytubefix import YouTube
from pytubefix.cli import on_progress
import ffmpeg
import sys
import os

def download_video_audio(videoURL):
    yt = YouTube(videoURL, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)
    filename = yt.title.replace("/", "_")
    print("Downloading YouTube File: " + yt.title)

    # download video and audio
    yt.streams \
        .filter(progressive=False, file_extension='mp4') \
        .order_by('resolution') \
        .desc() \
        .first() \
        .download(filename="video.mp4")
    print("Downloaded Video Stream")

    yt.streams \
        .filter(only_audio=True, file_extension='mp4', abr="128kbps") \
        .desc() \
        .first() \
        .download(filename="audio.mp4")
    print("Downloaded Audio Stream")

    # combine the video clip with the audio clip
    input_video = ffmpeg.input('video.mp4')
    input_audio = ffmpeg.input('audio.mp4')
    ffmpeg.output(input_video.video, input_audio.audio, filename + ".mp4", codec='copy').overwrite_output().run(quiet=True)
    print("Combined and Saved as: " + filename + ".mp4")

def process_files(file_list):
    for file_name in file_list:
        with open(file_name, 'r') as file:
            print("Getting URLs from: " + file_name)
			urls = file.readlines()
            for url in urls:
                url = url.strip()
                if "youtube.com" in url:
                    print("Downloading URL: " + url)
					download_video_audio(url)

if __name__ == "__main__":
    if len(sys.argv) == 2 and "youtube.com" in sys.argv[1]:
        download_video_audio(sys.argv[1])
    else:
        if len(sys.argv) > 1:
            file_list = sys.argv[1:]
            process_files(file_list)
        else:
            file_list = input("Enter the list of text files (separated by space): ").split()
            process_files(file_list)
