from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
from dark_title_bar import *
import subprocess

root = Tk()
root.title("Kolay Uygulama Değiştir")

def masaustune_don_fonk():
    subprocess.Popen("powershell.exe (New-Object -ComObject Shell.Application).ToggleDesktop()")

def tarayici_ac_fonk():
    subprocess.Popen("powershell.exe start 'https://www.google.com'")

def dosya_gezgini_ac_fonk():
    subprocess.Popen("powershell.exe start explorer")

w = 600
h = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

root.geometry("%dx%d+%d+%d" % (w,h,x,y))
root.iconbitmap("media/button.ico")
root.configure(bg="#000000")
root.resizable(False,False)
root.wm_attributes("-transparentcolor", "blue")

#Resimler
arkaplan = ImageTk.PhotoImage(file="media/bg.jpg")
masaustu = ImageTk.PhotoImage(file="media/masaustu.jpg")
tarayici = ImageTk.PhotoImage(file="media/tarayici.jpg")
dosya = ImageTk.PhotoImage(file="media/dosya.jpg")


#Butonlar / Labellar
arkaplan_label = Label(root, image=arkaplan).pack()

masaustune_don = Button(root, border=0, command=masaustune_don_fonk, cursor="hand2",image=masaustu).place(x=50,y=171)
tarayici_ac = Button(root, border=0, command=tarayici_ac_fonk, cursor="hand2", image=tarayici).place(x=50,y=298)
dosya_gezgini_ac = Button(root, border=0, command=dosya_gezgini_ac_fonk, cursor="hand2", image=dosya).place(x=50,y=426)





dark_title_bar(root)
root.mainloop()