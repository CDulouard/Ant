import modules.Map as Map
import modules.Pathfinding as pf
import sys


def main(args):
    map = Map.Map("map")
    print(pf.find(10000, map, False))
    map.test()


if __name__ == "__main__":
    main(sys.argv)
