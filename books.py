
ma_bibliothèque = []
def ajouter_livre(titre, auteur):
    livre = {"titre": titre, "auteur": auteur, "disponible": True}
    ma_bibliothèque.append(livre)
    return livre

def lister_livres():
    return ma_bibliothèque 
