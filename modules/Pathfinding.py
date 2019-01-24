import modules.Ant as Ant


def find(nbants, map, show=True):
    """
    Fonction de recherche de solution à modifier pour trouver le meilleur chemin
    :param nbants: nombre de fourmis a tester
    :param map: map de jeu
    :return: Nombre de mouvements moyens
    """
    avgmove = 0
    for i in range(nbants):
        print("ant : {}".format(i + 1))
        myant = Ant.Ant()
        avgmove += myant.find_path(map, show)

    myant = Ant.Ant()
    myant.gofast(map)

    return avgmove / nbants
