tablemorph = [
        ["0" , "0" , "0"] ,
        ["0" , "0" , "0"] ,
        ["0" , "0" , "0"]
    ]


def grid() :
    global tablemorph
    for i in range(3):
            for o in range(3):
                if tablemorph[i][o]==1:
                    print('😎',end='')
                elif tablemorph[i][o]==2:
                    print('🤓',end='')
                else:
                    print("", end='')
            print("",end='\n')

def lagagne():
    global tablemorph
    col=0
    row=0
    check1=0
    check2=0
    winner = "none"
    #gagner a l'horizontal
    for col in range(3):
        for row in range(3):
            if tablemorph[col-1][row-1]==1:
                check1=check1+1
            elif tablemorph[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="joueur1"
            elif check2==3:
                winner="joueur2"
        check1=0
        check2=0
    #gagner a la vertical 
    for row in range(3):
        for col in range(3):
            if tablemorph[col-1][row-1]==1:
                check1=check1+1
            elif tablemorph[col-1][row-1]==2:
                check2=check2+1
            if check1==3:
                winner="joueur1"
            elif check2==3:
                winner="joueur2"
        check1=0
        check2=0

    #gagner en bias de gauche à droite
    for case in range(3):
        if tablemorph[case-1][case-1]==1:
            check1=check1+1
        elif tablemorph[case-1][case-1]==2:
            check2=check2+1
        if check1==3:
            winner="joueur1"
        elif check2==3:
            winner="joueur2"
    #gagner en bias de droite à gauche
    if tablemorph[0][2]==tablemorph[1][1]==tablemorph[2][0]:
        if tablemorph[0][2]==1:
            winner="joueur1"
        elif tablemorph[0][2]==2:
            winner="joueur2"
    check1 = 0
    check2 = 0

    #ganer pour egalité
    look = 0
    for i in range(3):
        for o in range(3):
            if tablemorph[i][o] != 0:
                look = look + 1
    if look==9:
        winner="tie"
    return winner

def play(joueur):
    print("joueur1", joueur, end="" )
    if joueur==1:
        print("😎",end="\n")
    if joueur==2:
        print("🤓",end="\n")

    entry=input()
    if entry=="7":
        if tablemorph[0][0]==0:
            tablemorph[0][0]=joueur

    elif entry=="8":
        if tablemorph[0][1]==0:
            tablemorph[0][1]=joueur

    elif entry=="9":
        if tablemorph[0][2]==0:
            tablemorph[0][2]=joueur()
    
    elif entry=="4":
        if tablemorph[1][0]==0:
            tablemorph[1][0]=joueur

    elif entry=="5":
        if tablemorph[1][1]==0:
            tablemorph[1][1]=joueur

    elif entry=="6":
        if tablemorph[1][2]==0:
            tablemorph[1][2]=joueur

    elif entry=="1":
        if tablemorph[2][0]==0:
            tablemorph[2][0]=joueur

    elif entry=="2":
        if tablemorph[2][1]==0:
            tablemorph[2][1]=joueur  

    elif entry=="3":
        if tablemorph[2][2]==0:
            tablemorph[2][2]=joueur        

    else:
        print("pas possible")
        play(joueur)

def game():
    global tablemorph
    print("Pour jouer, utilisez les touches du pavé numérique")
    grid()
    while True:
        for i in range(1,3):
            play(i)
            grid()
            if lagagne()=="joueur1":
                print("LE JOUEUR 😎 A GAGNER! ")
                return
            elif lagagne()=="joueur2":
                print("LE JOUEUR 🤓 A GAGNER!")
                return
            elif lagagne()=="tie":
                print("EGALITE!QUELLE SURPRISE!")
                return

game()  





