import books

def emprunter_livre(titre):
    for livre in books.ma_bibliothèque:
        if livre["titre"] == titre and livre["disponible"]:
            livre["disponible"] = False
            return True
    return False

def rendre_livre(titre):
    for livre in books.ma_bibliothèque:
        if livre["titre"] == titre and not livre["disponible"]:
            livre["disponible"] = True
            return True
    return False