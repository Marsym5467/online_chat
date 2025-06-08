import customtkinter as ctk

app = ctk.CTk()
app.geometry("300x200")

ctk.CTkLabel(app, text="Логін:").grid(row=0, column=0, padx=10, pady=10)
ctk.CTkEntry(app).grid(row=0, column=1, padx=10, pady=10)

ctk.CTkLabel(app, text="Пароль:").grid(row=1, column=0, padx=10, pady=10)
ctk.CTkEntry(app, show="*").grid(row=1, column=1, padx=10, pady=10)

ctk.CTkButton(app, text="Увійти").grid(row=2, column=0, columnspan=2, pady=20)

app.mainloop()
