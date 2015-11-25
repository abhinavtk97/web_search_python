import Tkinter
from Tkinter import *
import webbrowser
	 
engine_dict = {'google': "https://www.google.com/?gfe_rd=cr&ei=qOnZVf3qM8mL8AX_9rvwBg&gws_rd=cr&fg=1#q=",
	               'bing': "https://www.bing.com/search?q=",
	               'yahoo': "https://search.yahoo.com/search?n=10&ei=UTF-8&va_vt=any&vo_vt=any&ve_vt=any&vp_vt=any&vst=0&vf=all&vm=i&fl=0&p="}
	 
def pick_engine():
    question = "Pick your favorite search engine between Google, Bing, and Yahoo."
    print (question)
    while True:
	        search_engine = raw_input('> ').lower()
	        if search_engine in engine_dict:
	            engine_name = search_engine.capitalize()
	            base_url = engine_dict[search_engine]
	        else:
	            print('Wrong answer! Try again.\n')
	            print(question)
	            continue
	        return engine_name, base_url
	 
engine_name, base_url = pick_engine()
	 
root = Tk()

root.title('Search in ' + engine_name)
	 
String_Entry = Entry(root)
String_Entry.grid(row=0, column=0)
	 
def search():
	    url = base_url + str(String_Entry.get())
	    webbrowser.open(url)
	   
Search_Button = Button(root, text='Search', command=search)
Search_Button.grid(row=0, column=1)
	 
Quit_Button = Button(root, text='Quit', command=quit)
Quit_Button.grid(row=0, column=2)
	 
mainloop()
