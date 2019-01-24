import modules.Map as Map
import modules.Pathfinding as pf
import sys


def main(args):
    map = Map.Map("maps/Map_1.txt")
    print(pf.find(1, map, False))


if __name__ == "__main__":
    main(sys.argv)
