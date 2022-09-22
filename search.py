from turtle import pu
from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN
import copy



def BFS(puzzle):
    """
    Breadth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []


    # TODO: WRITE CODE

    return states_searched, final_solution


def DFS(puzzle):
    """
    Depth-First Search.

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    parent_node = Node(puzzle)
    states_searched = [ Node(puzzle=puzzle, parent=parent_node, move=None) ]
    visited = []
    final_solution = []

    pos_x, pos_y = Node(puzzle).state.zero
    max_x = len(parent_node.state.puzzle) - 1
    max_y = len(parent_node.state.puzzle[0]) - 1

    while states_searched:
        node = states_searched.pop(0)
        if node in visited:
            continue

        visited.append(node)

        if node.state.check_puzzle() :
            print("Solution found at. ", Node(node.state.puzzle).state.print_puzzle())
            return states_searched, final_solution
        
        pos_x, pos_y = node.state.zero

        for i in range(3):
            if i == 0:
                print("---------------------------------")
                print("Current Position: " , pos_x, pos_y)
                print("---------------------------------")
                print("MAX cord", max_x, max_y)

                newx = pos_x - 1
                newy = pos_y
                print("NEW pos: ", newx, newy)

                if newx <= max_x and newx >= 0:
                    print("MOVE UP")
                    clone = copy.deepcopy(node.state)
                    leaf_node = Node(puzzle=puzzle, parent=parent_node, move=UP)
                    leaf_node.state.swap(pos_x, pos_y, newx, newy)
                    print("New puzzle: ")
                    leaf_node.print_puzzle() 
                    states_searched.append(leaf_node)
                    print("---------------------------------")
                else:
                    print("SKIPPING")
                    continue
            elif i == 1:
                print("---------------------------------")
                print("Current Position: " , pos_x, pos_y)
                print("---------------------------------")
                print("MAX cord", max_x, max_y)
                newx = pos_x - 1
                newy = pos_y
                print("NEW pos: ", newx, newy)
                if newx >= 0 and newx <= max_x:
                    print("MOVE LEFT")
                    clone = copy.deepcopy(node.state)
                    leaf_node = Node(puzzle=puzzle, parent=parent_node, move=LEFT)
                    leaf_node.state.swap(pos_x, pos_y, newx, newy)
                    print("New puzzle: ")
                    leaf_node.print_puzzle() 

                    states_searched.append(leaf_node)
                    print("---------------------------------")
                else: 
                    print("SKIPPING")
                    continue
            elif i == 2:
                print("---------------------------------")
                pos_x, pos_y = node.state.zero
                print("Current Position: " , pos_x, pos_y)
                print("---------------------------------")
                newx = pos_x + 1
                newy = pos_y
                if newx >= 0 and newx <= max_x:
                    print("MOVE DOWN") 
                    clone = copy.deepcopy(node.state)
                    leaf_node = Node(puzzle=clone, parent=parent_node, move=DOWN)
                    leaf_node.state.swap(pos_x, pos_y, newx, newy)
                    print("New puzzle: ")

                    states_searched.append(leaf_node) 
                    print("---------------------------------")                 
                else: 
                    print("SKIPPING")
                    continue
            elif i == 3:
                print("---------------------------------")
                print("Current Position: " , pos_x, pos_y)
                print("---------------------------------")
                newx = pos_x
                newy = pos_y + 1
                if newy >= 0 and newy <= max_y:
                    print("MOVE RIGHT")
                    clone = copy.deepcopy(node.state)
                    leaf_node = Node(puzzle=node.state,parent=parent_node, move=RIGHT)
                    leaf_node.state.swap(pos_x, pos_y, newx, newy )
                    print("New puzzle: ")
                    leaf_node.print_puzzle() 
                    states_searched.append(leaf_node)
                    print("---------------------------------")
                else: 
                    print("SKIPPING")
                    continue
            else:
                print("Error")

    # TODO: WRITE CODE

    return states_searched, final_solution



def A_Star_H1(puzzle):
    """
    A-Star with Heuristic 1

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []

    # TODO: WRITE CODE

    return states_searched, final_solution


def A_Star_H2(puzzle):
    """
    A-Star with Heauristic 2

    Arguments:
    - puzzle: Node object representing initial state of the puzzle

    Return:
    states_searched: An ordered list of all states searched.
    final_solution: An ordered list of moves representing the final solution.
    """

    states_searched = [Node(puzzle)]
    final_solution = []

    # TODO: WRITE CODE

    return states_searched, final_solution