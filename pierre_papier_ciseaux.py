
import random 
#On admet une fonction random qui donnera au hasard les valeurs de 0 a 3
#On admet une fonction imput qui récupère le nom du joueur
nom=input("Veuillez saisir votre nom")
joueur1=0
joueur2=0
nuls=0
#Tant que le coup du joueur 1 est different de "q" on lance le jeu 
while True:
 print(nom,joueur1,"égalités:",nuls,"joueur2",joueur2)
 coupjoueur1=input("entrez votre coup: (p)ierre,(f)euille,(c)iseaux ou (q)uitter:")
 #Si coupjoueur1 est "q" 
 if coupjoueur1=="q":
    #Alors affiché "quitté le jeu"
    print("vous avez quitté le jeu")
    #Arreter la boucle 
    break
#Si coupjoueur1 est different "p" "f" et "c" 
 if coupjoueur1!="p" and coupjoueur1!="f" and coupjoueur1!="c":
    #La boucle continue
    continue
#Si coupjoueur1 est "p"
 if coupjoueur1=="p":
    #Alors affiché "pierre contre"
    print("pierre contre")
 elif coupjoueur1=="f":
    #Alors affiché "feuille contre"
    print("feuille contre")
#Si le coup joueur est p    
 elif coupjoueur1=="c":
    #Alors affiché "ciseaux contre"
    print("ciseaux contre")

#on lance la fonction randome nomée r 
 r=random.randint(1,3)
 #si r verifie 1 
 if r==1:
   #Alors le coup du joueur 2 est pierre 
    coupjoueur2="p"
    print("pierre")
   #si r verifie 2 
 elif r==2:
   #Alors le coup du joueur 2 est feuille
    coupjoueur2="f"
    print("feuille")
   #sinon le coup du joueur 2 est ciseaux 
 else:
    coupjoueur2="c"
    print("ciseaux")
#si le coup du jouer 2 est le même que celu du joueur 1 
 if coupjoueur1==coupjoueur2:
   #Afficher "partie nulle "
    print("partie nulle")
    nuls=nuls+1

 #Si le coup joueur 1 est "p" et le coup joueur2 est "c"  
 elif coupjoueur1=="p" and coupjoueur2=="c":
    #Afficher "vous avez gagné "
    print("vous avez gagné")
    #Ajouer plus 1 au joueur1 
    joueur1=joueur1+1
 #Si le coup joueur 1 est "p" et le coup joueur2 est "f" 
 elif coupjoueur1=="p" and coupjoueur2=="f":
    #Afficher "partie perdu "
    print("vous avez perdu")
    #Ajouer plus 1 au joueur2 
    joueur2=joueur2+1
 #Si le coup joueur 1 est "f" et le coup joueur2 est "c" 
 elif coupjoueur1=="f" and coupjoueur2=="c":
   #Afficher "vous avez perdu "
    print("vous avez perdu")
    #Ajouer plus 1 au joueur2 
    joueur2=joueur2+1
 #Si le coup joueur 1 est "f" et le coup joueur2 est "p" 
 elif coupjoueur1=="f" and coupjoueur2=="p":
    #Afficher "vous avez gagné "
    print("vous avez gagné")
    #Ajouer plus 1 au joueur1 
    joueur1=joueur1+1
 #Si le coup joueur 1 est "c" et le coup joueur2 est "p" 
 elif coupjoueur1=="c" and coupjoueur2=="p":
    #Afficher "vous avez perdu "
    print("vous avez perdu")
    #Ajouer plus 1 au joueur2 
    joueur2=joueur2+1
 #Si le coup joueur 1 est "c" et le coup joueur2 est "f" 
 elif coupjoueur1=="c" and coupjoueur2=="f":
    #Afficher "vous avez gagné "
    print("vous avez gagné")
    #Ajouer plus 1 au joueur1 
    joueur1=joueur1+1













    #phase test 



    #Debut 
#On admet une fonction random qui donnera au hasard les valeurs de 0 a 3
#On admet une fonction imput qui récupère le choix du joueur 
#import random 

#On définit une fonction Playeur avec la variable choixPlayer tel que
#def Playeur (choixPlayer) : 
    #On initialise Pierre égale a 1
    #Pierre = 1 
    #On initialise Feuille égale a 2
    #Feuille = 2 
    #On initialise Ciseau égale a 3
    #Ciseau = 3 
    #On initialise fin du jeux a 4
    #fin = 4 
    #On definit la variable choixPlayer entrée par l'utilisateur avec le retourde la fonction Input
    #choixPlayer = int(input)
    
#On retourne la variable choixPlayer
#return choixPlayer 

#On definit la fonction ordinateur avec la variable IAChoix tel que 
#def ordinateur (IAChoix) : 
    #int(choixPlayer)  
    #r=random.randint(1,2,3) 
    
    #On definit la variable IAChoix avec le retour de l'execution de la  fonction Random 

    #Si la variable est égale a 1
     
        #Alor on affiche "pierre"

    #Si la variable est égale a 2 
        #Alor on affiche "feuille" 

    #Si la variable est égale a 3 
         #Alor on affiche "ciseaux"  


#On définit une fonction Resultat telle que
    
    #Si la variable choixPlayer est égale variable IAChoix  
    #If choixPlayer == IAChoix  
        #Alors on affiche "Egalité !"
        #print("Egalité")

    #Si la variable choixPlayer est égale à 1 et que la variable IAChoix est égale à 3 
    #If choixPlayer == 1 and IAChoix == 3 
        #Alors on affiche "Le joueur a gagné"
         #print("vous avez gagné")

    #Si la variable choixPlayer est égale à 2 et que la variable IAChoix est égale à 1 
    #If choixPlayer == 1 and IAChoix == 3 
        #Alor son affiche "Le joueur a gagné"
         #print("vous avez gagné")

    #Si la variable choixPlayer est égale à 3 et que la variable IAChoix est égale à 2  
    #If choixPlayer == 1 and IAChoix == 3 
        #Alors on affiche "Le joueur a gagné"
         #print("vous avez gagné")

    #Si la variable choixPlayer est égale à 1 et que la variable IAChoix est égale à 2  
    #If choixPlayer == 1 and IAChoix == 3 
        #Alors on affiche "Le joueur a perdu"
         #print("vous avez perdu")

    #Si la variable choixPlayer est égale à 2 et que la variable IAChoix est égale à 3  
    #If choixPlayer == 1 and IAChoix == 3 
        #Alors on affiche "Le joueur a perdu"
         #print("vous avez perdu")

    #Si la variable choixPlayer est égale à 3 et que la variable choixIA est égale à 1 
    #If choixPlayer == 1 and IAChoix == 3 
        #Alors on affiche "Le joueur a perdu"
        # print("vous avez perdu")


#Tant que choixPlayer est different de 4 
    #Alor demander "Choisir un nombre 1 et 3" 
        #Executer choixPlayer
        #Executer IAChoix
        #Executer Resultat   

#Fin