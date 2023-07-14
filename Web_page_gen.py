import tkinter as tk
from tkinter import *


win_size_num_X = 900 #enter win size X
win_size_num_Y = 400 #enter ein size Y 

win_multi ="x" #for sintax issue 
win_size = "{}".format(win_size_num_X) + win_multi + "{}".format(win_size_num_Y) #combines x and y values and turns them into a string as well as an x for sintax issue ("X,x,Y")("900x400")

Buttion1_location_X = win_size_num_X - 340  #math for buttion 1 to stay on edge_X
Buttion1_location_Y = win_size_num_Y - 80 #math for buttion 1 to stay on bottom edge_Y 

Buttion2_location_X = win_size_num_X - 170 #math for buttion 2 to stay on edge_X
Buttion1_location_Y = win_size_num_Y - 80 #math for buttion 2 to stay on bottom edge_Y
        
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")
        
        

        self.button = Button(self.master, text="Default HTML Page",width=20,height=3).place(bordermode= OUTSIDE,x=Buttion1_location_X,y=Buttion1_location_Y) #button for default page
        self.entry1 = Entry(self.master, width= 50).place(relx= .5, rely= .5, anchor= CENTER) #text box
        self.button2 = Button(self.master, text="Submit custom text",width=20,height=3).place(bordermode= OUTSIDE, x=Buttion2_location_X,y=Buttion1_location_Y) #button for custom page

  
                   
if __name__ == "__main__": 
    root = Tk()
    root.geometry(win_size) #set window size!!
    App = ParentWindow(root) 
    root.mainloop()
    
def defaultHTML(self): #for default html buttion
    htmlText = "Stay Tuned for our amazing summer sale!"
    htmlFile = open("index.html","w")
    htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"