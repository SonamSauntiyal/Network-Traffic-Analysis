import tkinter as tk
from tkinter import *
window=tk.Tk()
window.title('TCP SYN ATTACK')
window.geometry('400x200')
Label(window,text='Target IP Address')
targetIP=tk.Text(window,height=2,width=20)
targetIP.pack()
Label(window,text='Target Port Number')
portNum=tk.Text(window,height=2,width=20)
portNum.pack()
Label(window,text='Number of Pcaktes to be Flooded')
numOfPacket=tk.Text(window,height=2,width=20)
numOfPacket.pack()
button=tk.Button(window,text='start',width=10)
button.pack()
window.mainloop()