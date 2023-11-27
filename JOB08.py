def my_sort(liste):
    n = len(liste)
    total_coups = 0

    # Utilisation d'une variable pour suivre si des echanges ont été effectués dans une itération
    coups_effectuer = True

    # Boucle pour trier la liste
    while coups_effectuer:
        coups_effectuer = False  # Initialisation à False avant chaque itération

        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]  # Échange des éléments
                total_coups += 1
                coups_effectuer = True  # Un echanges a été effectué

    print(f"Nombre total de coups nécessaires : {total_coups}")
    return liste

# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
print("Liste initiale :", ma_liste)
resultat = my_sort(ma_liste[:])  # Appel de la fonction en passant une copie de la liste
print("Liste triée :", resultat)