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

def concat(a,b): # je definit un fonction a et b 
    return a + " , "+ b  # je retoure les fonction a et b en les séparant par une virgule 


#Exercice2 
#Fairte une fonction qui itere sur tout les index d'un tableau renvoyant une chaine de" caractere 
#avec l'ensemble des occuration d'un chiffre e.g.:
#Pour un tableau = [0,1,1,1,0,1,1,0,1]
#la fonction(tableau,0) doit renvoyer "0,4,7" n'hesitez pas a implementer la premiere fonction ; 









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

