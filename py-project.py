import os
import datetime
import shutil

def create_flask_app(base_dir="flask-app"):
    """Crée la structure d'un projet Flask"""
    
    # Structure des dossiers et fichiers
    structure = {
        "src": {
            "templates": {
                "base.html": """
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    {% block content %}{% endblock %}
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
</body>
</html>
""",
                "index.html": """
{% extends "base.html" %}
{% block title %}Accueil{% endblock %}
{% block content %}
    <h1>Bienvenue sur Flask App</h1>
{% endblock %}
"""
            },
            "static": {
                "css": {
                    "style.css": "/* Vos styles CSS ici */"
                },
                "js": {
                    "main.js": "// Votre JavaScript ici"
                }
            },
            "routes": {
                "main.py": """
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
"""
            },
            "app.py": """
from flask import Flask
from routes.main import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
"""
        },
        "tests": {
            "test_app.py": """
import pytest
from src.app import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
"""
        },
        "requirements.txt": """
flask==3.0.0
pytest==7.4.0
""",
        "README.md": """
# Flask App

## Installation
1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment
4. Install dependencies: `pip install -r requirements.txt`

## Running the app
```
python src/app.py
```
"""
    }

    try:
        # Création du dossier principal
        project_path = os.path.join(os.getcwd(), base_dir)
        if os.path.exists(project_path):
            shutil.rmtree(project_path)
        
        os.makedirs(project_path)

        def create_structure(current_path, structure):
            for name, content in structure.items():
                path = os.path.join(current_path, name)
                
                if isinstance(content, dict):
                    # C'est un dossier
                    os.makedirs(path, exist_ok=True)
                    create_structure(path, content)
                else:
                    # C'est un fichier
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content.strip())

        create_structure(project_path, structure)
        print(f"Projet Flask créé avec succès dans: {project_path}")
        
    except Exception as e:
        print(f"Erreur lors de la création du projet: {str(e)}")


def abreviation_mois_annee_actuelle():
    # Obtenir la date et l'heure actuelle
    date_actuelle = datetime.datetime.now()

    # Récupérer l'abréviation du mois et l'année actuelle
    abreviation_mois = date_actuelle.strftime("%b")
    annee = date_actuelle.year

    return f"{abreviation_mois}-{annee}"


def formated_template(auteur, description):
    template = f'''
    # -----------------------------------------------
    # |                  Auteur                     |
    # -----------------------------------------------
    # Auteur: {auteur}
    # Date de création: {abreviation_mois_annee_actuelle()}
    # Description: {description}

    # -----------------------------------------------
    # |           Description du Projet             |
    # -----------------------------------------------
    """Documentation

    """

    # -----------------------------------------------
    # |      Importation de Modules/ Packages       |
    # -----------------------------------------------
    import module1
    import module2

    # -----------------------------------------------
    # |          Initialisation Config              |
    # -----------------------------------------------
    # [Initialisation des paramètres, configuration
    # de l'environnement, etc.]


    # -----------------------------------------------
    # |           Définitions des Fonctions         |
    # -----------------------------------------------
    def fonction1(parametre1, parametre2):
        """Documentation de la fonction1."""
        # Corps de la fonction1
        pass


    def fonction2(parametre):
        """Documentation de la fonction2."""
        # Corps de la fonction2
        pass


    # -----------------------------------------------
    # |             Définitions des Classes         |
    # -----------------------------------------------
    class MaClasse:
        """Documentation de la classe MaClasse."""

        def __init__(self, parametre):
            """Initialisation de la classe MaClasse."""
            self.parametre = parametre

        def methode(self):
            """Documentation de la méthode."""
            # Corps de la méthode
            pass


    # -----------------------------------------------
    # |               Corps du Programme             |
    # -----------------------------------------------
    # [Corps principal du programme, logique principale,
    # appels de fonctions, etc.]

    # -----------------------------------------------
    # |                 Demo if Main                |
    # -----------------------------------------------
    if __name__ == "__main__":
        # [Code de démonstration, exemple d'utilisation
        # de fonctions/classes, tests, etc.]
        pass

    '''
    return template


def creer_dossiers_et_fichier(nom_dossier, auteur, description):
    print("Projet en cours d'execution")
    chemin = os.path.join(os.getcwd(), nom_dossier)

    # Créer le dossier spécifié s'il n'existe pas déjà
    if not os.path.exists(chemin):
        os.makedirs(chemin)
        print(f"Dossier '{nom_dossier}' créé avec succès.")
    else:
        print(f"Le dossier '{nom_dossier}' existe déjà.")

    # Liste des sous-dossiers à créer
    sous_dossiers = ["data", "assets", "modules"]

    # Créer les sous-dossiers dans le dossier spécifié
    for sous_dossier in sous_dossiers:
        chemin_sous_dossier = os.path.join(chemin, sous_dossier)
        if not os.path.exists(chemin_sous_dossier):
            os.makedirs(chemin_sous_dossier)
            print(f"Dossier '{sous_dossier}' créé avec succès dans '{nom_dossier}'.")
        else:
            print(f"Le dossier '{sous_dossier}' existe déjà dans '{nom_dossier}'.")

    # Créer le fichier "main.py" dans le dossier spécifié
    fichier_main = os.path.join(chemin, "main.py")
    if not os.path.exists(fichier_main):
        with open(fichier_main, "w") as f:
            # Écrire un contenu minimal dans le fichier main.py
            f.write(formated_template(auteur, description))
        print(f"Fichier 'main.py' créé avec succès dans '{nom_dossier}'.")
    else:
        print(f"Le fichier 'main.py' existe déjà dans '{nom_dossier}'.")


if __name__ == "__main__":
    nom_dossier = input("Project name : ")
    auteur = input("Author :")
    description = input("Description : ")
    creer_dossiers_et_fichier(nom_dossier, auteur, description)
