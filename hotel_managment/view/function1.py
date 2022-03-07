from tkinter.ttk import *
import hotel_managment.model.database as db
# import PythonStore.GUI.ControllerStore as Cs
import hotel_managment.control.controller as controller

class Function1(Frame):
    def __init__(self, container, attr_root):
        super(Function1, self).__init__(container)
        # labels
        self.label_status = Label(self, text="Enter All Required Below", foreground="red")
        self.label_status.grid(row=0, column=1, columnspan=2, padx=2, pady=2, sticky="NS")
        # buttons
        self.button_back_call(attr_root)
        self.button_enter_call()
        # entries calling
        self.entry_name_call()
        self.entry_id_call()
        self.entry_phone_call()
        self.entry_check_in_date_call()
        # combobox for type and rooms
        self.cbb_room_type_call()
        self.cbb_room_avail_call()
        # grid column figure
        # self.grid_columnconfigure(0, weight=1)
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

    def button_enter_call(self):
        self.button_enter = Button(self, text="Enter", command=lambda: command_button_enter())
        self.button_enter.grid(row=44, column=1, columnspan=2, padx=5, pady=5, sticky="NS")

        #
        def command_button_enter():
            # check1, check2, check3, check4, check5 = False, False, False, False, False
            check_id = False
            check_date = False
            # consider the condition
            if controller.input_identifier(self.entry_id.get(), self.label_id_annotation):
                check_id = True
            if controller.input_dob(self.entry_check_in_dat.get(), self.label_dob_annotation):
                check_date = True

            if check_id and check_date:
                # set up
                f_name = self.entry_name_first.get()
                l_name = self.entry_name_last.get()
                c_id = str(self.entry_id.get())
                phone = self.entry_phone.get()
                check_in_date = str(self.entry_check_in_dat.get())
                room_id = str(self.cbb_room_avail.get())

                # push information
                db.set_customer_table(c_id, f_name, l_name, phone)
                db.set_check_in_table(room_id, c_id, check_in_date)

                #
                self.label_room_avail_annotation.config(text="Action is Done !", foreground="red")
            pass

        pass

    def entry_name_call(self):
        # entries
        self.entry_name_first = Entry(self)
        self.entry_name_first.grid(row=1, column=1, columnspan=1, padx=3, pady=3, sticky="SNEW")
        self.entry_name_first.insert(-1, "First Name")

        self.entry_name_last = Entry(self)
        self.entry_name_last.grid(row=1, column=2, columnspan=1, padx=3, pady=3, sticky="SNEW")
        self.entry_name_last.insert(-1, "Last Name")
        # labels for this entry
        self.label_name = Label(self, text="Full Name :", foreground="red")
        self.label_name.grid(row=1, column=0, padx=2, pady=2, sticky="W")

        self.label_first_name_annotation = Label(self, text="")
        self.label_first_name_annotation.grid(row=2, column=1, columnspan=1, padx=2, pady=2, sticky="NS")

        self.label_first_name_annotation = Label(self, text="")
        self.label_first_name_annotation.grid(row=2, column=2, columnspan=1, padx=2, pady=2, sticky="NS")
        pass

    def entry_name_destroy(self):
        self.entry_name_first.destroy()
        self.entry_name_last.destroy()
        self.label_name.destroy()
        self.label_first_name_annotation.destroy()
        pass

    def entry_id_call(self):
        # entries
        self.entry_id = Entry(self)
        self.entry_id.grid(row=3, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")
        self.entry_id.insert(-1, "Card ID Number")

        # labels for this entry
        self.label_id = Label(self, text="Identifier* :", foreground="red")
        self.label_id.grid(row=3, column=0, padx=2, pady=2, sticky="W")

        self.label_id_annotation = Label(self, text="")
        self.label_id_annotation.grid(row=4, column=1, columnspan=2, padx=2, pady=2, sticky="NS")
        pass

    def entry_dob_destroy(self):
        self.entry_id.destroy()
        self.label_id.destroy()
        self.label_id_annotation.destroy()
        pass

    def entry_phone_call(self):
        # entries
        self.entry_phone = Entry(self)
        self.entry_phone.grid(row=5, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")
        self.entry_phone.insert(-1, "(999) 9999 999")

        # labels for this entry
        self.label_phone = Label(self, text="Phone Number :", foreground="red")
        self.label_phone.grid(row=5, column=0, padx=2, pady=2, sticky="W")

        self.label_phone_annotation = Label(self, text="")
        self.label_phone_annotation.grid(row=6, column=1, columnspan=2, padx=2, pady=2, sticky="NS")

    def entry_phone_destroy(self):
        # entries
        self.entry_phone.destroy()
        self.label_phone.destroy()
        self.label_phone_annotation.destroy()

    def entry_check_in_date_call(self):
        # entries
        self.entry_check_in_dat = Entry(self)
        self.entry_check_in_dat.grid(row=7, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")
        self.entry_check_in_dat.insert(-1, "(Day/Month/Year)")

        # labels for this entry
        self.label_dob = Label(self, text="Check In Date :", foreground="red")
        self.label_dob.grid(row=7, column=0, padx=2, pady=2, sticky="W")

        self.label_dob_annotation = Label(self, text="")
        self.label_dob_annotation.grid(row=8, column=1, columnspan=2, padx=2, pady=2, sticky="NS")

    def cbb_room_type_call(self):
        # event for updating the room available
        def after_choose_value(event):
            if self.cbb_room_type.get() == "standard":
                self.room_avail_value = db.get_room_available(types=1)
            elif self.cbb_room_type.get() == "business":
                self.room_avail_value = db.get_room_available(types=2)
            elif self.cbb_room_type.get() == "president":
                self.room_avail_value = db.get_room_available(types=3)
            else:
                print("File function 1 at cbb_room_type_call has an error")
            #
            self.cbb_room_avail_destroy()
            self.cbb_room_avail_call(update=True)
            print("Combobox of room available is updated by " + str(event))
            pass

        #
        room_type_value = db.get_room_type_list()
        # entries
        self.cbb_room_type = Combobox(self, value=room_type_value, state="readonly")
        self.cbb_room_type.bind("<<ComboboxSelected>>", after_choose_value)
        self.cbb_room_type.grid(row=9, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")

        # labels for this entry
        self.label_room_type = Label(self, text="Room Type :", foreground="red")
        self.label_room_type.grid(row=9, column=0, padx=2, pady=2, sticky="W")

        self.label_room_type_annotation = Label(self, text="")
        self.label_room_type_annotation.grid(row=10, column=1, columnspan=2, padx=2, pady=2, sticky="NS")

    def cbb_room_avail_call(self, update=False):
        #
        if not update:
            self.room_avail_value = []
        # entries
        self.cbb_room_avail = Combobox(self, value=self.room_avail_value, state="readonly")
        self.cbb_room_avail.bind()
        self.cbb_room_avail.grid(row=11, column=1, columnspan=2, padx=3, pady=3, sticky="SNEW")

        # labels for this entry
        self.label_room_avail = Label(self, text="Room Available :", foreground="red")
        self.label_room_avail.grid(row=11, column=0, padx=2, pady=2, sticky="W")

        self.label_room_avail_annotation = Label(self, text="")
        self.label_room_avail_annotation.grid(row=12, column=1, columnspan=2, padx=2, pady=2, sticky="NS")

    def cbb_room_avail_destroy(self):
        self.cbb_room_avail.destroy()
        self.label_room_avail.destroy()
        self.label_room_avail_annotation.destroy()
