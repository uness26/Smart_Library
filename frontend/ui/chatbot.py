import customtkinter as ctk
from api.client import send_message

class ChatbotWindow(ctk.CTkToplevel):

    def __init__(self):
        super().__init__()

        self.title("Library Assistant")
        self.geometry("700x500")

        self.chat_area = ctk.CTkTextbox(
            self,
            width=650,
            height=350
        )
        self.chat_area.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        self.message_entry = ctk.CTkEntry(
            self,
            placeholder_text="Ask something..."
        )
        self.message_entry.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.send_button = ctk.CTkButton(
            self,
            text="Ask",
            command=self.send
        )
        self.send_button.pack(pady=10)

    def send(self):

        message = self.message_entry.get().strip()

        if not message:
            return

        self.chat_area.insert(
            "end",
            f"You: {message}\n\n"
        )

        response = send_message(message)

        self.chat_area.insert(
            "end",
            f"Bot: {response['answer']}\n\n"
        )

        self.message_entry.delete(0, "end")