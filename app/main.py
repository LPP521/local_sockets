from Tkinter import *
import socket
from tkFileDialog import askopenfilenames
import tkFileDialog
import tkMessageBox
import pdb
import sys
sys.path.insert(0, '/media/sammy/Baracuda/ubuntu/documents/summer_17/Networking/local_sockets/modules')
from ip import get_ip_addr



def setupGUI():
    ip = StringVar(master)
    ip.set(ip_addr)
    Label(master, textvariable=ip).pack()
    # display = Label(master, text="sammy")
    #display.grid(row=20, column=10)
    #display.configure(text="%s" % str(ip_addr))
    display.pack()
    separator = Frame(height=500, width=500, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)
    Button(master, text="Upload file", command=fileupload).pack()
    

def fileupload():
    while True:
        uploadedfilenames = askopenfilenames(multiple=True)
        if uploadedfilenames == '':
            tkMessageBox.showinfo(message="File Upload has been cancelled program will stop")
            return
        uploadedfiles = master.tk.splitlist(uploadedfilenames)
        if len(uploadedfiles)!=1:
           tkMessageBox.showinfo(message="Select at least one file!")
        else:
            filenames.append(uploadedfiles)
            serveFile(filenames[0][0])
            return uploadedfiles

def serveFile(filename):
    port = 8080                    # Reserve a port for your service.
    s = socket.socket()             # Create a socket object
    host = ip_addr
    s.bind((host, port))            # Bind to the port
    s.listen(5)   
    Label(master, textvariable=filename).pack()
    while True:
        print('while true')
        display.configure(text="new file").pack()
        print("uploading file ?")
        conn, addr = s.accept()     # Establish connection with client.
        print 'Got connection from', addr
        data = conn.recv(1024)
        print('Server received', repr(data))
        f = open(filename,'rb')

        l = f.read(1024)
        while (l):
           conn.send(l)
           print('Sent ',repr(l))
           l = f.read(1024)
        f.close()

        print('Done sending')
        conn.send('Thank you for connecting')
        conn.close()
    s.close()
    return


# get ip address
ip_addr = get_ip_addr()

# Create GUI
master = Tk()
display = Label(master, text="sammy")
filenames = []
setupGUI()
