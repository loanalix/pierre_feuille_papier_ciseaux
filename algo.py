
r=12000
s= 1250
e=10
rh=230 

assertion1 = ((365 * 3) /(24 - (16-8))) * (rh) > r == (e * s < r)

15740.625 > 12000 == 12500 < 12000
true    ==       False
false 

assertion1pt1= (((365 * 3) /(24 - (16-8))) * (rh) > r) # true 
assertion1pt2= (e * s < r) # false 

#assertion1===(assertion1pt1==assertion1pt2)
#assertion1===(assertion1pt1==false)
#assertion1===(true==false)
#assertion1===false

print (assertion1)
#PRINT assertion1
#ECRIRE assertion1

#camelCase 
#kebab-case
#PascalCase
#snake_case
 
assertionDEUX = ((365 * 3) /(4 - (12-8))) * (rh) > r == (e * s < r)

assertionDEUXpt1= ((365 * 3) /(4 - (12-8))) * (rh) > r
assertionDEUXpt2 = (e * s < r)

#assertionDEUX===(assertionDEUXpt1==assertionDEUXpt2)
#assertionDEUX===(false==assertionDEUXpt2)
#assertionDEUX===(false==false)
#assertionDEUX=== #false 

def calculPtDeux():
 return ((e * s < r))

assertionDEUX = ((365 * 3) /(4 - (12-8))) * (rh) > r == calculPtDeux(1,2,3)

def add(x,y):
 return(x+y)


def sub(x,y):
 return(x-y)


def multiplite(x,y):
 return(x*y)

def divide(x,y):
 return(x/y)

def modulo(x,y):
 return(x%y)

def calculeSalaireParS(salaireH,HParJO,JOParAn):
    salaireAnnuelle = salaireH*HParJO*JOParAn #je calcule le salaire Annuel
    nbSecondeParAn = 365*24*60*60 #Je calcul le nombre de seconde par an 
    #return( salaireH*HParJO*JOParAn)/(365*24*60*60) 
SalaireAnnuel/NbDeSAnnuelles #je divise mon salaire par le nombre de seconde par an 



def withdrawFees(total,percent):
    #calcule de mon,tant des taxes a retirer
    fees=totale*(percent/100)
    #je retourne mon totale sans les taxes 
    return total-fees

def calcuSalaireNet(salairebrut,public):
    #Si j'occupe un post de la fonction publique
    if public:
    #Alors je retourne le salaire brut -15 % de taxes
         return withdrawFees(salairebrut , 15)
    #Sinon, c'estq ue je suis un travailleur privé,
    else:
    #Alors je retourn le salaire brut - 23% de douille bien a l'ancienne 
        return withdrawFees(salairebrut, 23)



nbPersonne = x

if nbPersonne == 1 :
    tuRentre()
elif nbPersonne == 3 : 
    tuRentre()
elif nbPersonne == 5 :
    tuRentre()
else:
     tuRentrePas()


#calculer le revenu par seconde 
#salaireH
#H/JO
# année /JO  
#calculNET converti depuis brut 
0.000360

def calcuSalaireNet(salairebrut,public):
 #Je calcule le salaire net d'un employé du secteur public 
 if public: return SalaireBrut * 15/100
 #je calcule le salaire net d'un employé d'une entreprise privée
 return SalaireBrut * 23/100 


def div(x,y ):
    #Si Y est 0, alors la division est impossible 
    if y == 0 :
        #Alors afficher un message d'erreur 
        print("ERR:Can't divide by 0")
        #Et renvoyer rien 
        return
    #Sinon,renvoyer la division de X rt Y 
    return x/y 




tour = 0 
# Tanque je ne suis pas au tour 5 
while tour != 5 : 
# Appeler la fonction JouerUnTour
    jouerUnTour()
# J'effectue l'action de passer un tour 
    tour = tour + 1 