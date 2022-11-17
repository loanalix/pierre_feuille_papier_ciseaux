# def regles_du_jeu():
#     print("Pour jouer au morpion il faut être à deux. Une version du jeu contre l'ordinateur est dans les cartons mais pour le moment, ce sera contre un autre être pensant (à priori humain) ou contre vous-même.\nCommencer par chosir la taille de la grille sur laquelle vous voulez jouer entre 3 et 10.\nEnsuite chaque joueur va à tour de rôle donner une coordonée horizontale, puis verticale. Le but est de placer un chiffre [1] pour le joueur 1 et un chiffre [2] pour le joueur 2 à l'intérieur de la grille.\nLe gagnant est le premier à aligner tous les ses  symboles identiques horizontalement, verticalement ou en diagonale. C'est archi simple et pourtant on peut y prendre goût.\nA vous de jouer...")
# regles_du_jeu()
 
 
# #Génère une grille de jeu (matrice) de taille n x n initialisée à la matrice nulle.
# def creation_morpion(n):
#     matrice=[]
#     for i in range(n):
#         matrice.append([0]*n)
#     return matrice
 
 
# #Essaye de placer un pion pour le joueur "player" en position (i,j). Renvoie None s'il y a eu un problème, et n'importe quoi d'autre sinon.
# def tour_suivant(morpion,player, i,j):
#     taille = len(morpion)
#     resulat = None
#     if((0 <= i <taille) and (0 <= j < taille)):
#         if(morpion[i][j]==0):
#             morpion[i][j] = player
#             resulat = 'Non!'
#     return resulat
 
     
# #Teste si la grille est remplie (plus aucun 0).
# def grille_Remplie(morpion):
#     full = True
#     for i in range(len(morpion)):
#         if (0 in morpion[i]):
#             full = False
#     return full
 
     
# #On suppose qu'un joueur vient de placer un pion en (i,j). Avec cette fonction, on compte le nombre de pions de ce joueur sur la colonne où il vient de placer le pion (s'il y en a n, on a gagné).
 
# def comptage_vertical(morpion,i,j):
#     comptage = 0
#     taille = len(morpion)
#     for ligne in range(taille):
# #On fixe la colonne j, on la parcourt ligne à ligne.
#         if(morpion[ligne][j] == morpion[i][j]):
#             comptage += 1
#     return comptage
 
 
# #On suppose qu'un joueur vient de placer un pion en (i,j). Avec cette fonction, on compte le nombre de pions de ce joueur sur la ligne où il vient de placer le pion (s'il y en a n, on a gagné).
 
# def comptage_horizontal(morpion,i,j):
#     comptage=0
#     taille=len(morpion)
#     for colonne in range(taille):
# #On fixe la ligne i, on la parcourt colonne par colonne.
#         if(morpion[i][colonne] == morpion[i][j]):
#             comptage+=1
#     return comptage
 
 
# #Compte le nombre de pions du joueur "player" sur la diagonale descendante de la grille de jeu.
# def comptage_diag_descendant(morpion,player):
#     comptage=0
#     taille=len(morpion)
#     for k in range(taille):
#         if (morpion[k][k] == player):
#             comptage += 1
#     return comptage
 
 
# #Compte le nombre de pions du joueur "player" sur la diagonale ascendante de la grille de jeu."""
# def comptage_diag_ascendant(morpion,player):
#     comptage=0
#     taille=len(morpion)
#     for k in range(taille):
#         if (morpion[taille-k-1][k] == player):
         
#             comptage += 1
#     return comptage
 
 
# #Fonction qui vérifie si le placement du dernier pion en (i,j) a provoqué la victoire d'un joueur. Renvoie True si oui, False sinon.
# def vérification_position(morpion,i,j):
#     win = False
#     pions = len(morpion)
#     vertical = comptage_vertical(morpion,i,j)
#     horizontal = comptage_horizontal(morpion,i,j)
#     descendant = 0
#     ascendant = 0
#     if i == j:
#         descendant = comptage_diag_descendant(morpion,morpion[i][j])
#     elif j == len(morpion)-i-1:
#         ascendant = comptage_diag_ascendant(morpion,morpion[i][j])
 
#     if((vertical == pions) or (horizontal == pions) or (descendant == pions) or (ascendant == pions)):
#         win = True
#     return win
 
 
# #Vérifie si la partie est terminée. Renvoie 1 si un des joueurs a gagné, -1 si personne n'a gagné mais que la grille n'est pas encore remplie (il faut donc continuer à jouer) et 0 si la grille est remplie mais sans gagnant.
 
# def fin_jeu(morpion,i,j):
#     if vérification_position(morpion,i,j):
#         resulat = 1
#     elif grille_Remplie(morpion):
#         resulat = 0
#     else:
#         resulat = -1
#     return resulat
 
 
# #Affiche la grille de jeu
# def print_morpion(morpion):
#     taille=len(morpion)
#     ligne='  '
#     for i in range(taille):
#         ligne=ligne+str(i)+" "
#     print (ligne)
#     ligne=' '  
#     for i in range(taille):
#         ligne=ligne+" "
#     print (ligne)
#     for i in range(taille):
#         ligne=str(i) + "|"
#         for j in range(taille):
#             ligne= ligne+str(morpion[i][j])+' '
#         print (ligne)
#         ligne=' '  
#         for i in range(taille):
#             ligne=ligne+" "
#         print (ligne)
 
 
# #Fonction qui met en oeuvre le jeu du morpion.
# def jouer_morpion():
#     #Réponse au test du v3 : Bug si validation sans introduction ligne ou colonne.
#     try:
#         n=int(input('Avec quelle taille de morpion souhaitez-vous jouer? '))
#     except ValueError:
#         n=int(input('Choix impossible, quelle taille de morpion souhaitez-vous, choisir un chiffre à partir de 3? '))
#     while  n>=0 and n<=2:
#         n=int(input('Choix impossible, quelle taille de morpion souhaitez-vous, choisir un chiffre à partir de 3? '))
#     while  n>10:
#         n=int(input('Choix impossible, quelle taille de morpion souhaitez-vous, choisir un chiffre jusqu à 10? '))
     
     
#     joueur = 1
#     morpion = creation_morpion(n)
#     working = -1
#     while (working == -1):
#         joueur = ( joueur + 1 ) % 2
#         print_morpion(morpion)
#         print ("Joueur", joueur+1 ,"joue: ")
#         #Réponse au test du v3 : Bug si validation sans introduction ligne ou colonne.
#         try:
#             i=int(input("Veuillez introduire la coordonnée horizontale: "))
#         except ValueError:
#             i=int(input("Veuillez introduire la coordonnée horizontale: "))
#         try:
#             j=int(input("Veuillez introduire la coordonnée verticale: "))
#         except ValueError:
#             j=int(input("Veuillez introduire la coordonnée verticale: "))
#         test=tour_suivant(morpion,joueur+1,i,j)
#         while(test==None):
#             print ("Coordonnées incorrectes")
#             print_morpion(morpion)
#             i=int(input("Veuillez introduire la coordonnée horizontale: "))
#             j=int(input("Veuillez introduire la coordonnée verticale: "))
#             test=tour_suivant(morpion,joueur+1,i,j)
             
#         working=fin_jeu(morpion,i,j)
     
#     print_morpion(morpion)
#     if(working==0):
#         print ("Vous êtes à égalité !")
#     else:
#         print ("Le joueur", joueur+1, "a gagné la partie !")
     
# if __name__ == "__main__":
#     jouer_morpion()









    # Import des bibliotheques necessaires au programme
from player import *
from copy import deepcopy
from random import randint
from copy import *
from random import *

# Class Computer - Implementation de Player pour l'ordinateur
class Computer(Player):

    # TODO: Corriger le bug de la boucle infinie (ecriture dans le mauvais tableau)
    def play(self, game):
        other = ("X" if self.sign == "O" else "O")
        for x in range(game.size):
            for y in range(game.size):
                if game.table[x][y] == "*":
                    copy = deepcopy(game.table)
                    copy[x][y] = self.sign
                    if game.win(copy) == self.sign:
                        return (x, y)
                    copy[x][y] = other
                    if game.win(copy) == other:
                        return (x, y)
        return (randint(0, game.size-1), randint(0, game.size-1))
        return self.bestMove(game, game.table, game.size, self.sign)[0]


    # Selectionner la meilleure possibilitee de jeu
    def bestMove(self, game, table, size, sign):
        # On recupere le sign de l'adverse pour nos calculs
        other = ("X" if sign == "O" else "O")
        # On cree une liste vide pour y ajouter nos possibilitees avec leur score
        moves = list()

        # On parcours le tableau pour classer chaque possibilitee
        for x in range(size):
            for y in range(size):
                # Si la case est disponible
                if table[x][y] == "*":
                    # On fait une copie du tableau dans laquelle on joue
                    copy = deepcopy(table)
                    copy[x][y] = sign
                    # Et on recupere le resultat
                    win = game.win(copy)

                    # Si le tableau est plein et que personne ne gagne, on le grade 0
                    if win == "*" and game.full(copy):
                        score = 0
                    # Si il permet de gagner, on le grade 1
                    elif win == sign:
                        score = 1
                    # Sinon, on le grade avec l'oppose du score pour le joueur adverse
                    # pour son meilleur coup dans son jeu suivant
                    else:
                        score = 0 - self.bestMove(game, copy, size, other)[1]
                    result = ((x, y), score)

                    # Si le score est 1, on joue ce coup
                    if score == 1:
                        return result
                    # Sinon on l'ajout dans la liste avec les autres et on continue
                    moves.append(result)

        # Une fois tous les coups dans la liste, on les trie par score
        shuffle(moves)
        moves.sort(key=lambda move: move[1], reverse=True)
        # Et on joue le meilleur
        return moves[0]


        # Class Game - Gestion du tableau de jeu
class Game:
    # Initialisation du tableau de jeu
    def __init__(self, size, player1, player2):
        self.size = size
        self.table = [["*" for x in range(size)] for y in range(size)]
        self.player1 = player1
        self.player2 = player2
    # Deroulement de la partie
    def start(self):
        win = "*"
        while win == "*" and not self.full():
            while win == "*" and not self.full(self.table):
                self.show()
            for player in [self.player1, self.player2]:
                x = y = -1
                while not self.play(x, y, player.sign) and not self.full():
                    while not self.play(x, y, player.sign) and not self.full(self.table):
                        (x, y) = player.play(self)
                print(player.sign+" joue en "+str(x+1)+", "+str(y+1))
                if x != -1 and y != -1:
                    print(player.sign+" joue en "+str(x+1)+", "+str(y+1))
            win = self.win(self.table)
        self.show()
        if win == "*":
            print("Match nul !")
            return
        print(win+" remporte la partie !")
    # Affichage du tableau
    def show(self):
        print("")
        line = "  "
        for x in range(self.size):
            line += str(x+1)
            line += str(x+1)+" "
        print(line)
        for y in range(self.size):
            line = str(y+1)+" "
            for x in range(self.size):
                line += self.table[x][y]
                line += self.table[x][y]+" "
            print(line)
        print("")

    # Change la valeur d'une case si libre
    def play(self, x, y, player):
        if x >= 0 and x < self.size and y >= 0 and y < self.size and self.table[x][y] == "*":
            self.table[x][y] = player
            return True
        return False
    # Regarde si un joueur a gagne
    def win(self, table):
        for i in range(self.size):
            line = self.line(table, i)
            if line != "*":
                return line
            col = self.col(table, i)
            if col != "*":
                return col
        for i in range(2):
            dia = self.dia(table, i)
            if dia != "*":
                return dia
        return "*"
    # Verifie une ligne
    def line(self, table, y):
        player = table[0][y]
        changed = False
        for x in range(self.size):
            if table[x][y] != player:
                changed = True
        if changed:
            return "*"
        return player
    # Verifie une colonne
    def col(self, table, x):
        player = table[x][0]
        changed = False
        for y in range(self.size):
            if table[x][y] != player:
                changed = True
        if changed:
            return "*"
        return player
    # Verifie une diagonale
    def dia(self, table, d):
        i = (0 if d == 0 else self.size-1)
        player = table[i][0]
        changed = False
        for x in range(self.size):
            i = (x if d == 0 else self.size-1-x)
            if table[i][x] != player:
                changed = True
        if changed:
            return "*"
        return player

    def full(self):
        def full(self, table):
            for x in range(self.size):
                for y in range(self.size):
                    if self.table[x][y] == "*":
                        if table[x][y] == "*":
                            return False
        return True