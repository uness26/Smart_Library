from flask import Flask
from flask_cors import CORS
from db.database import get_connection
from routes.book_routes import book_bp
from routes.chat_routes import chat_bp

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message":"Library API is running"}
app.register_blueprint(chat_bp)
app.register_blueprint(book_bp, url_prefix="/api")

@app.route("/test-db")
def test_db():
    conn = get_connection()
    conn.close()
    return {"status": "DB connected successfully"}


if __name__  == "__main__":
    app.run(debug=True)