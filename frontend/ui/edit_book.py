import customtkinter as ctk
from tkinter import messagebox
from api.client import update_book


class EditBook(ctk.CTkToplevel):
    def __init__(self, book, refresh_callback=None):
        super().__init__()
        
        self.book = book
        self.refresh_callback = refresh_callback

        self.title("Edit Book")
        self.geometry("400x500")
        
        ctk.CTkLabel(self, text="Edit Book", font=("Arial", 20, "bold")).pack(pady=10)

        self.titre = ctk.CTkEntry(self, placeholder_text="Title")
        self.titre.insert(0, book["titre"])
        self.titre.pack(pady=5)

        self.auteur = ctk.CTkEntry(self, placeholder_text="Author")
        self.auteur.insert(0, book["auteur"])
        self.auteur.pack(pady=5)

        self.categorie = ctk.CTkEntry(self, placeholder_text="Category")
        self.categorie.insert(0, book.get("categorie", ""))
        self.categorie.pack(pady=5)

        self.annee = ctk.CTkEntry(self, placeholder_text="Year")
        self.annee.insert(0, book.get("annee_publication", ""))
        self.annee.pack(pady=5)

        self.quantite = ctk.CTkEntry(self, placeholder_text="Quantity")
        self.quantite.insert(0, book.get("quantite_disponible", ""))
        self.quantite.pack(pady=5)

        self.statut = ctk.CTkEntry(self, placeholder_text="Status (disponible/emprunté)")
        self.statut.insert(0, book.get("statut", ""))
        self.statut.pack(pady=5)

        ctk.CTkButton(
            self,
            text="Save",
            command=self.save
        ).pack(pady=20)

    def save(self):
        data = {
            "titre": self.titre.get(),
            "auteur": self.auteur.get(),
            "categorie": self.categorie.get(),
            "annee_publication": self.annee.get(),
            "quantite_disponible": self.quantite.get(),
            "statut": self.statut.get()
        }

        result, status = update_book(self.book["id_livre"], data)

        if status == 200:
            messagebox.showinfo("Success", result["message"])
            self.refresh_callback()
            self.destroy()
        else:
            messagebox.showerror("Error", result.get("error", "Update failed"))