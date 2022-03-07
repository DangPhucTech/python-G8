from tkinter.ttk import *
import hotel_managment.model.database as db


class Function2(Frame):
    def __init__(self, container, attr_root):
        super(Function2, self).__init__(container)
        label_status = Label(self, text="Room Information", foreground="red")
        label_status.grid(row=0, column=0, columnspan=3, padx=3, pady=3, sticky="NS")
        # buttons
        self.button_back_call(attr_root)
        self.button_room_id_call()
        self.button_room_type_call()
        self.button_room_status_call()
        # grid column configure
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        # show data
        self.show_room_list()
        pass

    def button_back_call(self, attr_root):
        button_back = Button(self, text="<-", width=5, command=lambda: command_to_back())
        button_back.grid(row=0, column=0, columnspan=1, padx=3, pady=3, sticky="W")

        #
        def command_to_back():
            self.destroy()
            attr_root.show_frame(attr_root.MenuFrame)
            pass

    def button_room_id_call(self):
        self.button_room_id = Button(self, text="Room ID")
        self.button_room_id.grid(row=1, column=0, columnspan=1, padx=3, pady=3, sticky="SNEW")
        pass

    def button_room_type_call(self):
        self.button_room_type = Button(self, text="Room Type")
        self.button_room_type.grid(row=1, column=1, columnspan=1, padx=3, pady=3, sticky="SNEW")
        pass

    def button_room_status_call(self):
        self.button_room_status = Button(self, text="Room ID")
        self.button_room_status.grid(row=1, column=2, columnspan=1, padx=3, pady=3, sticky="SNEW")
        pass

    def show_room_list(self, sort=False, sort_value=None):
        # can not declared parameter directly in constructor
        # so pycharm hint this below
        if sort_value is None:
            sort_value = [1]
        # take room data from database
        if sort:
            data = sort_value
        else:
            data = db.get_room_data()
        # this thing for auto increase row after each row of information
        row = 2
        element = 0
        #
        self.label_id_list = []
        self.label_type_list = []
        self.label_status_list = []
        #
        for room in data:
            r_id = room[0]
            r_type = room[1]
            r_status = room[2]
            #
            if r_status == "available":
                r_status_color = "green"
            else:
                r_status_color = "red"
            #
            self.label_id_list.append(Label(self, text=r_id))
            self.label_id_list[element].grid(row=row, column=0, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_type_list.append(Label(self, text=r_type))
            self.label_type_list[element].grid(row=row, column=1, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_status_list.append(Label(self, text=r_status, foreground=r_status_color))
            self.label_status_list[element].grid(row=row, column=2, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            element += 1
            row += 1
