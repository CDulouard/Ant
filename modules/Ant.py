import modules.Map as Map
import random


class Ant:
    """
    Fonctions :
    spawn : pose la fourmi a l entree de la map
    get_yant : recupere position y de la fourmi
    get_xant : recupere position x de la fourmi
    moveto : deplace la fourmi à la position donnee si possible
    scan : retourne les positions possibles autour de la fourmi (retourne uniquement la pos de la sortie si a cote)
    watchcell : regarde le type de la case aux coordonnees donnees par rapport a la fourmi
    ia : retourne la position ou aller
    find_path : deplace la fourmi jusqu a trouver la sortie et retourne le nombre de deplacement


    Consigne :

    Modifier ia (eventuellement find_path) pour obtimiser le deplacement de la fourmi

    """
    path_ = []  # le chemin emprunte par la fourmi
    memory = []  #la memoire de la fourmi
    count = 0   # le nombre de deplacement de la fourmi
    xant_ = 0  #position en x de la fourmi
    yant_ = 0  #position en y de la fourmi
    location_ = ''  # La valeur de la case de la case



    def spawn(self, map):
        self.yant_, self.xant_ = map.get_start()
        self.location_ = map.get_cellat(self.yant_, self.xant_)
        map.modficell(self.yant_, self.xant_, "A")

    def moveto(self, map, posy, posx):
        if map.get_cellat(posy, posx) != "w" and (((posy - self.yant_) + (posx - self.xant_) == 1) or ((posy - self.yant_) + (posx - self.xant_) == -1)):
            map.modficell(self.yant_, self.xant_, self.location_)
            self.yant_, self.xant_ = posy, posx
            self.location_ = map.get_cellat(self.yant_, self.xant_)
            map.modficell(self.yant_, self.xant_, "A")

    def get_yant(self):
        return self.yant_

    def get_xant(self):
        return self.xant_

    def scan(self, map):
        possibilities = []

        y, x = 1, 0

        value = self.watchcell(map, y, x)
        if value != "w":
            if value == "O":
                possibilities = [[self.yant_ + y, self.xant_ + x]]
                return possibilities
            possibilities += [[self.yant_ + y, self.xant_ + x]]

        y, x = 0, 1

        value = self.watchcell(map, y, x)
        if value != "w":
            if value == "O":
                possibilities = [[self.yant_ + y, self.xant_ + x]]
                return possibilities
            possibilities += [[self.yant_ + y, self.xant_ + x]]

        y, x = -1, 0

        value = self.watchcell(map, y, x)
        if value != "w":
            if value == "O":
                possibilities = [[self.yant_ + y, self.xant_ + x]]
                return possibilities
            possibilities += [[self.yant_ + y, self.xant_ + x]]

        y, x = 0, -1

        value = self.watchcell(map, y, x)
        if value != "w":
            if value == "O":
                possibilities = [[self.yant_ + y, self.xant_ + x]]
                return possibilities
            possibilities += [[self.yant_ + y, self.xant_ + x]]

        return possibilities

    def watchcell(self, map, y, x):
        """
        :param y: distance y depuis notre pos
        :param x:  distance x depuis notre pos
        :return: valeur de la case regardée
        """
        return map.get_cellat(self.yant_ + y, self.xant_ + x)

    def ia(self, possibilities):
        choice = random.randint(0, len(possibilities) - 1)
        return possibilities[choice]

    def find_path(self, map):
        exit = map.get_exit()
        self.spawn(map)
        while self.yant_ != exit[0] or self.xant_ != exit[1]:
            choice = self.ia(self.scan(map))
            posx = choice[1]
            posy = choice[0]
            self.moveto(map, posy, posx)
            map.show()
            self.count += 1
        return self.count
