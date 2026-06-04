from flask import Blueprint, jsonify, request
from services.book_service import get_all_books, add_book, update_book, delete_book, get_book_by_id

book_bp = Blueprint("books", __name__)

@book_bp.route('/books', methods = ["GET"])
def get_books():
    try : 
        books = get_all_books()
        return jsonify(books)
    
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400

@book_bp.route('/books/<int:book_id>', methods=["GET"])
def get_book(book_id):
    try:
        book = get_book_by_id(book_id)
        
        if not book:
            return jsonify({
                "message": f"Book with ID {book_id} not found",
            }), 404
            
        return jsonify(book), 200
        
    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400

@book_bp.route('/books', methods = ["POST"])
def create_book():
    try:
        data = request.get_json()
        new_id = add_book(data)
        return jsonify({
            "message" : "Book added successfuly",
            "id_livre": new_id
        }), 201
        
    except Exception as e:
        return jsonify({"error" : str(e)}),400
    
@book_bp.route('/books/<int:book_id>', methods = ["PUT"])
def edit_book(book_id):
    try:
        data = request.get_json()
        updated_rows = update_book(book_id, data)
        
        if updated_rows == 0:
            return jsonify({
                "message" : "Book not found"
            }), 404
            
        return jsonify({
            "message" : "Book updated successfuly",
            "id_livre" : book_id
        }), 200
        
    except Exception as e:
        return jsonify({
            "error" : str(e)
        }), 400
        
@book_bp.route("/books/<int:book_id>", methods=["DELETE"])
def remove_book(book_id):
    try:
        deleted_rows = delete_book(book_id)

        if deleted_rows == 0:
            return jsonify({
                "message": "Book not found"
            }), 404

        return jsonify({
            "message": "Book deleted successfully",
            "id_livre": book_id
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400
        
@book_bp.route("/books/search", methods=["GET"])
def search_books():
    try:
        query = request.args.get("q", "").strip()

        if not query:
            return jsonify([])

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM books
                    WHERE
                        CAST(id_livre AS TEXT) ILIKE %s OR
                        titre ILIKE %s OR
                        auteur ILIKE %s
                    ORDER BY id_livre
                """, (f"%{query}%", f"%{query}%", f"%{query}%"))

                rows = cur.fetchall()

        return jsonify(rows)

    except Exception as e:
        return jsonify({"error": str(e)}), 400