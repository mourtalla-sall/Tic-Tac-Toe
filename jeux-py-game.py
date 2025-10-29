import pygame, sys

pygame.init()

# Constantes 
WIDTH, HEIGHT = 600, 600
TAILLE_CASE = WIDTH // 3
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')

case_vide = " "
signe = ("X", "O")
joueur = signe[0]
board = [case_vide for _ in range(9)]
jeu_termine = False
gagnant = None

# --- Fonction d'affichage du plateau ---
def affichage_Tableaux():
    screen.fill(BLANC)

# Dessiner la grille
    for i in range(1, 3):
        pygame.draw.line(screen, NOIR, (i * TAILLE_CASE, 0), (i * TAILLE_CASE, HEIGHT), 4)
        pygame.draw.line(screen, NOIR, (0, i * TAILLE_CASE), (WIDTH, i * TAILLE_CASE), 4)


# Afficher les symboles et le taille 
    font = pygame.font.Font(None, 150)
    for i in range(9):
        symbole = board[i]
        if symbole != case_vide:
            x = (i % 3) * TAILLE_CASE + 70
            y = (i // 3) * TAILLE_CASE + 30
            texte = font.render(symbole, True, NOIR)
            screen.blit(texte, (x, y))

# Si le jeu est terminé → afficher le gagnant
    if jeu_termine:
        afficher_gagnant(gagnant)

    pygame.display.flip()

# Vérifier les condition pour gagner
def verifier_gagnant(board):
    combinaisons = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in combinaisons:
        if board[a] == board[b] == board[c] != case_vide:
            return board[a]
    if case_vide not in board:
        return "Égalité"
    return None

# Afficher le gagnant
def afficher_gagnant(gagnant):
    font = pygame.font.Font(None, 70)
    if gagnant == "Égalité":
        message = "Match nul !"
    else:
        message = f"Le joueur {gagnant} gagne la partie !"
    texte = font.render(message, True, NOIR)
    rect = texte.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(texte, rect)




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Gestion clic souris pour que l'utilusateur clic sur l'interface 
        if event.type == pygame.MOUSEBUTTONDOWN and not jeu_termine:
            x, y = event.pos
            col = x // TAILLE_CASE
            row = y // TAILLE_CASE
            index = row * 3 + col

            if board[index] == case_vide:
                board[index] = joueur
                gagnant = verifier_gagnant(board)
                if gagnant:
                    jeu_termine = True
                else:
                    joueur = "O" if joueur == "X" else "X"

      

    affichage_Tableaux()
