import modules.Map as Map
import modules.Pathfinding as pf
import sys


def main(args):
    map = Map.Map("maps/MAP_ULTIMATE")
    print(pf.find(50, map, False, 1000000))


if __name__ == "__main__":
    main(sys.argv)
