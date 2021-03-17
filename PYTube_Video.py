import pytube
import os
from os import system

system("title " + "YouTube Downloader - by ProgrammAlex [Video]")
youtube_link = input("\nYouTube Downloader - by ProgrammAlex\n--- Video ---\n\nYouTube Link: ");
youtube_video = pytube.YouTube(youtube_link);
stream = youtube_video.streams.get_highest_resolution();
stream.download();

print("\nDownload completed!");
os.system("pause > nul");