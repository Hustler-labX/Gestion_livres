
class Livre:
    def __init__(self, titre, auteur, isbn, quantite):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.quantite = quantite

class Emprunteur:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

class Librairie:
    def __init__(self):
        self.collection = []

    def ajouter_livre(self, livre):
        self.collection.append(livre)

    def supprimer_livre(self, isbn):
        livre_a_supprimer = None
        for livre in self.collection:
            if livre.isbn == isbn:
                livre_a_supprimer = livre
                break
    
        if livre_a_supprimer:
            self.collection.remove(livre_a_supprimer)
            print(f"Le livre '{livre_a_supprimer.titre}' a été supprimé de la collection.")
        else:
            print("Livre non trouvé dans la collection.")

    def demander_pret(self, emprunteur, isbn):
        livre_demande = None
        for livre in self.collection:
            if livre.isbn == isbn:
                livre_demande = livre
                break

        if livre_demande and livre_demande.quantite > 0:
            livre_demande.quantite -= 1
            print(f"'{emprunteur.nom}' a emprunté le livre '{livre_demande.titre}'.")
        elif livre_demande:
            print(f"Le livre '{livre_demande.titre}' n'est actuellement pas disponible.")
        else:
            print("Livre non trouvé dans la collection.")

    def demander_la_collection(self):
        for livre in self.collection:
            print(livre.titre,livre.quantite)
    def retourner_un_livre(self,isbn_livre_a_rendre):
        for livre in self.collection:
            if livre.isbn == isbn_livre_a_rendre:
                livre.quantite+=1
                print(f"Le livre '{livre.titre}' a été prêté avec succès.")
            else:
                print("Livre non trouvé dans la collection.")

# Exemple d'utilisation du système
if __name__ == "__main__":
    librairie = Librairie()

    livre1 = Livre("Harry Potter", "J.K. Rowling", "00700", 5)
    livre2 = Livre("Les miserables", "Victor Hugo", "00600", 3)
    librairie.ajouter_livre(livre1)
    librairie.ajouter_livre(livre2)
    librairie.demander_la_collection()
    emprunteur1 = Emprunteur("Mustapha", "mustapha.bedoui@ensta-paris.fr")

    librairie.demander_pret(emprunteur1, "00700")
    librairie.demander_la_collection()
    librairie.retourner_un_livre("00700")

    librairie.supprimer_livre("00600")
    librairie.demander_la_collection()
    librairie.retourner_un_livre("00600")

