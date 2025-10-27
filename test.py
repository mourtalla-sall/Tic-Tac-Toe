
# case_vide = " "
# board = [case_vide in range(9)]
# def affichage_Tableaux():
#     for i in range(9):
#         print()
#         print(f" {board[i] } ", end="|")
#         if i % 3 == 2:
#          print("|")
#          print(" ----+----+----")

# affichage_Tableaux()

case_vide = " "
board = [case_vide for i in range(9)]

def affichage_Tableaux():
    for i in range(9):
        print(f" {board[i]} ", end="|")
        if i % 3 == 2:
            print()
            if i != 8:
                print("---+---+----")

affichage_Tableaux()
