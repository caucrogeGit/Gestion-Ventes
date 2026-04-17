from controllers.client_controller import ClientController

ROUTES = {
    ("GET",  "/"):               ClientController.list,
    ("GET",  "/clients"):        ClientController.list,
    ("GET",  "/clients/add"):    ClientController.add_form,
    ("GET",  "/clients/edit"):   ClientController.edit_form,
    ("POST", "/clients/add"):    ClientController.add,
    ("POST", "/clients/edit"):   ClientController.edit,
    ("POST", "/clients/delete"): ClientController.delete,
}
