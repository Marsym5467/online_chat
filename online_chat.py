from customtkinter import *

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('Чат')
        set_appearance_mode('Dark')

        self.menu_frame = CTkFrame(self, width=175, height=400)
        self.menu_frame.place(x=0, y=0)
        self.menu_is_open = True
        self.open_menu_btn = CTkButton(self, width=30, text='/', command=self.toggle_menu)
        self.open_menu_btn.place(x=0, y=0)

        self.scroll_massages = CTkScrollableFrame(self, width=360, height=370)
        self.scroll_massages.place(x=30, y=0)
        self.scroll_massages.grid_columnconfigure(0,weight=1)

        self.input_msg = CTkEntry(self, placeholder_text="Введіть повідоилення", width=360, height=30)
        self.input_msg.place(x=0, y=370)

        self.send_msg_btn = CTkButton(self, text=">", width=40, height=30)
        self.send_msg_btn.place(x=360, y=370)

        self.name_input = CTkEntry(self.menu_frame, width=130, placeholder_text="Введіть імя")

    def toggle_menu(self):
        if self.menu_is_open:
            self.open_menu_btn.configure("|>")
            self.menu_frame.configure(width=0)
            self.scroll_massages.place(x=30)
            self.input_msg.place(x=150)
            self.name_input.place_forget()
        else:
            self.open_menu_btn.configure(text="<|")
            self.menu_frame.configure(width=150)
            self.scroll_massages.place(x=150)
            self.input_msg.place(x=150)
            self.name_input.place(x=10, y=30)
        self.menu_is_open = not self.menu_is_open


win = MainWindow()
win.mainloop()




