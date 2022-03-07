from ttkthemes import *
from tkinter import *
from hotel_managment.view.menu_frame import MenuFrame


class Root(ThemedTk):
    def __init__(self):
        super(Root, self).__init__()
        # setting main window and class's attribute
        self.geometry("500x500")
        self.minsize(500, 500)
        self.maxsize(500, 500)
        self.title("Hotel Management")
        self.set_theme("arc")
        self.MenuFrame = MenuFrame
        # create container that contain all things
        self.container = Frame(self)
        self.container.pack(fill="both", expand=True)
        #
        self.show_frame(MenuFrame)

    def show_frame(self, frame_want_to_show):
        frame_showed = frame_want_to_show(self.container, self)
        frame_showed.pack(fill="both", expand=True)
        frame_showed.tkraise()
