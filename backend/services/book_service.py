from db.database import get_connection

def get_all_books():
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM books")
            rows = cur.fetchall()
            
    return [
                {
                    "id_livre": r[0],
                    "titre": r[1],
                    "auteur": r[2],
                    "categorie": r[3],
                    "annee_publication": r[4],
                    "quantite_disponible": r[5],
                    "statut": r[6]
                } for r in rows
            ]

def get_book_by_id(book_id):
    query = """ SELECT * FROM books WHERE id_livre = %s"""
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (book_id,))
            book = cur.fetchone()
            return {
                    "id_livre": book[0],
                    "titre": book[1],
                    "auteur": book[2],
                    "categorie": book[3],
                    "annee_publication": book[4],
                    "quantite_disponible": book[5],
                    "statut": book[6]
                }


def add_book(data):
    
    query = """
        INSERT INTO books (titre, auteur, categorie, annee_publication, quantite_disponible, statut)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id_livre;
        """
    params = (
        data["titre"],
        data["auteur"],
        data.get("categorie"),
        data.get("annee_publication"),
        data.get("quantite_disponible"),
        data.get("statut"),
    )
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            new_id = cur.fetchone()[0]
            conn.commit()
    
    return new_id
    
def update_book(book_id, data):
    query = """
        UPDATE books 
        SET titre = %s,
            auteur = %s,
            categorie = %s,
            annee_publication = %s,
            quantite_disponible = %s,
            statut = %s
        WHERE id_livre = %s
        """
    params = (
        data["titre"],
        data["auteur"],
        data.get("categorie"),
        data.get("annee_publication"),
        data.get("quantite_disponible"),
        data.get("statut"),
        book_id
    )
    
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            conn.commit()
            return cur.rowcount
    
def delete_book(book_id):
    query = "DELETE FROM books WHERE id_livre = %s"

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, (book_id,))
            conn.commit()

            return cur.rowcount