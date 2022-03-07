from tkinter.ttk import *
from hotel_managment.view.function1 import Function1
from hotel_managment.view.function2 import Function2
from hotel_managment.view.function3 import Function3
from hotel_managment.view.function4 import Function4
from hotel_managment.view.function5 import Function5


class MenuFrame(Frame):

    def __init__(self, container, attr_root):
        super(MenuFrame, self).__init__(container)
        #
        lb_start = Label(self, text="Select the functionality by click buttons")
        lb_start.grid(row=0, column=0, pady=10)
        # Button for setting student inf
        bt_function1 = Button(self, text="Check In", width=20,
                              command=lambda: [attr_root.show_frame(Function1), self.destroy()])
        bt_function1.grid(row=1, column=0, pady=10)
        #
        bt_function2 = Button(self, text="Room Manage", width=20,
                              command=lambda: [attr_root.show_frame(Function2), self.destroy()])
        bt_function2.grid(row=2, column=0, pady=10)
        # #
        bt_function3 = Button(self, text="Room Order", width=20,
                              command=lambda: [attr_root.show_frame(Function3), self.destroy()])
        bt_function3.grid(row=3, column=0, pady=10)
        # #
        bt_function4 = Button(self, text="Check Out", width=20,
                              command=lambda: [attr_root.show_frame(Function4), self.destroy()])
        bt_function4.grid(row=4, column=0, pady=10)
        # #
        bt_function5 = Button(self, text="History", width=20,
                              command=lambda: [attr_root.show_frame(Function5), self.destroy()])
        bt_function5.grid(row=5, column=0, pady=10)
        #
        # bt_function6 = Button(self, text="Get Courses Information", width=30,
        #                       command=lambda: [attr_root.show_frame(Function6), self.destroy()])
        # bt_function6.grid(row=6, column=0, pady=10)
        # #
        # bt_function7 = Button(self, text="Get Courses Information", width=30,
        #                       command=lambda: [attr_root.show_frame(Function7), self.destroy()])
        # bt_function7.grid(row=7, column=0, pady=10)

        self.grid_columnconfigure(0, weight=1)
