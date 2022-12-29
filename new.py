from tkinter import *
from tkinter import filedialog

screen = Tk()
title = screen.title('Youtube Downloader')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# Logo Image
logo_img = PhotoImage(file='yt.png')
# Resize Logo
logo_img = logo_img.subsample(4, 4)
canvas.create_image(250, 80, image=logo_img)


# Link Field
link_field = Entry(screen, width=50)
link_label = Label(screen, text='Enter Youtube URL ')

# Add Widgets To Window
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link_field)

screen.mainloop()
