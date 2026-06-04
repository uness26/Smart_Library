import customtkinter as ctk
from ui.dashboard import Dashboard

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class LibraryApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Library")
        self.geometry("1000x700")
        Dashboard(self)
        
if __name__ == "__main__":
    LibraryApp().mainloop()