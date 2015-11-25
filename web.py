
#Importing Essential Modules
from Tkinter import *
import webbrowser
import engine_select

#Select search engine
def engine():
    v=(var.get())
    engine_name=engine_select.server_select(v)

#Selecting the image of engine
    if engine_name=="Google":
     image1=PhotoImage(file="res/google.gif")
     cwgt.img=image1
     cwgt.create_image(115,110,anchor=NW,image=image1)
    if engine_name=="Bing":
     image1=PhotoImage(file="res/bing.gif")
     cwgt.img=image1
     cwgt.create_image(40,110,anchor=NW,image=image1)
    if engine_name=="Yahoo":
     image1=PhotoImage(file="res/yahoo.gif")
     cwgt.img=image1
     cwgt.create_image(25,110,anchor=NW,image=image1)
    sel(engine_name)
    
def sel(engine_name):
    selection = text="Enter your query here to search in "+engine_name
    label.config(text = selection)

#Search function
def search():
    v=(var.get())
    base_url=engine_select.url_select(v)
    url = base_url + str(c2.get())
    webbrowser.open(url)
    
#Bringing up new Window
root = Tk()   
root.title("Web Search")
label = Label(root)
label.pack()
label.config(text="Select any one of the search engines")
cwgt=Canvas(root)
cwgt.configure(background='white')
cwgt.pack(expand=True, fill=BOTH)

#Making Radio Buttons
var = IntVar()
R1 = Radiobutton(root, text="Google", variable=var, indicatoron = 0,
                width = 10,
                padx = 20,value=1,
                  command=engine)
cwgt.create_window(10,20,window=R1, anchor=NW)

R2 = Radiobutton(root, text="Bing", variable=var, indicatoron = 0,
                width = 10,
                padx = 20,value=2,
                  command=engine)
cwgt.create_window(130,20,window=R2, anchor=NW)

R3 = Radiobutton(root, text="Yahoo",variable=var, indicatoron = 0,
                width = 10,
                padx = 20,value=3,
                  command=engine)
cwgt.create_window(250,20,window=R3, anchor=NW)

engine_name="Google"

#Inserting query box
c2 = Entry(root)
cwgt.create_window(127,60,window=c2, anchor=NW)
v=1


#Insrting Search Button	    
a1 = Button(root, text='Search', command=search)
cwgt.create_window(140,85,window=a1, anchor=NW)

#Inserting Quit Button
a2 = Button(root, text='Quit', command=quit)
cwgt.create_window(210,85,window=a2, anchor=NW)	 

#Credits
cred=Button(cwgt,text="Developed by Abhinav T K, Earnest, Amrutha ",bd=0)
cwgt.create_window(75,240,window=cred,anchor=NW)
cred.configure(background='white')

root.mainloop()
