from tkinter import *
from pytube import YouTube


root = Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title("youtube video downloader")
     
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
link = StringVar()

Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 50,textvariable = link).place(x = 25, y = 60)
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
def exit1():
    exit()
button1=Button(root,text = 'DOWNLOAD NOW', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
# button1.pack()
button2=Button(root,text = 'Exit', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = exit1).place(x=180 ,y = 200)
# button2.pack()
root.mainloop()
