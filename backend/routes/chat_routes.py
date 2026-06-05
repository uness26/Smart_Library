from flask import Blueprint, request, jsonify
from services.chatbot_service import ask_library_question

chat_bp = Blueprint("chatbot", __name__)

@chat_bp.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("question")

    if not question:
        return jsonify({
            "error": "Message is required"
        }), 400

    answer = ask_library_question(question)

    return jsonify({
        "answer": answer
    }), 200