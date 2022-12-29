from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil

# Functions

def select_location():
    path = filedialog.askdirectory()
    location_label.config(text=path)

def download_file():
    get_link = link_field.get()
    user_location = location_label.cget('text')
    screen.title('Download Downloading')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    video_clip = VideoFileClip(mp4_video)
    video_clip.close()
    shutil.move(mp4_video, user_location)
    screen.title('Download Complete')

def close():
    screen.destroy()

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# Logo Image
logo_img = PhotoImage(file='.pics/yt.png')
# Resize Logo
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 80, image=logo_img)

# Link Field
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Enter Youtube URL ', font=('Arial', 15))

# Download Location
location_label = Label(screen, text='Download Location ', font=('Arial', 15))
location_button = Button(screen, text='Pick Location', command=select_location)

# Download Button
download_button = Button(screen, text='Download Video', command=download_file)

# Exit Button
exit_button = Button(screen, text='Exit', command=close)

# Add Widgets To Window
canvas.create_window(250, 170, window=location_label)
canvas.create_window(250, 220, window=location_button)
canvas.create_window(250, 280, window=link_label)
canvas.create_window(250, 330, window=link_field)
canvas.create_window(250, 400, window=download_button)
canvas.create_window(250, 450, window=exit_button)


screen.mainloop()
