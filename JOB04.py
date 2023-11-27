def afficher_tapis_diagonale(taille):
    for i in range(taille + 1):
        for j in range(taille + 1):
            if j == 0 or j == taille:
                print("|", end=" ")
            elif i == 0 or i == taille or i == j:
                print("-", end=" ")
            else:
                print("#", end=" ")

        print("")

# Exemple pour une taille de 10
taille = 10
afficher_tapis_diagonale(taille)