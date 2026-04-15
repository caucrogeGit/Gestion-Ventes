from database import get_connection, close_connection
from sql.client_queries import (
    GET_ALL_CLIENTS,
    GET_CLIENT_BY_ID,
    ADD_CLIENT,
    UPDATE_CLIENT,
    DELETE_CLIENT
)

def get_all_clients():

    # Retourne la liste de tous les clients triés par ClientId
    # Chaque client est renvoyé sous forme de dictionnaire
    # Retourne None si aucun client n'est trouvé
    connection=None
    try:
        connection=get_connection()
        cursor=connection.cursor(dictionary=True)
        cursor.execute(GET_ALL_CLIENTS)
        clients=cursor.fetchall()
        return clients
    finally:
        close_connection(connection)

def get_client_by_id(client_Id):

    # Retourne un seul client à partir de son identifiant
    # Retourne None si aucun client n'est trouvé
    connection = None
    try:
        connection=get_connection()
        cursor=connection.cursor(dictionary=True)
        cursor.execute(GET_CLIENT_BY_ID, (client_Id,))
        client=cursor.fetchone()
        return client
    finally:
        close_connection(connection)


def add_client(client_id, nom_societe, contact_nom, contact_titre, adresse, ville, region, code_postal, pays, telephone, fax):
    
    # Ajoute un client dans la Table
    connection = None
    try:
        connection=get_connection()
        cursor=connection.cursor(dictionary=True)
        cursor.execute(ADD_CLIENT,(
            client_id, nom_societe, contact_nom, contact_titre, adresse, ville, region, code_postal, pays, telephone, fax
        ) )
        connection.commit()
    finally:
        close_connection(connection)

def update_client(client_id, nom_societe, contact_nom, contact_titre, adresse, ville, region, code_postal, pays, telephone, fax):
    
    # Modifie les information d'un client dans la Table
    connection = None
    try:
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute(UPDATE_CLIENT,(
            nom_societe, contact_nom, contact_titre, adresse, ville, region, code_postal, pays, telephone, fax, client_id
        ) )
        connection.commit()
    finally:
        close_connection(connection)        

def delete_client(client_id):

    # Supprime un client à partir de son identifiant
    connection=None
    try:
        connection=get_connection()
        cursor=connection.cursor()
        cursor.execute(DELETE_CLIENT, (client_id,))
        connection.commit()
    finally:
        close_connection(connection)


