from tkinter import *
from PIL import Image, ImageTk
class Window(Frame):

    #create constructor
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.exit_frame)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)
        
        #added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)
        
    def showImg(self):
        load = Image.open("picture.jpg")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=10)


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()
        

        
        # creating a button instance
        quitButton = Button(self, text="Quit",command =self.exit_frame)

        # placing the button on my window
        quitButton.place(x=0, y=0)
    def exit_frame(self):
        exit()

root=Tk()
#size of window
root.geometry("400x300")
app =Window(root)
root.mainloop()

