from models.client_model import get_all_clients, get_client_by_id, add_client, update_client, delete_client


def test_model():

    clients = get_all_clients()
    print("Nombre de clients :", len(clients))

    if len(clients) > 0:
        print("Premier client :", clients[0])

    client = get_client_by_id("ALFKI")
    print("Client ALFKI :", client)

    add_client("LMDI", "La maison de l'informatique", "Lequette", "Gérant", "Rue de fleurs", "Cherisy", "Eure et Loir", "28100", "France", "0670045000", "0237504020") 
    client = get_client_by_id("LMDI")
    print("Client LMDI :", client)

    update_client("La maison de l'informatique", "Lequette", "PDG", "Rue de fleurs", "Cherisy", "Eure et Loir", "28100", "France", "0670045000", "0237504020", "LMDI")
    client = get_client_by_id("LMDI")
    print("Client LMDI :", client)

    delete_client("LMDI")

if __name__ == "__main__":
    test_model()