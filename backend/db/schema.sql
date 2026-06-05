CREATE TABLE IF NOT EXISTS books (
    id_livre SERIAL PRIMARY KEY,
    titre VARCHAR(255) NOT NULL,
    auteur VARCHAR(255) NOT NULL,
    categorie VARCHAR(100),
    annee_publication INTEGER,
    quantite_disponible INTEGER DEFAULT 1,
    statut VARCHAR(20),
    date_retour_prevue DATE
);