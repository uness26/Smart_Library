from services.chatbot_service import ask_library_question

question = input("Question: ")

answer = ask_library_question(question)

print("\nAnswer:")
print(answer)