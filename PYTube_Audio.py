import pytube
import os
from os import system

system("title " + "YouTube Downloader - by ProgrammAlex [Audio]")
youtube_link = input("\nYouTube Downloader - by ProgrammAlex\n--- Audio ---\n\nYouTube Link: ");
youtube_video = pytube.YouTube(youtube_link);
title = youtube_video.streams[0].title;
name = pytube.extract.video_id(youtube_link)
pytube.YouTube(youtube_link).streams.filter(only_audio=True).first().download(filename=name)
location = name + '.mp4'
renametomp3 = name + '.mp3'

if os.name == 'nt':
    os.system('ren {0} {1}'. format(location, renametomp3))
else:
    os.system('mv {0} {1}'. format(location, renametomp3))

os.rename(renametomp3, title+'.mp3');
print("\nDownload completed!");
os.system("pause > nul");