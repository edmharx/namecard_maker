import customtkinter
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(frame, text="State your name", font=('Arial', 20))
label.pack(padx=12, pady=10,)

name_entry = customtkinter.CTkEntry(frame, placeholder_text="Name")
name_entry.pack(padx=12, pady=10,)

label = customtkinter.CTkLabel(frame, text="What is your dream job?", font=('Arial', 20))
label.pack(padx=12, pady=10,)

jobs = ["Software Engineer", "Web Developer", "Backend Programmer", "Fullstack Developer"]
dropdown = customtkinter.CTkOptionMenu(frame, values=jobs)
dropdown.pack()


def on_click():
    messages = f"{name_entry.get()}\n{dropdown.get()}"
    CTkMessagebox (title="Namecard", message=(messages), icon="")



button = customtkinter.CTkButton(frame, text="Submit", command=on_click)
button.pack(padx=20, pady=12)

root.mainloop()