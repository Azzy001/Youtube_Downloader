from tkinter import *
from pytube import YouTube
from tkinter import filedialog

window = Tk()
Folder_Name = ""
select = 1


def file_location():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if len(Folder_Name) > 1:
        locationError.config(text=Folder_Name, fg="green")
        locationError.place(x=77, y=79)
    else:
        locationError.config(text="Please Choose Folder", fg="red")
        locationError.place(x=109, y=79)


def downloader():
    # function to complete download once button is clicked
    url = Link1.get()
    global select

    if len(url) > 1:
        DwnError.config(text="")
        yt = YouTube(url)
        select = yt.streams.get_highest_resolution()
        select.download(Folder_Name)

        lab3 = Label(window, text="Download Complete", font="arial 13 bold",
                     bg="#96A7BF", borderwidth=2, relief=RAISED)
        lab3.place(x=95, y=283)

    else:
        DwnError.config(text="Error Link", fg="red")

# ''''''''''''''''''''''''''''''''''''''''''''''


Link1 = StringVar()

# create entry box for link
Link_Ent = Entry(window, width=50, textvariable=Link1)
Link_Ent.place(x=25, y=110)

# create button with image for downloading file
Img2 = PhotoImage(file="icon.png")
btn1 = Button(window, font="arial 15", command=downloader,
              image=Img2, borderwidth=2, relief=RAISED, bg="#96A7BF")
btn1.place(x=110, y=140)

# ''''''''''''''''''''''''''''''''''''''''''''''

# Error Message location
locationError = Label(window, text="Select Path", fg="red",
                      bg="#373737", font=("jost", 10))
locationError.place(x=140, y=80)

# Error Message on Download
DwnError = Label(window, fg="red", bg="#373737", font=("jost", 10))
DwnError.place(x=146, y=20)

# Save video onto directory
saveEntry = Button(window, width=15, bg="red", fg="white",
                   text="Choose Path", command=file_location)
saveEntry.place(x=120, y=50)

# ''''''''''''''''''''''''''''''''''''''''''''''

# Tkinter features
window.configure(bg="#373737")
window.configure()
icon1 = PhotoImage(file="icon.png")
window.iconphoto(False, icon1)
window.geometry("350x360")
window.resizable(0, 0) # keeps window as one size
window.title("Arsalon's Youtube Downloader")
window.attributes("-topmost", True)  # keep window on top
window.mainloop()