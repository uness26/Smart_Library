import os, requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

def get_books():
    response = requests.get(f"{BASE_URL}/books")
    
    if response.status_code == 200:
        return response.json()
    
    return []

def add_book(data):
    response = requests.post(f"{BASE_URL}/books", json=data)
    return response.json(), response.status_code


def update_book(book_id, data):
    response = requests.put(
        f"{BASE_URL}/books/{book_id}",
        json=data
    )
    return response.json(), response.status_code


def delete_book(book_id):
    response = requests.delete(f"{BASE_URL}/books/{book_id}")
    return response.json(), response.status_code

def send_question(question):
    response = requests.post(
        "http://127.0.0.1:5000/chat",
        json={"question": question}
    )

    return response.json()["answer"]

def send_message(message):

    response = requests.post(
        f"{BASE_URL}/chat",
        json={"question": message}
    )

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    return response.json()