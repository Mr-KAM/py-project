import os
import datetime


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
