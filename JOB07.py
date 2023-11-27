def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40:
            multiple_de_5_superieur = ((note + 2) // 5) * 5  # Calcul du prochain multiple de 5 supérieur à la note
            if multiple_de_5_superieur - note < 3:  # Vérification du critère pour arrondir
                notes_arrondies.append(multiple_de_5_superieur)  # Ajout de la note arrondie
            else:
                notes_arrondies.append(note)  # Ajout de la note non arrondie
        else:
            notes_arrondies.append(note)  # Ajout de la note non arrondie (échec)
    return notes_arrondies

# Exemple d'utilisation :
liste_notes = [83, 62, 45, 37, 90, 29]
notes_arrondies = arrondir_notes(liste_notes)
print("Notes initiales :", liste_notes)
print("Notes arrondies :", notes_arrondies)