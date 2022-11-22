#DEBUT

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
#On definit la fonction "lagagne"

def lagagne():
    #On introduit la liste 
    global tablemorph
    # on intialisse que il n'y a aucun score 
    col=0
    row=0
    #on initialsier les check pour les 2 joueur à 0
    check1=0 
    check2=0
    #Initialiser qu'il n'y a pas de "winner"
    winner = "none"
    #gagner a l'horizontal
     #On repete la variable col 3 fois   
    for col in range(3):
         #On repete la variable row 3 fois 
        for row in range(3):
            #Si la liste 
            if tablemorph[col-1][row-1]==1:
                check1=check1+1
            #Si la liste 
            elif tablemorph[col-1][row-1]==2:
                check2=check2+1
            #Si la verification1 est sur 3 cases 
            if check1==3:
                #Alors c'est le joueur 1 qui gagne 
                winner="joueur1"
            #Si la verification2 est sur 3 cases
            elif check2==3:
                #Alors c'est le joueur 2 qui gagne 
                winner="joueur2"
        #Reinitialiser la verification1 
        check1=0
        #Reinitialiser la verification2
        check2=0
    #gagner a la vertical 
    for row in range(3):
        for col in range(3):
            #Si 
            if tablemorph[col-1][row-1]==1:
                check1=check1+1
            elif tablemorph[col-1][row-1]==2:
                check2=check2+1
            #Si la verification1 est sur 3 cases
            if check1==3:
                #Alors c'est le joueur 1 qui gagne 
                winner="joueur1"
            #Si la verification2 est sur 3 cases
            elif check2==3:
                #Alors c'est le joueur 2 qui gagne 
                winner="joueur2"
        #Reinitialiser la verification1
        check1=0
        #Reinitialiser la verification2
        check2=0

    #gagner en bias de gauche à droite
    for case in range(3):
        if tablemorph[case-1][case-1]==1:
            check1=check1+1
        elif tablemorph[case-1][case-1]==2:
            check2=check2+1
         #Si la verification1 est sur 3 cases
        if check1==3:
            #Alors c'est le joueur 1 qui gagne 
            winner="joueur1"
         #Si la verification2 est sur 3 cases
        elif check2==3:
            #Alors c'est le joueur 2 qui gagne 
            winner="joueur2"
    #gagner en bias de droite à gauche
    if tablemorph[0][2]==tablemorph[1][1]==tablemorph[2][0]:
        if tablemorph[0][2]==1:
            winner="joueur1"
        elif tablemorph[0][2]==2:
            winner="joueur2"
    #Reinitialiser la verification1
    check1 = 0
    #Reinitialiser la verification2
    check2 = 0

    #ganer pour egalité
    look = 0
    for i in range(3):
        for o in range(3):
            if tablemorph[i][o] != 0:
                look = look + 1
    #Si toutes les cases sont remplis             
    if look==9:
        #"winner" est égale a l'égalité 
        winner="tie"
    #Retourner le gagnant
    return winner


#definir la fonction play avec comme parametre joueur 
def play(joueur):
    #Afficher Le mot "Playeur"
    print("Playeur", joueur, end="" )
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
    #Sinon
    else:
        #Afficher "Erreur"
        print("Erreur")
         #Refaire jouer le joueur 
        play(joueur)



#On definit la fonction "game"
def game():
    #On importe la liste dans la fonction 
    global tablemorph
    #On affiche le message "pour jouer, utilisez les touches du pavé numérique "
    print("Pour jouer, utilisez les touches du pavé numérique")
    #On appel la fonction "grid"
    grid()
    #Tant que c'est vrai 
    while True:
        #On créer une boucle i qui est comprise entre 1 et 2 
        for i in range(1,3):
            #On lance le jeux
            play(i)
            #On appel la fonction grid 
            grid()
            #Si l'une des fonctions "lagagne" est verifier pour le joueur1
            if lagagne()=="joueur1":
                #Alors afficher "Le joueur cool a gagner"
                print("LE JOUEUR 😎 A GAGNER! ")
                #retourner la fonction
                return
            #Si l'une des fonctions "lagagne" est verifier pour le joueur2
            elif lagagne()=="joueur2":
                #Alors afficher "Le joueur neurd a gagner"
                print("LE JOUEUR 🤓 A GAGNER!")
                #retourner la fonction
                return
            #Si la fonction "lagagne " vérifie la fonction "tie" 
            elif lagagne()=="tie":
                #Alors afficher "EGALITE!QUELLE SURPRISE!"
                print("EGALITE!QUELLE SURPRISE!")
                #retourner la fonction
                return
#Appeler la fonction game
game()  



#Fin






# https://github.com/NathanFallet/MorpionTPE/commit/2e2bc099f13a0632a286e1a0425b85f2cf3f7f42






# def ordinateur(IA):
#     global tablemorph
#     if tablemorph[i][o]==1:
#         print('😎',end='')
#     else:
#         #On affiche le neutre "-"
#         print("-", end='')
#         #A la fin d'une liste on va a la ligne 
#     print("",end='\n')

# def jouer(IA):
#     #Afficher Le mot "Playeur"
#     print("Playeur", IA, end="" )
#      #Si c'est le joueur2 
#     if IA==1:
#          #Alors afficher un emoji neurd puis aller a la ligne 
#         print("🤓",end="\n")
#     #Demader au joueur de choisir sa position 
#     entry=[1,10]
#     #Si il choisi "7"
#     if entry=="7":
#         #Si la position en haut a gauche est libre 
#         if (tablemorph[0][0])==0:
#             #Placer l'emoji du joueur en haut a gauche 
#             tablemorph[0][0]= IA
#     #Si il choisi "8"
#     elif entry=="8":
#         #Si la position en haut au milieu est libre 
#         if (tablemorph[0][1])==0:
#             #Placer l'emoji du joueur en haut au milieu
#             tablemorph[0][1]= IA

#     #Si il choisi "9"
#     elif entry=="9":
#         #Si la position en haut a droite est libre 
#         if (tablemorph[0][2])==0:
#             #Placer l'emoji du joueur en haut a droite
#             tablemorph[0][2]= IA

#     #Si il choisi "4"
#     elif entry=="4":
#         #Si la position au milieu a gauche est libre 
#         if (tablemorph[1][0])==0: 
#             #Placer l'emoji du joueur au milieu a gauche
#             tablemorph[1][0]= IA

#     #Si il choisi "5"
#     elif entry=="5":
#         #Si la position au milieu est libre 
#         if (tablemorph[1][1])==0:
#             #Placer l'emoji du joueur au milieu
#             tablemorph[1][1]= IA

#     #Si il choisi "6"
#     elif entry=="6":
#         #Si la position au milieu a droite est libre
#         if (tablemorph[1][2])==0:
#             #Placer l'emoji du joueur au milieu a droite
#             tablemorph[1][2]= IA

#     #Si il choisi "1"
#     elif entry=="1":
#         #Si la position en bas a gauche est libre
#         if (tablemorph[2][0])==0:
#             #Placer l'emoji du joueur en bas a gauche
#             tablemorph[2][0]= IA

#     #Si il choisi "2"
#     elif entry=="2":
#         #Si la position en bas au milieu est libre
#         if (tablemorph[2][1])==0:
#             #Placer l'emoji du joueur en bas au milieu 
#             tablemorph[2][1]= IA 

#     #Si il choisi "3"
#     elif entry=="3":
#         #Si la position en bas a droite est libre 
#         if (tablemorph[2][2])==0:
#             #Placer l'emoji du joueur en bas a droite 
#             tablemorph[2][2]= IA        
#     #Si non si les position de son pas libre ou que le joueur rentre un mauvais numero 
#     else:
#         #Afficher le message "pas possible"
#         print("pas possible")
#         #Refaire jouer le joueur 
#         jouer(IA)


# if joueur==tablemorph[0][0]:
#     coupIA==tablemorph[0][1] or coupIA==tablemorph[0][2] or coupIA==tablemorph[1][0] or coupIA==tablemorph[1][1] or coupIA==tablemorph[1][2] or coupIA==tablemorph[2][0] or coupIA==tablemorph[2][1] or coupIA==tablemorph[2][2]




#     if joueur==tablemorph[0][1]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][1]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[0][2]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][1]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[1][0]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][1]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[1][1]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][1]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[1][2]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][1]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[2][0]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][1]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[2][1]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][2]

#     if joueur==tablemorph[2][2]:
#     coupIA==tablemorph[0][0]
#     or coupIA==tablemorph[0][1]
#     or coupIA==tablemorph[0][2]
#     or coupIA==tablemorph[1][0]
#     or coupIA==tablemorph[1][1]
#     or coupIA==tablemorph[1][2]
#     or coupIA==tablemorph[2][0]
#     or coupIA==tablemorph[2][1]