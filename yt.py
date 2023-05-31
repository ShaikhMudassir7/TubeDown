from os import path
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from pytube import YouTube

selected_path = ""
def browse_directory():
    global selected_path
    selected_path = filedialog.askdirectory()
    lbl_path_show = Label(root, text= "Path: "+ str(selected_path), background = "lightgray", foreground = "black", font = ("Arial", 10, "bold"))
    lbl_path_show.place(x = 200, y = 162)
    if len(selected_path) < 1:
        messagebox.showerror("Error", "Please insert Directory") 

def download_video():
    url = str(ent_link.get())
    resolution = var.get()

    if len(url) < 1:
        messagebox.showerror("Error", "URL cannot be Empty")
 
    yt = YouTube(url)
    try:
        if var.get() == 0:
             selected_resolution = yt.streams.get_highest_resolution()
        elif var.get() == 1:
            selected_resolution = yt.streams.get_lowest_resolution()
        elif var.get() == 2:
            selected_resolution = yt.streams.filter(only_audio=True).first()
        else:
            selected_resolution = yt.streams.get_highest_resolution()
        try:
            selected_resolution.download(selected_path)
            
            messagebox.showinfo("Success", "Video Downloaded!")
            messagebox.showinfo("Message", "For more information, please refer to the documentation.")

        except:
            messagebox.showerror("Error", "Download Failed")
    except:
        messagebox.showerror("Error","Please try again")


root = Tk()
root.geometry('500x400+350+100')
root.resizable(False, False)
root.title("Video Downloader")
root.config(bg = "lightgray")

#--------------------------Header----------------------
heading = Label(root, text = "Video Downloader", background  = "lightgray", foreground = "blue", font = ("Arial", 15))
heading.pack(anchor= "center", pady = 10)

credit1 = Label(root, text = "-By Your Name ❤", background  = "lightgray", foreground = "black", font = ("Arial", 12))
credit1.pack(anchor = "ne" , padx= 10)

#--------------------------Link----------------------
lbl_link = Label(root, text = "Link", background  = "lightgray", foreground = "blue", font = ("Arial", 10))
lbl_link.pack(anchor = "nw", padx= 50, pady= 20)

ent_url = StringVar()
ent_link = Entry(root, width = 52, textvariable= ent_url)
ent_link.place(x = 120, y = 105)

#--------------------------Browse----------------------
lbl_path = Label(root, text = "Path", background  = "lightgray", foreground = "blue", font = ("Arial", 10))
lbl_path.pack(anchor = "nw", padx= 50, pady= 20)

btn_path = Button(root, text = "Browse", command = browse_directory)
btn_path.place(x = 120, y = 160)

#--------------------------Quality---------------------
lbl_reso = Label(root, text = "Select Quality", background  = "lightgray", foreground = "blue", font = ("Arial", 10))
lbl_reso.pack(anchor= "nw", padx= 50, pady=20)

lbl_war = Label(root, text= "Note: By default the quality will be Highest", background  = "lightgray", foreground = "black", font = ("Arial", 8))
lbl_war.pack(anchor= "nw
