class Map:
    """
    fonctions :

    Map : genere la map a partir d un fichier  /!\ la map dois etre rectangulaire ! et etre resolvable
    findinout : trouve la pos des entrees et sortie et les stock dans l'objet
    genemap : genere la map a partir du fichier entre
    show : affiche le terrain
    rewalline : fonctions interne
    rewal : met des murs autour du terrain
    test : affiche les deux tableaux et in et out
    initweight : cree le tableau de poids
    modifcell : modifie une cellule /!\ passer par les fonctions de ant pour modifier le tableau
    get_cellat : donne le type de case aux coordonnees donnees
    get_start : retourne la position de la case de depart sous forme de tupple
    get_exit : retourne la position de la case d arrivee sous forme de tupple
    """

    map_ = []
    weights_ = []
    start_ = []
    exit_ = []

    def __init__(self, path):
        self.genemap(path)
        self.rewall()
        self.initweights()
        self.findinout()

    def findinout(self):
        for i in range(len(self.map_)):
            for j in range(len(self.map_[i])):
                if self.map_[i][j] == "I":
                    self.start_ = [i, j]
                if self.map_[i][j] == "O":
                    self.exit_ = [i, j]

    def genemap(self, path):
        file = open(path, "r")
        content = file.read()
        lines = content.split()

        for i in range(len(lines)):
            self.map_.append([])
            for j in range(len(lines[i])):
                self.map_[i].append(lines[i][j])

        file.close()

    def show(self):

        for i in self.map_:
            print()
            for j in i:
                print(j, end='')
        print()

    def rewalline(self, line):
        ans = ['w']
        for i in line:
            ans += [i]
        ans += ['w']
        return ans

    def rewall(self):
        """
        met des murs autours de la map de forme rectangulaire
        """
        height = len(self.map_)
        width = len(self.map_[0])

        self.map_.append([])
        self.map_.append([])
        line = self.map_[0]

        for i in range(height):
            temp = self.map_[i + 1]
            self.map_[i + 1] = self.rewalline(line)
            line = temp

        self.map_[0] = ["w"] * (width + 2)
        self.map_[height + 1] = ["w"] * (width + 2)

    def test(self):
        print(len(self.map_))
        for i in self.map_:
            print(i)
        for i in self.weights_:
            print(i)
        print("IN : {}".format(self.start_))
        print("OUT : {}".format(self.exit_))

    def initweights(self):
        for i in range(len(self.map_)):
            self.weights_.append([])
            for j in range(len(self.map_[i])):
                if self.map_[i][j] == 'w':
                    self.weights_[i].append([-1, 0])
                else:
                    self.weights_[i].append([0, 0])

    def modficell(self, posy, posx, value):
        self.map_[posy][posx] = value

    def get_cellat(self, y, x):
        return self.map_[y][x]

    def get_start(self):
        return self.start_[0], self.start_[1]

    def get_exit(self):
        return self.exit_[0], self.exit_[1]
