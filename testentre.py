"Les tabelaux"




tableau = [0,10,15,5,14,7,6,3,4,8,9,5,1,7,5,2,1,8,4,4,6,8]

#Pour recuperer 15 je prends dans le tableau l'index 3-1 
print(tableau[2]) #Renvoie 15

len(tableau) #Renvoi la longeur de tableau 

prenom = "Alexandre"
nom = " Delaistre"

nomPrenom = nom + prenom #Renvoie DelaistreAlexandre 
nomPrenom = nom +" " + prenom #Renvoie Delaistre Alexandre 
intergerValue =342
stringIntergerValue = str(342) #Renvoie "342" au lieu de 342


#Exercice1 
#Faire une fonction qui concatene 2 chaine de caractere , les separants par une virgule 

#Definir une fonction w/ comme parametres : chaineA et chaineB
#qui retourne la concatenation de chaineA, une comma et enfin chaine
def concatWithComma(chaineA, chaineB): 
    #Je m'assure que chaineA soit bien de type str
    stringifiedChaineA = str(chaineA)
    #Je m'assure que chaineA soit bien de type str
    stringifiedChaineB = str(chaineB)
    #Retourner chaineA concatené w/ un comma et chaineB
    return stringifiedChaineA + " , "+ stringifiedChaineB


#Exercice2 
#Fairte une fonction qui itere sur tout les index d'un tableau renvoyant une chaine de" caractere 
#avec l'ensemble des occuration d'un chiffre e.g.:
#Pour un tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0,4,7" n'hesitez pas a implementer la premiere fonction ; 


tableau = [0,1,1,1,0,1,1,0,1]
#Definir une fonction qui prend une liste et une variable x quelconque 
def findIndexes(tableau,x) :
    #Initialiser i a 0
    i = 0
    #Definir chaineResultat en tan que string 
    ChaineResultat = ""
    #On determine firstTurn a true 
    firstTurn = True 
    #Tant que i est inferieur a la longeur de tableau 
    while i< len(tableau) :
            #Alors Si l'elt d'index i de tableau est egal a x
        if tableau[i] == x :
            # Alors 
            print("")
            #Si je suis au premier tour ( Si firstTurn est true )
        if firstTurn: 
                #Alors j'assigne str(i) a chaine resultat
            ChaineResultat = str(i)
                #On passe firstTurn a false
            firstTurn = False 
            #Sinon on assige a chaine resultat le retour de concatWithComma(chaineResultat, str(i))    
            ChaineResultat = concatWithComma (ChaineResultat , str(i))
        #On incremente i de 1 
    i=i+1
    #Retourner chaineResultat
    return ChaineResultat




tableauMultiType = ["Alexandre" , True , tableau, 4 > 2, None ]
tableau = [0,1,2,3]
tableauMultiDim = [ tableauDim1 , tableauMultiDim2]
tableauMultiDim[1][2] # Renvoie 21

tableauCleVal = {"Cle" : "Valeur" }
tableauCleVal["Cle"] #Renvoie "Valeur"

#Tel que 
listeUtilisateur ={
    "Alexandre" : "motdepasse",
    "Michel" : "password" ,
    "Toto" : "12345" ,
    "JhonDoe" : "azerty"
} 

#Ecrivez la fonction login(userName, pasword, listUser) permettant d'afficher un message de connexion si 
#le combo user/password est bon 

def mlg(userName, pasword): 
    #trouver l'utilisateur dans la liste 
    #trouver son mot de pass dans la liste 

    print(mlg)

