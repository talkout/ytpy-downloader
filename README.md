# ytpy-downloader

A barebones YouTube video downloader cobbled together for personal use. It's functional but far from optimized. 

This Python script automates the process of downloading YouTube videos and their corresponding audio tracks (using pytube), then combines them into a single file (using ffmpeg). It can handle both individual YouTube URLs and lists of URLs stored in text files. 

It particularly downloads the highest resolution video available along with the audio separately and combines them. This enables bypassing the limitation of 360p/720p as the maximum resolution of video streams with audio. So, this script can download a 1080p stream without audio, and a separate audio stream, and mux them to get the final output.

## Prerequisites

Make sure you have the following Python packages installed:
- `pytubefix`
- `ffmpeg`

You can install these packages using pip:
```bash
pip install pytubefix ffmpeg-python
```

The ffmpeg-python package also requires FFmpeg to be installed seperately. Install it as needed for your OS (See: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)). For Windows, make sure to add the installation directory to your PATH.

## Usage

To use this script, you can run it from the command line with either a YouTube URL or a list of text files containing URLs:

### Download a Single YouTube Video
```bash
python script.py "https://www.youtube.com/watch?v=NCTVMNg1M1I"
```

### Download Multiple Videos from Text File/s
```bash
python script.py file1.txt file2.txt
```

If no arguments are passed, the script will prompt you to enter the filename/s.

## Script Explanation

### Imports and Setup
The script imports necessary modules: `YouTube` and `on_progress` from `pytubefix`, `ffmpeg`, `sys`, and `os`.

### Downloading Video and Audio
The `download_video_audio` function takes a YouTube URL, downloads the video and audio streams separately, and combines them into a single file. It uses `pytubefix` to handle the YouTube download and `ffmpeg` to combine the video and audio.

### Processing Files
The `process_files` function reads a list of URLs from each text file and calls `download_video_audio` for each URL.

### Main Script Logic
The script checks if it was called with exactly one argument containing "youtube.com". If true, it downloads the video and audio for that URL. If multiple arguments are passed, it assumes they are filenames containing lists of URLs and processes them. If no arguments are passed, it prompts the user to enter filenames.

## Acknowledgments

- [Jim Lynn](https://www.jimlynn.com/posts/pytube/)
