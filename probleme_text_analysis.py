# ecrire un programme python qui :
# demande a l'utilisateur d'entrer une phrase .
# convertit la phrase en minuscules .
# decoupe la phrase en une liste de mots .
# affiche:
# le nombre total de mots 
# le mot le plus long 
# le nombre total de voyelles dans la phrase
# construit une nouvelle phrase dans laquelle :
# les mots de longueur paire sont convertis en majuscules
# les mots de longueur impaire restent inchanges 
def analyze_text():
    phrase = input("Veillez saisir une phrase : ")

    phrase_lower = phrase.lower()
    mots = phrase_lower.split()
    nombre_mots = len(mots)
    mot_plus_long = max(mots, key=len) if mots else ""
    voyelles = 'aeiouy'
    nombre_voyelles = sum(1 for char in phrase_lower if char in voyelles)
    nouvelle_phrase = []
    for mot in mots:
        if len(mot) % 2 == 0:
            nouvelle_phrase.append(mot.upper())
        else:
            nouvelle_phrase.append(mot)

    nouvelle_phrase_str = ' '.join(nouvelle_phrase)

    print(f"Nombre total de mots : {nombre_mots}")
    print(f"Mot le plus long : {mot_plus_long}")
    print(f"Nombre total de voyelles : {nombre_voyelles}")
    print(f"Nouvelle phrase : {nouvelle_phrase_str}")