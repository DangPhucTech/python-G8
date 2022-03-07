from tkinter.ttk import *
import hotel_managment.model.database as db
# import PythonStore.GUI.ControllerStore as Cs
import hotel_managment.control.controller as controller

class Function4(Frame):
    def __init__(self, container, attr_root):
        super(Function4, self).__init__(container)
        # labels
        self.label_status = Label(self, text="Select check out room", foreground="red")
        self.label_status.grid(row=0, column=1, columnspan=3, padx=2, pady=2, sticky="NS")

        # buttons
        self.button_back_call(attr_root)
        self.button_enter_call()
        # entries
        self.entry_check_out_day()

        # combo boxes
        self.cbb_check_out_room()
        # column configure
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        pass

    def button_back_call(self, attr_root):
        button_back = Button(self, text="<-", width=5, command=lambda: command_to_back())
        button_back.grid(row=0, column=0, padx=2, pady=2, sticky="W")

        #
        def command_to_back():
            self.destroy()
            attr_root.show_frame(attr_root.MenuFrame)
            pass

    def button_enter_call(self):
        self.button_enter = Button(self, text="Enter", command=lambda: command_button_enter())
        self.button_enter.grid(row=44, column=1, columnspan=3, padx=5, pady=5, sticky="NS")

        #
        def command_button_enter():
            if controller.input_dob(self.entry_check_out.get(), self.label_check_out_annotation):
                r_id = str(self.cbb_room.get())
                print(r_id + " line 44 F4")
                c_i_id = db.get_check_in_id_by_room_id(r_id)
                date = self.entry_check_out.get()
                price = db.get_price_for_checkout(r_id, c_i_id, date, self.label_check_out_annotation)
                db.set_check_out_table(c_i_id, date, price)
                db.change_room_status(r_id, status=1)
                #
                self.label_check_out_annotation.config(text="Action is done !", foreground="red")
                pass

        pass

    def cbb_check_out_room(self):
        cbb_value = db.get_room_unavailable()
        self.cbb_room = Combobox(self, value=cbb_value, state="readonly")
        self.cbb_room.grid(row=1, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")

        # labels for this cbb
        self.label_room = Label(self, text="Room Available :", foreground="red")
        self.label_room.grid(row=1, column=0, padx=2, pady=2, sticky="W")

        self.label_room_annotation = Label(self, text="")
        self.label_room_annotation.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky="NS")
        pass

    def show_bill(self, destroy=0):
        """

        :param destroy:
                destroy = 0 => there is no labels to destroy at beginning
                destroy = 1 => destroy labels and update value for showing again
        :return:
        """
        if destroy == 1:
            self.destroy_show_bill()

        # this thing for auto increase row after each row of information
        row = 3
        element = 0
        #
        self.label_supply_name_list = []
        self.label_supply_quantity_list = []
        self.label_total_price_list = []
        #
        data = []
        for supply in data:
            r_id = supply[0]
            r_type = supply[1]
            r_status = supply[2]
            #
            self.label_supply_name_list.append(Label(self, text=r_id))
            self.label_supply_name_list[element].grid(row=row, column=0, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_supply_quantity_list.append(Label(self, text=r_type))
            self.label_supply_quantity_list[element].grid(row=row, column=1, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            self.label_total_price_list.append(Label(self, text=r_status))
            self.label_total_price_list[element].grid(row=row, column=2, columnspan=1, padx=2, pady=2, sticky="NS")
            #
            element += 1
            row += 1

        pass

    def destroy_show_bill(self):
        for i in self.label_supply_name_list:
            i.destroy()
        #
        for i in self.label_supply_quantity_list:
            i.destroy()
        #
        for i in self.label_total_price_list:
            i.destroy()
        pass

    def entry_check_out_day(self):
        self.entry_check_out = Entry(self)
        self.entry_check_out.grid(row=3, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")
        self.entry_check_out.insert(-1, "(Day/Month/Year)")

        # entry
        self.label_check_out = Label(self, text="Check Out Date :", foreground="red")
        self.label_check_out.grid(row=3, column=0, columnspan=1, padx=3, pady=3, sticky="SNEW")

        self.label_check_out_annotation = Label(self, text="")
        self.label_check_out_annotation.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky="NS")
        pass
