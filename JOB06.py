def distance_toilettes():
    hauteur_marche = float(input("Entrez la hauteur d'une marche  : "))
    nombre_marches = int(input("Entrez le nombre de marches : "))
    hauteur_marche_en_metres = hauteur_marche / 100
    distance_par_montee_et_descente = nombre_marches * hauteur_marche_en_metres * 2
    distance_par_jour = distance_par_montee_et_descente * 2
    distance_par_semaine = distance_par_jour * 5/7
    resultat = f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_par_semaine:.2f} m par semaine."
    return resultat
resultat = distance_toilettes()
print(resultat)