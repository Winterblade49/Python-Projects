import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        self.button = Button(self.master, text="Default HTML Page",width=30,height=2)
        self.button.grid(padx=(10,10),pady=(10,10))

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
def defaultHTML(self):
    htmlText = "Stay Tuned for our amazing summer sale!"
    htmlFile = open("index.html","w")
    htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"