# Déffinir les varibles 
case_vide = " "
signe = ("X", "O")
joueur = signe[0]

# initialliation d'un tableaux afin d'afficher tous les 9 cases par une boucle for 
board = [case_vide for i in range(9)]


# Définir un fonction Affiche_Tableaux pour que l'utilusateur voir comment il est le Tableau avant de commencer
def affichage_Tableaux():
    for i in range(9):
        print("|", board[i], end=" ")
        if i % 3 == 2:
         print("|")
         print(" ---+---+---")


# définir comment doit etre les ligne  pour qu'un le joureur gagne
def verifier_victoire():
    return (
        case_vide != board[0] == board[1] == board[2] or
        case_vide != board[3] == board[4] == board[5] or
        case_vide != board[6] == board[7] == board[8] or
        case_vide != board[0] == board[3] == board[6] or
        case_vide != board[1] == board[4] == board[7] or
        case_vide != board[2] == board[5] == board[8] or
        case_vide != board[0] == board[4] == board[8] or
        case_vide != board[2] == board[4] == board[6]
    )


# définir le boucle While pour avoir un boucle répétitif   
while True:

#Appel du fonction Affiche_Tableaux 
    affichage_Tableaux()
    choix_joueur = 0

# définir boucle while pour conditionner aux utilisateurs sur les valeur à mettre  
    while True:
        try:
            choix_joueur = int(input("Donnez une case entre 1 et 9 : "))
            if 1 <= choix_joueur <= 9 and board[choix_joueur - 1] == case_vide:
                break
            else:
                print("Case invalide ou déjà prise, réessayez.")
        except:
            print("Veuillez entrer un nombre entre 1 et 9.")

    board[choix_joueur -1] = joueur

# appel la fonction qui vérifie qu'un joureur gagne
    if verifier_victoire():
        print(f"le joueur {joueur} a gagné la partis !")
        affichage_Tableaux()
        break
# définir si tout les case sont remplient alors c'est un mmatch null
    elif case_vide not in board:
        print("Match Null !")
        break


# définir si le premiére jour prend X alors l'autre prend directement O
    if joueur == signe[0]:
        joueur= signe[1]
    else:
        joueur = signe[0]    
   