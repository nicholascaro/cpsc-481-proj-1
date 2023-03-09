from search import *
if __name__ == '__main__':
    eight_puzzle = EightPuzzle(initial=(1,2,3,5,7,4,8,6,0))
    print("\nA* Search\n")
    astar_search(eight_puzzle, h=None, display=True)
    print("\nBFS\n")
    breadth_first_graph_search(eight_puzzle, display=True)
    print("\nDFS\n")
    depth_first_graph_search(eight_puzzle, display= True)


    