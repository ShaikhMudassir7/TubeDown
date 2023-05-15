from os import path
from tkinter import * 
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import *
from pytube import YouTube

path1 = ""
def browsefile():
    global path1
    path1 = filedialog.askdirectory()
    lbl_path_show = Label(root, text= "Path: "+ str(path1), background = "gray3", foreground = "white", font = ("Bookman Old Style", 10, "bold"))
    lbl_path_show.place(x = 200, y = 162)
    if len(path1) < 1:
        messagebox.showerror("Error", "Please insert Directory") 

def download():
    url = str(ent_link.get())
    res = var.get()

    if len(url) < 1:
        messagebox.showerror("Error", "URL cannot be Empty")
 
    yt = YouTube(url)
    try:
        if var.get() == 0:
             reso_select = yt.streams.get_highest_resolution()
        elif var.get() == 1:
            reso_select = yt.streams.get_lowest_resolution()
        elif var.get() == 2:
            reso_select = yt.streams.filter(only_audio=True).first()
        else:
            reso_select = yt.streams.get_highest_resolution()
        try:
            reso_select.download(path1)
            
            messagebox.showinfo("Sucess", "Video Downloaded!")
            messagebox.showinfo("Follow Me", "For more Stuffs like this Follow me")
            messagebox.showinfo("GitHub", "https://github.com/Sumant-Dusane")


        except:
            messagebox.showerror("Error", "Download Failed")
    except:
        messagebox.showerror("Error","Please try again")


root = Tk()
root.geometry('500x400+350+100')
root.resizable(False, False)
root.call('wm', 'iconphoto', root._w, PhotoImage(file='F:\Sumant\Python\YouTube Downloader\yicon.png'))
root.title("Youtube Video Downloader")
root.config(bg = "gray3")

#--------------------------Header----------------------
heading = Label(root, text = "Youtube Video Downloader", background  = "gray3", foreground = "#ff0000", font = ("Vadher", 15))
heading.pack(anchor= "center", pady = 10)

credit1 = Label(root, text = "-By Sumant Dusane ❤", background  = "gray3", foreground = "white", font = ("XXII ARABIAN-ONENIGHTSTAND", 15))
credit1.pack(anchor = "ne" , padx= 10)

#--------------------------Link----------------------
lbl_link = Label(root, text = "Link", background  = "gray3", foreground = "orange", font = ("Valorant", 10))
lbl_link.pack(anchor = "nw", padx= 50, pady= 20)

ent_url = StringVar()
ent_link = Entry(root, width = 52, textvariable= ent_url)
ent_link.place(x = 120, y = 105)

#--------------------------Browse----------------------
lbl_path = Label(root, text = "Path", background  = "gray3", foreground = "orange", font = ("Valorant", 10))
lbl_path.pack(anchor = "nw", padx= 50, pady= 20)

btn_path = Button(root, text = "Browse", command = browsefile)
btn_path.place(x = 120, y = 160)

#--------------------------Quality---------------------
lbl_reso = Label(root, text = "Select Quality", background  = "gray3", foreground = "orange", font = ("Valorant", 10))
lbl_reso.pack(anchor= "nw", padx= 50, pady=20)

lbl_war = Label(root, text= "Note: By default the quality will be Highest", background  = "gray3", foreground = "white", font = ("Consolas", 8))
lbl_war.pack(anchor= "nw", padx= 50)

var = IntVar()
s = ttk.Style()                   
s.configure('Wild.TRadiobutton', background= "gray3", foreground='orange') 

res1 = Radiobutton(root, text= "High", variable= var, value=0, style= 'Wild.TRadiobutton')
res1.place(x= 200, y= 220)

res2 = Radiobutton(root, text= "Low", variable= var, value=1, style= 'Wild.TRadiobutton')
res2.place(x= 300, y= 220)

res3 = Radiobutton(root, text= "Audio", variable= var, value=2, style= 'Wild.TRadiobutton')
res3.place(x= 400, y= 220)

#--------------------------Download!---------------------
s1 = ttk.Style()
s1.configure('Wild.TButton', background = "gray3", foreground = "red", font = ("Exotc350 Bd BT Bold", 15, "bold"))

btn_down = Button(root, text= "Download", style= 'Wild.TButton', command= download)
btn_down.pack(anchor= "center", pady= 25)


root.mainloop() 