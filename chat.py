import socket
import time
import threading
from tkinter import *

 
root=Tk()
root.title("P2P|Chat ")
root.geometry("300x500")
root.config(bg="white")
t = Text(root, height = 5 ,width = 52)
l=Label(root ,text="P2P|Chat",bg = "white")
l.config(font =("courier",18))

hostname='Astronaut-G3'
ip=socket.gethostname()

 
def func():
    global ip,hostname
    lstbx.insert(0,"Your Hostname :  "+ip)
    lstbx.insert(1,"connected to :  "+hostname)
    t=threading.Thread(target=recv)
    t.start()
 
 
def recv():
    listensocket=socket.socket()
    port=2000
    maxconnection=99
    global ip
    print("\n       ||||||Connect succesfully||||||")
 
    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()
     
    while True:
        sendermessage=clientsocket.recv(1024).decode()
        if not sendermessage=="":
            #time.sleep(5)
            lstbx.insert(0," "+hostname+" : "+sendermessage)
 
 
s=0
def sendmsg():
    global s
    if s==0:
        s=socket.socket()
        global hostname
        port=3000
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())

    else:
        msg=messagebox.get()
        lstbx.insert(0,"You : "+msg)
        s.send(msg.encode())
 
 
def threadsendmsg():
    th=threading.Thread(target=sendmsg)
    th.start()
 
 


l.pack()
buttons=Button(root,text="|Start|",font=("courier",14),bg ="white",command=func,borderwidth=0,)
buttons.place(x=100,y=40)
 
message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=0.5,width=32)
messagebox.place(x=10,y=440)
 
sendmessageimg=PhotoImage(file='send.png')
sendmessageimg=sendmessageimg.zoom(10)
sendmessageimg=sendmessageimg.subsample(70)
 
sendmessagebutton=Button(root,image=sendmessageimg,command=threadsendmsg,borderwidth=0)
sendmessagebutton.place(x=250,y=440)
 
lstbx=Listbox(root,height=20,width=43)
lstbx.place(x=15,y=100)
 
user_name = Label(root,text =" Number" ,width=10)
 
root.mainloop()
