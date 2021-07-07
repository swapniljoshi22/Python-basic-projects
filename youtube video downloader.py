#importing the module

pip install pytube
from pytube import YouTube 
  
#where to save 
SAVE_PATH = "E:/" #to_do 
  
#link of the video to be downloaded 
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
  
try: 
    #object creation using YouTube which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception 
  
#filters out all the files with "mp4" extension 
mp4files = yt.filter('mp4') 
  
yt.set_filename('GeeksforGeeks Video') #to set the name of the file 
  
#get the video with the extension and resolution passed in the get() function 
d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
try: 
    #downloading the video 
    d_video.download(SAVE_PATH) 
except: 
    print("Some Error!") 
print('Task Completed!')

"""
#Downloading a file takes some time as a very large amount of data is being dowloaded from the web. Depending on the speed of the connection, time taken to execute the program varies. In case you wish to download the number of files, go with the next case.

#The basic task of downloading the multiple videos is same as downloading a single video. We can use a for loop for downloading the video.

filter_none
edit
play_arrow

brightness_4
from pytube import YouTube 
  
#where to save 
SAVE_PATH = "E:/" #to_do 
  
#link of the video to be downloaded 
link=["https://www.youtube.com/watch?v=xWOoBJUqlbI", 
      "https://www.youtube.com/watch?v=xWOoBJUqlbI"
     ]#list of youtube links which need to be downloaded 
for i in link: 
    try: 
        #object creation using YouTube which was imported in the beginning 
        yt = YouTube(i) 
    except: 
        print("Connection Error") #to handle exception 
      
    #filters out all the files with "mp4" extension 
    mp4files = yt.filter('mp4') 
  
    #get the video with the extension and resolution passed in the get() function 
    d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution) 
    try: 
        #downloading the video 
        d_video.download(SAVE_PATH) 
    except: 
        print("Some Error!") 
print('Task Completed!')
"""
