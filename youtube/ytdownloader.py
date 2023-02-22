from pytube import YouTube
from sys import argv

link = input("Enter Video link: ")
yt = YouTube(link)

print("Title: ", yt.title)

print("Length of video: ",yt.length,"seconds")

print("View: ", yt.views)


#uncomment line 13 and 16 to enable download
#GET VIDEO LOGIC
#yd = yt.streams.get_highest_resolution()

#Starting download
#print("Downloading...")

# ADD DOWNLOAD FOLDER HERE
#yd.download(r"C:\Users\Stanley Ocran\Downloads\Video\Youtube Videos")

#print("Download completed!!")