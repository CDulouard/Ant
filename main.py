import modules.Map as Map
import modules.Pathfinding as pf
import sys


def main(args):
    map = Map.Map("maps/MAP_1.txt")
    print(pf.find(1000, map, False))


if __name__ == "__main__":
    main(sys.argv)
