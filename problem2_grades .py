# On considere la liste suivante des notes d'une classe :
# students = [("Ali",12), ("Fatou",17), ("Moussa",9), ("Awa",14), ("Ibrahima",7)]
# ecrire un programme python qui :
# Affiche tous les etudiants avec leurs notes.
# Calcule et Affiche :
# La moyenne de la classe.
# la note maximale 
# la note minimale
# Affiche :
# la liste des etudiants admis (note >= 10)
# la liste des etudiants ajournes (note < 10)
# Cree une nouvelle liste contenant uniquement les noms des etudiants admis, triee par ordre alphabetique.
# contraintes:
# utiliser des tuples et des listes
# utiliser au moins deux foctions 
# utiliser des boubles et des conditions 
# NB: NE PAS UTILISER DE LIBRAIRIES EXTERNES (NUMPY, PANDAS, ETC.).
def afficher_etudiants(students):
    print("Liste des etudiants avec leurs notes :")
    for nom, note in students:
        print(f"{nom} : {note}")
        students = [("Ali",12), ("Fatou",17), ("Moussa",9), ("Awa",14), ("Ibrahima",7)]
        def calculer_moyenne():
            total = sum(note for nom, note in students)
            moyenne = total / len(students)
            return moyenne
        def analyser_notes():
            notes = [note for nom, note in students]
            note_max = max(notes)
            note_min = min(notes)
            admis = [nom for nom, note in students if note >= 10]
            ajournes = [nom for nom, note in students if note < 10]
            admis_tries = sorted(admis)
            return note_max, note_min, admis, ajournes, admis_tries
        afficher_etudiants(students)
        moyenne = calculer_moyenne()    
        print(f"\nMoyenne de la classe : {moyenne:.2f}")
        note_max, note_min, admis, ajournes, admis_tries = analyser_notes()
        print(f"Note maximale : {note_max}")
        print(f"Note minimale : {note_min}")
        print(f"\nListe des etudiants admis (note >= 10) : {admis}")
        print(f"Liste des etudiants ajournes (note < 10) : {ajournes}")
        print(f"\nListe des noms des etudiants admis, triee par ordre alphabetique : {admis_tries}") 
        