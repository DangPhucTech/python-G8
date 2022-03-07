from tkinter.ttk import *


class Function5(Frame):
    def __init__(self, container, attr_root):
        super(Function5, self).__init__(container)
        #
        self.button_back_call(attr_root)
        pass

    def button_back_call(self, attr_root):
        button_back = Button(self, text="<-", width=5, command=lambda: command_to_back())
        button_back.grid(row=0, column=0, padx=2, pady=2, sticky="W")

        #
        def command_to_back():
            self.destroy()
            attr_root.show_frame(attr_root.MenuFrame)
            pass
