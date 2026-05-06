import books 
import loans 
import stats 

while True:
    print("\n--- BIBLIOCAMPUS ---")
    print("1. Ajouter un livre")
    print("2. Lister les livres")
    print("3. Emprunter un livre")
    print("4. Voir les statistiques")
    
    choix = input("Votre choix : ")

    if choix == "1":
        t = input("Titre : ")
        a = input("Auteur : ")
        books.ajouter_livre(t, a)
        print("Livre ajouté !")
    elif choix == "2":
        for l in books.lister_livres():
            etat = "Dispo" if l["disponible"] else "Emprunté"
            print(f"- {l['titre']} ({etat})")
    elif choix == "3":
        t = input("Titre à emprunter : ")
        if loans.emprunter_livre(t):
            print("Succès !")
        else:
            print("Impossible.")
    elif choix == "4":
        stats.afficher_statistiques()
    