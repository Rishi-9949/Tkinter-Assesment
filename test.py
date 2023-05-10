from tkinter import *


# a subclass of Canvas for dealing with resizing of windows
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas 
        self.config(width=self.width, height=self.height)
        # rescale all the objescts tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)

def main():
    window = Tk()
    window.config(bg='pink')
    myframe = Frame(window)
    myframe.pack(fill=BOTH, expand=YES)
    # create a canvas with initial size 600x600
    mycanvas = ResizingCanvas(window,width=600, height=400, highlightthickness=0)
    mycanvas.place(x=0,y=450)



    # Shapping my line and filling it with colour
    mycanvas.create_rectangle(600, 600, 0, 450, fill="#004AAD")
    mycanvas.create_rectangle(600, 440, 0, 450, fill="#000000")
    # tag all of the drawn widgets
    mycanvas.addtag_all("all")
    window.mainloop()

if __name__ == "__main__":
    main()
