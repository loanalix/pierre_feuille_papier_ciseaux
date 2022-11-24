#Debut

import math
import copy

#on initialise la variable easterCounter comme 1
easterCounter=1

#On créer une liste que l'on utilisera comme une table 
tablemorph = [
        [0 , 0 , 0] ,
        [0 , 0 , 0] ,
        [0 , 0 , 0]
    ]

#On definit une grille 
def grid() :
    #on introduit la liste dans la fonction 
    global tablemorph
    #On repete la variable i pour avoir 3 colones 
    for i in range(3):
            #On repete la variable i pour avoir 3 lignes
            for o in range(3):
                #Si la liste verifie 1 
                if tablemorph[i][o]==1:
                    #alors on affiche le joueur cool (joueur1 )
                    print('😎 ',end='')
                #Si la liste verifie 2
                elif tablemorph[i][o]==2:
                     #alors on affiche le joueur neurd (joueur2 )
                    print('🤓 ',end='')
                #Sinon 
                else:
                    #On affiche le neutre "-"
                    print(" - ", end='')
            #A la fin d'une liste on va a la ligne 
            print("",end='\n')

#On definit la fonction "lagagne" qui va scanner le tableau
def lagagne(list):
    #On initialise qu'il n'y a rien dans les colone et les ligne 
    col=0
    row=0
    #On initialise qu'il n'y a pas de vérification au début 
    check1=0
    check2=0
    #On initialise qu'il n'y a pas de gagnant 
    winner = "none"
    #check for horizontal win
    #On créer 3 colone 
    for col in range(3):
        #On créer 3 ligne 
        for row in range(3):
            #Si la fonction vérifie 1 
            if list[col-1][row-1]==1:
                #On ajoute une vérification au joueur 1 
                check1=check1+1
            #Si la fonction vérifie 2
            elif list[col-1][row-1]==2:
                #On ajoute une vérification au joueur 2
                check2=check2+1
            #Si cela vérifi qu'il y a 3 symbole du joeur 1 aligner a l'horizontale 
            if check1==3:
                #le gagnant est le joueur 1
                winner="joueur1"
            #Si cela vérifi qu'il y a 3 symbole du joeur 2 aligner a l'horizontale
            elif check2==3:
                #le gagnant est le joueur 2
                winner="joueur2"
        #Réinitialiser les vérifications 
        check1=0
        check2=0
    #check for vertical wins
    #On créer 3 ligne
    for row in range(3):
        #On créer 3 colone
        for col in range(3):
            #Si la fonction vérifie 2
            if list[col-1][row-1]==1:
                #On ajoute une vérification au joueur 1
                check1=check1+1
            #Si la fonction vérifie 2
            elif list[col-1][row-1]==2:
                #On ajoute une vérification au joueur 2
                check2=check2+1
            #Si cela vérifi qu'il y a 3 symbole du joeur 1 aligner a la verticale 
            if check1==3:
                #le gagnant est le joueur 1
                winner="joueur1"
            #Si cela vérifi qu'il y a 3 symbole du joeur 2 aligner a la verticale
            elif check2==3:
                #le gagnant est le joueur 2
                winner="joueur2"
        #Réinitialiser les vérifications
        check1=0
        check2=0

    #check en bias de gauche à droite
    #Si la liste vérifie la diagonale de gauche a droite 
    if list[0][0]==list[1][1]==list[2][2]:
        #Si la liste vérifie 1 
        if list[0][0]==1:
            #le gagnant est le joueur 1
            winner="joueur1"
        elif list[0][0]==2:
            #le gagnant est le joueur 2
            winner="joueur2"
    #check en bias de droite à gauche
    #Si la liste vérifie la diagonale de droite a gauche 
    if list[0][2]==list[1][1]==list[2][0]:
        if list[0][2]==1:
            #le gagnant est le joueur 1
            winner="joueur1"
        elif tablemorph[0][2]==2:
            #le gagnant est le joueur 2
            winner="joueur2"
    #Réinitialiser les vérifications
    check1 = 0
    check2 = 0

    #check pour egalité
    #Vérification de l'égalité égale a zéro
    checkTie = 0
    #On répète 3 fois i pour créer 3 ligne 
    for i in range(3):
        #On répète 3 fois o pour créer 3 colone  
        for o in range(3):
            #Si es coordoné sont différente de 0 et qu'il n'y a pas de gagnant 
            if list[i][o] != 0 and winner=="none":
                #Ajouter a checkTie 1 
                checkTie = checkTie + 1
    #Si checkTie est égale a 9             
    if checkTie==9:
        #Alors il y a égalité 
        winner="tie"
    #Retourner le gagnant     
    return winner

#definir la fonction play avec comme parametre joueur 
def play(joueur):
    #on introduit la easterCounter dans la fonction 
    global easterCounter
    #Afficher une barre de séparation 
    print("----------")
    #Si c'est le joueur 1 
    if joueur==1:
        #Afficher avec la couleur bleu 
        print('\033[36m')
    #Si c'est le joueur 2
    elif joueur==2:
        #Afficher avec la couleur verte 
        print('\033[92m')
    #Afficher le mot joueur avec l'anulation de la couleur précedante     
    print("Joueur ",joueur,'\033[0m',end="")
    #Si c'est le joueur1 
    if joueur==1:
        #Alors afficher un emoji cool puis aller a la ligne 
        print("😎",end="\n")
    #Si c'est le joueur2
    if joueur==2:
        #Alors afficher un emoji neurd puis aller a la ligne 
        print("🤓",end="\n")
    #Demader au joueur de choisir sa position
    entry=input()
    #Si le choix est "7"
    if entry=="7":
        #Si la position en haut au milieu est libre
        if(tablemorph[0][0]==0):
            #Placer l'emoji du joueur en haut au milieu
            tablemorph[0][0]=joueur
        #Sinon 
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "8"
    elif entry=="8":
        #Si la position en haut au milieu est libre 
        if(tablemorph[0][1]==0):
            #Placer l'emoji du joueur en haut au milieu 
            tablemorph[0][1]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "9"
    elif entry=="9":
        #Si la position en haut a droite est libre
        if(tablemorph[0][2]==0):
            #Placer l'emoji du joueur en haut a droite
            tablemorph[0][2]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "4"
    elif entry=="4":
        #Si la position au milieu a gauche est libre
        if(tablemorph[1][0]==0):
             #Placer l'emoji du joueur au milieu a gauche
            tablemorph[1][0]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "5"
    elif entry=="5":
        #Si la position au milieu  est libre
        if(tablemorph[1][1]==0):
            #Placer l'emoji du joueur au milieu
            tablemorph[1][1]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "6"
    elif entry=="6":
        #Si la position au milieu a droite est libre
        if(tablemorph[1][2]==0):
            #Placer l'emoji du joueurau milieu a droite
            tablemorph[1][2]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "1"
    elif entry=="1":
        #Si la position en bas a gauche  est libre
        if(tablemorph[2][0]==0):
            #Placer l'emoji du joueur en bas a gauche
            tablemorph[2][0]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "2"
    elif entry=="2":
        #Si la position en bas au milieu est libre
        if(tablemorph[2][1]==0):
            #Placer l'emoji du joueur en bas au milieu
            tablemorph[2][1]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le choix est "3"
    elif entry=="3":
        #Si la position en bas a droite est libre
        if(tablemorph[2][2]==0):
            #Placer l'emoji du joueur en bas a droite
            tablemorph[2][2]=joueur
        #Sinon
        else:
            #Afficher "Vous ne pouvez pas faire cette action"
            print("Vous ne pouvez pas faire cette action")
            #Refaire jouer le joueur
            play(joueur)
    #Si le joueur rentre "69"
    elif entry=="69":
        #Si la variable esterCounter est a 1 
        if easterCounter==1:
            #Afficher le message "Nice mais ce n'est pas ce que je voulais"
            print("Nice mais ce n'est pas ce que je voulais ")
            #Ajouter 1 a la variable esterCounter 
            easterCounter = easterCounter + 1
            #Refaire jouer le joueur 
            play(joueur)
        #Si la variable esterCounter est a 2
        elif easterCounter==2:
            #Afficher le message "Toujours pas..."
            print("Toujours pas...")
            #Ajouter 1 a la variable esterCounter
            easterCounter = easterCounter + 1
            #Refaire jouer le joueur
            play(joueur)
        #Si la variable esterCounter est a 3
        elif easterCounter==3:
            #Afficher le message "Bon ça commence à bien faire là"
            print("Bon ça commence à bien faire là")
            #Ajouter 1 a la variable esterCounter
            easterCounter = easterCounter + 1
            #Refaire jouer le joueur
            play(joueur)
        #Si la variable esterCounter est a 4
        elif easterCounter==4:
            #Afficher le message "Dernière fois sinon..."
            print("Dernière fois sinon...")
            #Ajouter 1 a la variable esterCounter
            easterCounter = easterCounter + 1
            #Refaire jouer le joueur
            play(joueur)
        #Si la variable esterCounter est a 5
        elif easterCounter==5:
            #Afficher le message "Je vous aurais prévenu."
            print("Je vous aurais prévenu.")
            #Ajouter 1 a la variable esterCounter
            easterCounter = easterCounter + 1
            #Refaire jouer le joueur
            play(joueur)
        #Si la variable esterCounter est a 6
        elif easterCounter==6:
            #Faire quiter le jeu 
            quit()
   #Sinon
    else:
        #Afficher "Erreur"
        print('\033[91m',"Erreur. Tips : Les touches vont de 1 à 9 incluses !",'\033[0m')
         #Refaire jouer le joueur 
        play(joueur)
#On définit une fonction minimax avec comme parametre "isMaximizing"
def minimax(isMaximizing):
    #Si la fonction lagagne vérifie le joueur 1 
    if lagagne(tablemorph)=="joueur1":
        #retourner 1 
        return 1
    #Si la fonction lagagne vérifie le joueur 2
    elif lagagne(tablemorph)=="joueur2":
        #retourner -1
        return -1
    #Si la fonction lagagne vérifie l'égalité 
    elif lagagne(tablemorph)=="tie":
        #retourner 0
        return 0
    #Si il y a isMaximizing 
    if isMaximizing:
        #Commencez avec un bestScore de -100
        bestScore = -100
        #Créer 3 ligne 
        for row in range(3):
            #Créer 3 colone 
            for col in range(3):
                #Si il ya un jouer 1 
                if tablemorph[row][col]==0:
                    tablemorph[row][col]=1
                    #le score est égale au minimax desactiver 
                    score = minimax(False)
                    #Un joueur joue 
                    tablemorph[row][col]=0
                    #Si le score est superieur a bestScore 
                    if score > bestScore:
                        #Le bestScore prend la valeur de score 
                        bestScore = score
        #Retourner le bestScore 
        return bestScore
    #Si le isMaximizing n'est pas activer 
    elif not isMaximizing:
        #Commencez avec un bestScore de 100
        bestScore = 100
        #Créer 3 ligne
        for row in range(3):
            #Créer 3 colone
            for col in range(3):
                if tablemorph[row][col]==0:
                    tablemorph[row][col]=2
                    #le score est égale au minimax activer 
                    score = minimax(True)
                    #Le bot joue 
                    tablemorph[row][col]=0
                    #Si le score est plus petit que le bestScore 
                    if score < bestScore:
                        #Alors le bestScore prend la valeur du score 
                        bestScore = score
        #Retourner la fonction bestScore 
        return bestScore
#On définit la fonction "botPlay"
def botPlay():
    #On affiche une ligne de séparation 
    print("----------")
    #On affiche "Bot 🤓" en rouge 
    print('\033[31m'"Bot 🤓 ",'\033[0m')
    #On initialise le "bestScore" du bot a 100
    bestScore = 100
    #On initialiser les coordoné pour le meilleur coup de base 
    bestMove = [0,0]
    #On repete 3 fois pour créer 3 ligne 
    for row in range(3):
        #On repete 3 fois pour créer 3 colone 
        for col in range(3):
            #Si il n'y a pas de joueur 2 
            if tablemorph[row][col]==0:
                #Le bot prend la position du joueur 2 
                tablemorph[row][col]=2
                #Le score est égale au minimax qui est activer 
                score = minimax(True)
                #le bot joue 
                tablemorph[row][col]=0
                #Si le score est plus petit que le bestSore 
                if score < bestScore:
                    #Le bestScore prend la valeur du score du bot 
                    bestScore = score
                    #le bestMove ce joue dans les ligne et colones 
                    bestMove = [row, col]
    #Rejouer les bestMove 
    tablemorph[bestMove[0]][bestMove[1]]=2

#On definit la fonction game avec le parametre "bot" désactiver de base 
def game(bot=False):
    #On importe la liste dans la fonction 
    global tablemorph
    #On affiche le message "pour jouer, utilisez les touches du pavé numérique "
    print('\033[91m',"Pour jouer, utilisez les touches du pavé numérique", '\033[0m')
    #On appel la fonction "grid"
    grid()
    #Tant que 
    while True:
        #On répete 
        for i in range(1,3):
            #Si le i verrifie 2 et que le Bot est activé 
            if i==2 and bot==True :
                #Alors le bot joue en 2ème position 
                botPlay()
            #Sinon 
            else:
                #Faire jouer le joueur 2 
                play(i)
            #On appel la fonction "grid"
            grid()
            #Si l'une des fonctions "lagagne" est verifier pour le joueur1
            if lagagne(tablemorph)=="joueur1":
                #Alors afficher "LE JOUEUR 😎 GAGNE !"en rose
                print('\033[95m',"LE JOUEUR 😎 GAGNE!  ",'\033[0m')
                #Afficher une barre de séparation 
                print("====================")
                #retourner  la fonction
                return
            #Si l'une des fonctions "lagagne" est verifier pour le joueur2
            elif lagagne(tablemorph)=="joueur2":
                #Alors afficher "LE JOUEUR 🤓 GAGNE !"en rose
                print('\033[95m',"LE JOUEUR 🤓 GAGNE!  ",'\033[0m')
                #Afficher une barre de séparation 
                print("====================")
                #retourner  la fonction
                return
            #Si la fonction "lagagne " vérifie la fonction "tie"
            elif lagagne(tablemorph)=="tie":
                #Alors afficher "EGALITE!QUELLE SURPRISE!"en rose 
                print('\033[95m',"EGALITE!",'\033[0m')
                #Afficher une barre de séparation 
                print("====================")
                #retourner  la fonction
                return
#On appel la fonction grid
grid()
#On appel la fonction game en activant le bot  
game(True) 

#Fin 