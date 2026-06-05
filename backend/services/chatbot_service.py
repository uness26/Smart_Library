import os
import google.generativeai as genai
from dotenv import load_dotenv
from services.book_service import get_all_books

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_library_question(question):

    books = get_all_books()

    prompt = f"""
You are an intelligent library assistant.

Your role:
- Answer only using the library catalog.
- Be friendly and professional.
- Format answers clearly using emojis and sections.
- Never invent books that are not in the catalog.
- If a book is unavailable, clearly indicate it.
- If no result exists, explain politely that nothing was found.

Response formatting rules:

For a single book:

📚 Book Found

📖 Title: ...
✍️ Author: ...
🏷️ Category: ...
📅 Year: ...
📌 Status: ...

For multiple books:

📚 Books Found

1.
📖 ...
✍️ ...

2.
📖 ...
✍️ ...

For recommendations:
Explain briefly why each book may interest the user.

Library Catalog:
{books}

User Question:
{question}

You are the official assistant of a smart library management system.

You help users:
- Search books
- Check availability
- Find books by author
- Recommend books by category
- Explain library information

If the answer is based on books from the catalog, always mention their status.

If a user asks for recommendations, recommend books from the catalog only.

"""

    response = model.generate_content(prompt)

    return response.text