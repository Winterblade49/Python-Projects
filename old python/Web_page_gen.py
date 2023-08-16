import tkinter as tk
from tkinter import *
import webbrowser

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
        
        
        self.labeltext = Label(text="Enter Custom text or click default html button")
        self.labeltext.grid(row=0,column=0,padx=20,pady=(20,0))
        self.button = Button(self.master, text="Default HTML Page",width=20,height=3,command=self.defaultHTML)
        #.place(bordermode= OUTSIDE,x=Buttion1_location_X,y=Buttion1_location_Y) #button for default page
        self.button.grid(row = 2,column = 1,padx=(0,10),pady=(10,10))
        self.entry1 = Entry(self.master, width= 50)#.place(relx= .5, rely= .5, anchor= CENTER) #text box
        self.entry1.grid(row = 1,column = 0,padx=(30,15),pady=(10,10),columnspan=3, sticky=W+E )
        self.button2 = Button(self.master, text="Submit custom text",width=20,height=3,command=self.format_document)
        #.place(bordermode= OUTSIDE, x=Buttion2_location_X,y=Buttion1_location_Y) #button for custom page
        self.button2.grid(row = 2,column = 2,padx=(0,10),pady=(10,10))

    def format_document(self):
        htmlText = self.entry1.get()
        file = open("index.html", "w")
        body = "<html> <body> <h1>" + htmlText + "</h1> </body> </html>"
        file.write(body)
        file.close()
        webbrowser.open_new_tab("index.html")
    
                    
        
    def defaultHTML(self): #for default html buttion
        htmlText = "Stay Tuned for our amazing summer sale!"
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
        
if __name__ == "__main__": 
        root = Tk()
        root.geometry(win_size) #set window size!!
        App = ParentWindow(root) 
        root.mainloop()