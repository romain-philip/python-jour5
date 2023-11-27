def draw_rectangle(width, height):
    # Boucle pour dessiner les lignes du rectangle
    for i in range(height):
        if i == 0 or i == height - 1:
            # Première et dernière ligne avec des côtés horizontaux
            print('|' + '-' * (width - 2) + '|')
        elif i == height // 2:
            # Ligne du milieu avec deux caractères '-' encadrés par '|'
            print('|' + ' ' * (width - 2) + '|')
        else:
            # Autres lignes avec des espaces à l'intérieur du rectangle
            print('|' + ' ' * (width - 2) + '|')

# Appel de la fonction avec les paramètres (10, 3)
draw_rectangle(10, 3)