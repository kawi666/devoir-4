﻿from q4d1 import show_m

"""
Le tableau du jeu sera représenté par [y][x]

  x1 x2 x3
y1
y2
y3

[
    [c, c, c],
    [c, c, c],
    [c, c, c],
]

donc les sous tableaux représentent les lignes
"""

def inverse(tab):

    if all([list == type(e) for e in tab]):
        for l in tab:
            inverse(l)
    
    if all([int == type(e) for e in tab]):
        tab[0], tab[1] = tab[1], tab[0]


def effaceTableau (tab):
    '''
    (list) -> None
    Cette fonction prepare le tableau de jeu (la matrice) 
    en mettant '-' dans tous les elements.
    Elle ne crée pas une nouvelle matrice
    Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    # a completer
    
    # si la matrice est n x n, on peut dire que la longeur du tableau est la même longeur que les sous tableaux
    n = len(tab)

    for y in range(n):
        for x in range(n):
            tab[y][x] = '-'

    # retourne rien

      
def verifieGagner(tab):  
    '''(list) ->  bool
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    * Verifie s'il y a un gagnant.
    * Cherche pour 3 X's et O's dans une ligne, colonne, et diagonal.
    * Si on a trouvé, affiche le gagnant (le message "Joueur X a gagné!" 
    * ou "Joueur O a gagné!") et retourne True.
    * S'il y a un match nul (verifie ca avec la fonction testMatchNul),
    * affiche "Match nul" et retourne True.
    * Si le jeu n'est pas fini, retourne False.
    * La fonction appelle les fonctions testLignes, testCols, testDiags
    * pour verifier s'il y a un gagnant.
    * Ces fonctions retournent le gagnant 'X' ou 'O', ou '-' s'il n'y a pas de gagnant
    '''

    # a completer

    # voir plus bas

    return False  # a changer

def test(combos, tab):
    for combo in combos:
        fx, fy = combo[0]
        compare = tab[fy][fx]
        print(f"testing with first cell {fx, fy} -> {compare}")
        o = ''
        for x, y in combo:
            o += f"{tab[y][x]} "
        print(o)

        if all(compare == tab[y][x] for x, y in combo):
            print('All Equal')

def testLignes(tab):
    ''' (list) ->  str
    * verifie s’il y a une ligne gagnante.
    * cherche trois 'X' ou trois 'O' dans une ligne.  
    * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    # a completer

    combos = [[[x, y] for x in range(3)] for y in range(3)]
    # print(combos)
    show_m(combos)
    test(combos, tab)
    inverse(combos)
    show_m(combos)
    test(combos, tab)

    
    return '-' # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant 

  
  
def testCols(tab):
   ''' (list) ->  str
   * verifie s’il y a une colonne gagnante.
   * cherche trois 'X' ou trois 'O' dans une colonne.  
   * Si on trouve, le caractere 'X' ou 'O' et retourné, sinon '-' est retourné.
   * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
   '''
    
   # a completer
  
   return '-'   #a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

   
def testDiags(tab):
    ''' (list) ->  str
    * cherche trois 'X' ou trois 'O' dans une diagonale.  
    * Si on trouve, le caractere 'X' ou 'O' et retourné
    * sinon '-' est retourné.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''

    # a completer
        
    return '-'   # a changer pour retourner le gagnant, ou '-' s'il n'y a pas de gagnant

  
  
def testMatchNul(tab):
    ''' (list) ->  bool
    * verifie s’il y a un match nul
    * verifie si tous les elements de la matrice contiennent X ou O, pas '-'.  
    * Si on ne trouve pas de '-' dans la matrice, retourne True. 
    * S'il y a de '-', retourne false.
    * Preconditions: tab est une reference a une matrice n x n qui contient '-', 'X' ou 'O'
    '''
        
    # a completer
    
    return False  # a changer

