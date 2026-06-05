import customtkinter as ctk
from tkinter import messagebox
from api.client import get_books, delete_book
from ui.add_book import AddBook
from ui.edit_book import EditBook
from ui.chatbot import ChatbotWindow

class Dashboard(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(fill="both", expand=True)
        
        self.title_label = ctk.CTkLabel(
            self,
            text="Library",
            font=("Arial", 28, "bold")
            )
        self.title_label.pack(pady=20)
        
        self.refresh_button = ctk.CTkButton(
            self,
            text="Refresh Books",
            command = self.load_books
        )
        self.refresh_button.pack(pady=10)
        
        self.add_button = ctk.CTkButton(
            self,
            text="Add New Book",
            command=self.open_add_form
        )
        self.add_button.pack(pady=10)
        
        self.chatbot_button = ctk.CTkButton(
            self,
            text="AI Assistant",
            command=self.open_chatbot
        )

        self.chatbot_button.pack()
        
        self.books_container = ctk.CTkScrollableFrame(
            self,
            width=900,
            height=500
        )

        self.books_container.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )
        
        self.load_books()
        
    def open_add_form(self):
        AddBook(refresh_callback=self.load_books)
        
    def load_books(self):
        for widget in self.books_container.winfo_children():
            widget.destroy()

        books = get_books()

        if not books:
            ctk.CTkLabel(
                self.books_container,
                text="No books found."
            ).pack(pady=20)
            return

        for book in books:

            card = ctk.CTkFrame(
                self.books_container,
                corner_radius=10
            )
            card.pack(
                fill="x",
                padx=10,
                pady=5
            )
            

            ctk.CTkLabel(
                card,
                text=book.get("titre", "N/A"),
                font=("Arial", 18, "bold")
            ).pack(anchor="w", padx=10, pady=(10, 5))

            ctk.CTkLabel(
                card,
                text=f"Auteur : {book.get('auteur', 'N/A')}"
            ).pack(anchor="w", padx=10)

            ctk.CTkLabel(
                card,
                text=f"Catégorie : {book.get('categorie', 'N/A')}"
            ).pack(anchor="w", padx=10)

            ctk.CTkLabel(
                card,
                text=f"Année : {book.get('annee_publication', 'N/A')}"
            ).pack(anchor="w", padx=10)

            ctk.CTkLabel(
                card,
                text=f"Quantité : {book.get('quantite_disponible', 'N/A')}"
            ).pack(anchor="w", padx=10)

            ctk.CTkLabel(
                card,
                text=f"Statut : {book.get('statut', 'N/A')}"
            ).pack(anchor="w", padx=10, pady=(0, 10))

            status = book.get("statut", "").lower()

            if status == "disponible":
                status_color = "green"
            elif status == "emprunté":
                status_color = "red"

            ctk.CTkLabel(
                card,
                text=f"● {book.get('statut', 'N/A')}",
                text_color=status_color,
                font=("Arial", 13, "bold")
            ).pack(anchor="w", padx=10, pady=(0, 10))

            actions_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )
            actions_frame.pack(fill="x", padx=10, pady=(0, 10))

            edit_btn = ctk.CTkButton(
                actions_frame,
                text="Edit",
                width=100,
                command=lambda b=book: self.edit_book(b)
            )
            edit_btn.pack(side="left", padx=5)

            delete_btn = ctk.CTkButton(
                actions_frame,
                text="Delete",
                width=100,
                command=lambda book_id=book["id_livre"]: self.delete_book(book_id)
            )
            delete_btn.pack(side="left", padx=5)
            
    def delete_book(self, book_id):
        result, status = delete_book(book_id)

        if status == 200:
            messagebox.showinfo("Success", result["message"])
            self.load_books()
        else:
            messagebox.showerror("Error", result.get("message", "Delete failed"))
    
    def edit_book(self, book):
        EditBook(book, refresh_callback=self.load_books)
        
    def open_chatbot(self):
        ChatbotWindow()