import modules.Map as Map
import modules.Pathfinding as pf
import sys
import modules.Display as dp

def main(args):
    map = Map.Map("maps/map3")
    print(pf.find(10, map, False, 10000))
    dp.display(args, map)



if __name__ == "__main__":
    main(sys.argv)
