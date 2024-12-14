from tkinter import *
from gtts import gTTS
from playsound import playsound
import os

def play():
   myentry=mytext.get()
   myfun=gTTS(text=myentry)
   if os.path.exists("sound.mp3"):
       os.remove("sound.mp3")
       myfun.save('sound.mp3')
       os.system('sound.mp3')

def set():
    mytext.delete(0,END)

myf=Tk()
myf.title("Text To Speech")
mylabel=Label(myf,text="Text To Speech",font=("Arial",16),fg="gray")
mylabel.pack(pady=20,padx=10)  

mylabel2=Label(myf,text="Enter Your Text :", font=("Arial",13),fg="purple")
mylabel2.pack(anchor="nw")

mytext=Entry(myf)
mytext.pack ( ipady=5,ipadx=5, pady=15, anchor="nw", fill=X,expand=True)

mybutton=Button(myf,text="Play",bg="green",fg="white",font=("Arial",10),width=18,command=play)
mybutton.pack( side=LEFT,padx=20,pady=40,anchor="sw")

mybutton2=Button(myf,text="Exit",bg="red",fg="black",font=("Arial",10),width=18,command=exit)
mybutton2.pack( side=LEFT,padx=20,pady=40,anchor="sw")

mybutton3=Button(myf,text="Set",bg="blue",fg="white",font=("Arial",10),width=18,command=set)
mybutton3.pack( side=LEFT,padx=20,pady=40,anchor="sw")

myf.mainloop()