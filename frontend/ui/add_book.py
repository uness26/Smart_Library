import customtkinter as ctk
from api.client import add_book
from tkinter import messagebox

class AddBook(ctk.CTkToplevel):

    def __init__(self, refresh_callback=None):
        super().__init__()

        self.refresh_callback = refresh_callback

        self.title("Add New Book")
        self.geometry("400x500")

        ctk.CTkLabel(self, text="Add Book", font=("Arial", 20, "bold")).pack(pady=10)

        self.title_entry = ctk.CTkEntry(self, placeholder_text="Title")
        self.title_entry.pack(pady=10)

        self.author_entry = ctk.CTkEntry(self, placeholder_text="Author")
        self.author_entry.pack(pady=10)

        self.category_entry = ctk.CTkEntry(self, placeholder_text="Category")
        self.category_entry.pack(pady=10)

        self.year_entry = ctk.CTkEntry(self, placeholder_text="Year")
        self.year_entry.pack(pady=10)

        self.quantity_entry = ctk.CTkEntry(self, placeholder_text="Quantity")
        self.quantity_entry.pack(pady=10)

        self.status_entry = ctk.CTkEntry(self, placeholder_text="Status (disponible/emprunté)")
        self.status_entry.pack(pady=10)

        ctk.CTkButton(self, text="Save Book", command=self.save_book).pack(pady=20)

        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack()

    def save_book(self):

        data = {
            "titre": self.title_entry.get(),
            "auteur": self.author_entry.get(),
            "categorie": self.category_entry.get(),
            "annee_publication": int(self.year_entry.get() or 0),
            "quantite_disponible": int(self.quantity_entry.get() or 1),
            "statut": self.status_entry.get() or "disponible"
        }

        response, status = add_book(data)

        if status == 201:
            self.result_label.configure(text="Book added successfully ✅")
            
            if self.refresh_callback:
                self.refresh_callback()

            self.after(1000, self.destroy)
        else:
            self.result_label.configure(text=f"Error: {response}")