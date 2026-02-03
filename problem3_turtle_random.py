# Ecrire un programme python utilisant les modules turtle et random pour :
# Dessiner N formes geometriques aleatoires a l'ecran.
# chaque forme est choisie aleatoirement parmi : carre, triangle, cercle.
# pour chaque forme : la taille est aleatoire (limite 400 px), la couleure est choisie aleatoirement et la position est aleatoire a l'ecran.
# contraintes:
# utiliser les modules random 
# creer une fonction par type de forme 
# utiliser une boucle for 
import turtle
import random
def dessiner_carre(tortue, taille, couleur):
    tortue.fillcolor(couleur)
    tortue.begin_fill()
    for _ in range(4):
        tortue.forward(taille)
        tortue.right(90)
    tortue.end_fill()
def dessiner_triangle(tortue, taille, couleur):
    tortue.fillcolor(couleur)
    tortue.begin_fill()
    for _ in range(3):
        tortue.forward(taille)
        tortue.right(120)
    tortue.end_fill()
def dessiner_cercle(tortue, taille, couleur):
    tortue.fillcolor(couleur)
    tortue.begin_fill()
    tortue.circle(taille)
    tortue.end_fill()
def dessiner_formes_aleatoires(N):
    ecran = turtle.Screen()
    ecran.setup(width=800, height=600)
    tortue = turtle.Turtle()
    tortue.speed(0)
    formes = [dessiner_carre, dessiner_triangle, dessiner_cercle]
    couleurs = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink']
    for _ in range(N):
        forme = random.choice(formes)
        taille = random.randint(20, 200)
        couleur = random.choice(couleurs)
        x = random.randint(-390, 390)
        y = random.randint(-290, 290)
        tortue.penup()
        tortue.goto(x, y)
        tortue.pendown()
        forme(tortue, taille, couleur)
    tortue.hideturtle()
    ecran.mainloop()
dessiner_formes_aleatoires(10) 