import random

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
            if i < 8:
                print(" ---+---+---")

# fonction pour vérifier si un joueur a gagné
def victoire(symbole):
    return (
        (board[0] == board[1] == board[2] == symbole) or
        (board[3] == board[4] == board[5] == symbole) or
        (board[6] == board[7] == board[8] == symbole) or
        (board[0] == board[3] == board[6] == symbole) or
        (board[1] == board[4] == board[7] == symbole) or
        (board[2] == board[5] == board[8] == symbole) or
        (board[0] == board[4] == board[8] == symbole) or
        (board[2] == board[4] == board[6] == symbole)
    )

# fonction pour le choix de l'IA
def choix_ia():
# si l'IA peut gagner, elle joue cette case
    for i in range(9):
        if board[i] == case_vide:
            board[i] = signe[1]
            if victoire(signe[1]):
                board[i] = case_vide
                return i
            board[i] = case_vide

# sinon, si le joueur humain peut gagner, bloquer cette case
    for i in range(9):
        if board[i] == case_vide:
            board[i] = signe[0]
            if victoire(signe[0]):
                board[i] = case_vide
                return i
            board[i] = case_vide

# sinon, choisir une case libre au hasard
    cases_libres = [i for i in range(9) if board[i] == case_vide]
    return random.choice(cases_libres)

# définir le boucle While pour avoir un boucle répétitif   
while True:

 # Appel du fonction Affiche_Tableaux 
    affichage_Tableaux()
    choix_joueur = 0

# tour du joueur humain (X)
    if joueur == signe[0]:
        while True:
            try:
                choix_joueur = int(input("Donnez une case entre 1 et 9 : "))
                if 1 <= choix_joueur <= 9 and board[choix_joueur - 1] == case_vide:
                    break
                else:
                    print("Case invalide ou déjà prise, réessayez.")
            except:
                print("Veuillez entrer un nombre entre 1 et 9.")
        board[choix_joueur - 1] = joueur

# tour de l'IA (O)
    else:
        choix_ia_index = choix_ia()
        board[choix_ia_index] = joueur

# Appel un funtion Victoir et le tableaux pour qu'un joueur gagne
    if victoire(joueur):
        affichage_Tableaux()
        if joueur == signe[0]:
            print(f"Le joueur {joueur}a gagné la partie !")
    
        break

# définir si toutes les cases sont remplies → match nul
    elif case_vide not in board:
        affichage_Tableaux()
        print("Match Nul !")
        break

# définir si le premier joueur prend X alors l'autre prend directement O
    if joueur == signe[0]:
        joueur = signe[1]
    else:
        joueur = signe[0]
