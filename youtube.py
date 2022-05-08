#   Author : Lommpas 
#   Creation Date : 05/01/2022
#   Version : 1.0
#   Language : Python 3.10.4
#   Aim : Download Youtube Video 
#  Project : Youtube Downloader
#  module to download : Pytube 
# 
# 
#  
#
from pytube import YouTube
# Comme ci comme ca Stephane Legar

def slice_Mil (a_Number):  # permet de spérarer les milliers
    reverse_Number_Text = str(a_Number)[::-1]  # [::-1] reverses the string order
    result_Sep = " "
    nb_decimal = int(len(reverse_Number_Text)/3+1)
    for i in range(nb_decimal):
        result_Sep += reverse_Number_Text[3*i:3*i+3]+ " "
    result_Sep=result_Sep.strip()[::-1] # reverse to have the correct original string
    return (result_Sep)

def print_Streams(video):
    print ("List des streams ")
    for i in video.streams.fmt_streams:
        print (i)

url_Video = "https://www.youtube.com/watch?v=PuDfh4F0aKc"

video =  YouTube(url_Video)

youtube_video = YouTube(url_Video)

print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)
print ("Téléchargement ....")
stream = youtube_video.streams.get_lowest_resolution()
print("variable sett")
stream.download()
print ("OK")
"""
print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print("  ", stream)

print (f"The Title : {video.title} ")
print (f"The Number of views : {slice_Mil(video.views)} ")

# print_Streams (video)
print ("STREAMS")
for stream in video.streams.fmt_streams:
    print (" ",stream)
"""