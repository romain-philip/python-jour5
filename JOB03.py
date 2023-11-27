def afficher_triangle(hauteur):
    for i in range(hauteur):
        espaces = hauteur - i - 1
        if i == hauteur - 1:  
            ligne = ' ' * espaces + '/' + '_' * (2 * i) + '\\'
        else:
            ligne = ' ' * espaces + '/' + ' ' * (2 * i) + '\\'
        print(ligne)
hauteur = int(input("Entrez la hauteur du triangle : "))
afficher_triangle(hauteur)