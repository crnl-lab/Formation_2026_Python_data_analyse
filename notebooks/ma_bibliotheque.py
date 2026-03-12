

def affiche_un_beau_triangle(n: int =10):
    for i in range(n):
        print('|' + (' ' * i) + '\\')
    print('-' * (n + 1))


def affiche_un_beau_triangle_tete_en_bas(n: int =10):
    print('_' * (n + 2))
    for i in range(n):
        print('|' + (' ' * (n - i)) + '/')
    

