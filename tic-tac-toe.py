case_vide = " "
signe = ("❌", "⭕")
joueur = signe[0]
board = [case_vide for i in range(9)]

def affichage_Tableaux():
    for i in range(9):
        print("|", board[i], end=" ")
        if i % 3 == 2:
         print("|")
         print(" ---+---+---")


   
while True:
    affichage_Tableaux()
    choix_joueur = 0

    while choix_joueur < 1 or choix_joueur > 9 or board[choix_joueur -1] != case_vide:
        choix_joueur = int(input("Donnez une case entre 0 à 9 :"))

    board[choix_joueur -1] = joueur

# définir comment doit etre les ligne  pour qu'un le joureur gagne
    if case_vide != board[0] ==  board[1] ==  board[2] \
    or  case_vide != board[3] ==  board[4] ==  board[5] \
    or  case_vide != board[6] ==  board[7] ==  board[8]  \
    or  case_vide != board[0] ==  board[3] ==  board[6]  \
    or  case_vide != board[1] ==  board[4] ==  board[7]  \
    or  case_vide != board[2] ==  board[5] ==  board[8]  \
    or  case_vide != board[0] ==  board[4] ==  board[8]  \
    or  case_vide != board[2] ==  board[4] ==  board[6]  :
        print(f"le joueur {joueur} a gagné la partis !")
        affichage_Tableaux()
        break
    elif case_vide not in board:
        print("Match Null !")

    if joueur == signe[0]:
        joueur= signe[1]
    else:
        joueur = signe[0]    
   