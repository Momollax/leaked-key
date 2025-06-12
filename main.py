import sqlite3

# Chemin du fichier de base de données
DATABASE_FILE = "mon_fichier.db"

def initialiser_base():
    """Création de la base et des tables si elles n'existent pas"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()

    # Table users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        refresh_token TEXT NOT NULL
    )
    """)

    # Table firebase_keys
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS firebase_keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT NOT NULL UNIQUE
    )
    """)

    conn.commit()
    conn.close()

def ajouter_user(username, password, refresh_token):
    """Insertion d'un utilisateur"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, refresh_token) VALUES (?, ?, ?)", 
                   (username, password, refresh_token))
    conn.commit()
    conn.close()

def ajouter_firebase_key(key):
    """Insertion d'une clé Firebase"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO firebase_keys (key) VALUES (?)", (key,))
    conn.commit()
    conn.close()

def afficher_users():
    """Affiche tous les utilisateurs"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("Utilisateurs:")
    for row in rows:
        print(row)
    conn.close()

def afficher_firebase_keys():
    """Affiche toutes les clés Firebase"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM firebase_keys")
    rows = cursor.fetchall()
    print("Firebase Keys:")
    for row in rows:
        print(row)
    conn.close()

if __name__ == "__main__":
    # Initialisation
    initialiser_base()
    
    # Exemple d'insertion
    ajouter_user("mon_user", "mon_password", "mon_refresh_token")
    ajouter_firebase_key("AIzaSyBCn9x04zmlwwoWAjFIqEc-FC_NXUgbFfM")

    # Affichage des données
    afficher_users()
    afficher_firebase_keys()
