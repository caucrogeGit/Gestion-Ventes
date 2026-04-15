import mariadb
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER_LOGIN, DB_USER_PWD

def get_connection():

    # Ouvre une connexion à la base de données MariaDB
    # Retourne l'objet connexion si tout va bien       
    # Lève une exception en cas d'erreur
    try:
        connection = mariadb.connect(
            host = DB_HOST,
            port = DB_PORT,
            user = DB_USER_LOGIN,
            password = DB_USER_PWD,
            database = DB_NAME
        )
        return connection
    except mariadb.Error as error:
        print(f"Erreur de connection à la base de donnée 'Ventes' : {error}")
        raise

def close_connection(connection):

    # Ferme proprement la connexion si elle existe.
    if connection is not None:
        connection.close()

