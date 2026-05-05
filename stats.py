import books

def afficher_statistiques():
    tous_les_livres = books.ma_bibliothèque
    total = len(tous_les_livres)
    
    if total == 0:
        print("Aucune statistique disponible (bibliothèque vide).")
        return

    disponibles = sum(1 for l in tous_les_livres if l["disponible"])
    empruntes = total - disponibles

    print(f"\n--- STATISTIQUES ---")
    print(f"Nombre total de livres : {total}")
    print(f"Livres disponibles      : {disponibles}")
    print(f"Livres en cours d'emprunt : {empruntes}")
