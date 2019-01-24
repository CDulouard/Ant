import modules.Ant as Ant


def find(nbants, map, show=True):
    """
    Fonction de recherche de solution à modifier pour trouver le meilleur chemin
    :param nbants: nombre de fourmis a tester
    :param map: map de jeu
    :return:
    """

    myant = Ant.Ant()
    print(myant.find_path(map, show))
