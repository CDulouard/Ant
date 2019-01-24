import modules.Map as Map
import modules.Pathfinding as pf


def main():
    map = Map.Map("map")
    pf.find(1, map)


if __name__ == "__main__":
    main()
