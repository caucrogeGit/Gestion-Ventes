"""
app.py - Point d'entrée de l'application
=========================================
Serveur HTTP pur Python (sans framework) basé sur http.server.

Responsabilités :
    - Démarrer le serveur HTTP
    - Recevoir chaque requête entrante
    - Déléguer le traitement au bon controller via la table ROUTES
    - Servir les fichiers statiques (CSS, JS)

Ce fichier ne contient aucune logique métier.
Les routes sont déclarées dans routes.py.
La configuration (hôte, port) est dans config.py.

Démarrage : python3 app.py
"""
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse
from config import APP_HOST, APP_PORT
from routes import ROUTES

# Chemin absolu vers le dossier static/, calculé une seule fois au démarrage.
STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")

# Types MIME associés aux extensions de fichiers statiques.
CONTENT_TYPES = {"css": "text/css", "js": "application/javascript"}


class RequestHandler(BaseHTTPRequestHandler):
    """
    Gestionnaire de requêtes HTTP.

    Chaque requête entrante crée une instance de cette classe.
    Les méthodes do_GET et do_POST sont appelées automatiquement
    par HTTPServer selon le verbe HTTP de la requête reçue.
    """

    def do_GET(self):
        """
        Traite les requêtes HTTP GET.

        Si le chemin commence par /static, sert le fichier correspondant.
        Sinon, recherche un handler (fonction chargée de traiter une requête) dans ROUTES et l'appelle.
        Retourne 404 si aucune route ne correspond.
        """
        parsed = urlparse(self.path)
        path   = parsed.path

        if path.startswith("/static"):
            self._serve_static(path)
            return

        handler = ROUTES.get(("GET", path))
        if handler:
            handler(self)
        else:
            self._send_response(404, "<h1>404 - Page non disponible</h1>")

    def do_POST(self):
        """
        Traite les requêtes HTTP POST.

        Recherche un handler dans ROUTES et l'appelle.
        Retourne 404 si aucune route ne correspond.
        """
        parsed  = urlparse(self.path)
        path    = parsed.path
        handler = ROUTES.get(("POST", path))

        if handler:
            handler(self)
        else:
            self._send_response(404, "<h1>404 - Page non disponible</h1>")

    def _serve_static(self, path):
        """
        Sert un fichier statique (CSS, JavaScript).

        Lit le fichier depuis le dossier static/ et l'envoie au navigateur
        avec le Content-Type approprié.

        Sécurité — Protection contre le Path Traversal :
            Un attaquant pourrait tenter de remonter les dossiers avec "../"
            pour accéder à des fichiers sensibles hors de static/ :
                GET /static/../../.env  →  accès aux mots de passe !
            os.path.realpath() résout le chemin absolu réel, puis on vérifie
            que le fichier demandé est bien situé dans static/.
            Si ce n'est pas le cas → 403 Interdit.

        Args:
            path (str) : chemin brut de la requête, ex: /static/style.css

        Réponses possibles :
            200 : fichier trouvé et envoyé
            403 : tentative d'accès hors de static/
            404 : fichier introuvable dans static/
        """
        filepath = os.path.realpath(os.path.join(STATIC_DIR, path.removeprefix("/static/")))

        if not filepath.startswith(STATIC_DIR):
            self._send_response(403, "<h1>403 - Interdit</h1>")
            return

        try:
            with open(filepath, "rb") as file:
                content = file.read()

            ext          = path.split(".")[-1]
            content_type = CONTENT_TYPES.get(ext, "text/plain")

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()
            self.wfile.write(content)

        except FileNotFoundError:
            self._send_response(404, "<h1>404 - Fichier non trouvé</h1>")

    def _send_response(self, code, html):
        """
        Envoie une réponse HTTP avec un contenu HTML.

        Args:
            code (int) : code de statut HTTP (ex: 200, 403, 404)
            html (str) : contenu HTML à envoyer au navigateur
        """
        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        """
        Surcharge du logger par défaut de BaseHTTPRequestHandler.
        Affiche chaque requête reçue dans le terminal avec l'adresse IP du client.
        """
        print(f"[{self.address_string()}] {format % args}")


# Point d'entrée principal.
# Démarre le serveur HTTP sur l'hôte et le port définis dans config.py.
# Le serveur tourne jusqu'à un arrêt manuel (Ctrl+C).
if __name__ == "__main__":
    server = HTTPServer((APP_HOST, APP_PORT), RequestHandler)
    print(f"Serveur démarré sur http://{APP_HOST}:{APP_PORT}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServeur arrêté.")
        server.server_close()
