#definir u par n 
#initialiser unUn comme egale a 0 et unDeux comme egale a 1 
#afficher le u
#Tanque la suite n'est pas arreter 
    #Alors ajouter un-1 a u
    #afficher le nouveau u 
#retourner la fonction de la suite  




#On crée une fonction fibonachi qui prend en parametre les nombre d'élément dans la liste 
def fibo (b) :
    #On crée une liste qui va contenir les elements de la suite 
    l = []
    #On cree un incrementeur pour la boucle 
    i = 0 
    #On met dans une variable le premier element de la suite qui est 0
    elem1 = 0 
    #On met dans une autre variable le deuxieme element de la liste 
    elem2 = 1
    #Si le parametre est egale a 1 
    if b == 1 :
        #Alors on ajoute dans la liste le premier element et on la retourne 
        l.append(elem1)
        return
    #Tant que i est inferieur à b 
    while i < b : 
        #On cree une variable temporaire qui va stoker la somme des deux dernier element 
        somme == elem1 + elem2 
        #On ajout à la liste la variable somme 
        l.append(somme)
        #On réatribu la bonne valeur a elem1 et elem2
        elem1 = elem2
        elem2 = 1[-1]
        #On ajoute 1 à i 
        i = i + 1 
    #Puis on retourne la liste 
    return customJoin(1)    