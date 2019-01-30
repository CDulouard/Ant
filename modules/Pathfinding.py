import modules.Ant as Ant


def find(nbants, map, show=True, TTL=100000):
    """
    Fonction de recherche de solution à modifier pour trouver le meilleur chemin
    :param nbants: nombre de fourmis a tester
    :param map: map de jeu
    :return: Nombre de mouvements moyens
    """
    avgmove = 0
    bestmove = 100000000000000
    for i in range(nbants):

        myant = Ant.Ant()
        count = myant.find_path_memory(map, show, TTL)

        if count < bestmove:
            bestmove = count

        avgmove += count
        print("ant : {} : ".format(i + 1), count)

    myant.show_best_path(map)

    print("Meilleur chemin trouve : ", Ant.Ant.memory_)
    print("Longueur meilleur chemin : {}".format(bestmove))

    return avgmove / nbants
