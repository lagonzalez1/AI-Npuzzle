from helpers import Node, NPuzzle, LEFT, RIGHT, UP, DOWN


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
    states_searched = [Node(puzzle=puzzle, parent=parent_node, move=None)]
    visited = []
    final_solution = []

    pos_x, pos_y = Node(puzzle).state.zero
    max_x = len(parent_node.state.puzzle) - 1
    max_y = len(parent_node.state.puzzle[0]) - 1

    while states_searched:
        node = states_searched[0]
        visited.append(node)

        if node.state.check_puzzle() :
            print("Solution found at. ", node.state.puzzle.depth)
            print(node.state.print())
            break

        for i in range(3):
            if i == 0:
                print("UP")
                pos_x, pos_y = node.state.zero
                new_x = pos_x - 1
                new_y = pos_y
                if new_x <= max_x and new_x >= 0:
                    pos_x, pos_y = node.state.zero
                    leaf_node = Node(puzzle=node.state, parent=parent_node, move=UP).state.swap(pos_x, pos_y, new_x, new_y)
                      # this shoudl be a node?
                    states_searched.append(leaf_node)
                    print("Creating new leaf node from up move",leaf_node.state.print_puzzle())
                    print( pos_x, pos_y )
                    print( new_x, new_y )
                    continue
                else:
                    continue
            elif i == 1:
                print("LEFT")
                pos_x, pos_y = node.state.zero
                new_x = pos_x
                new_y = pos_y - 1
                if new_y >= 0 and new_y <= max_y:
                    print("ENTER")
                    pos_x, pos_y = node.state.zero

                    leaf_node = Node(puzzle=node.state, parent=parent_node, move=LEFT).state.swap(pos_x, pos_y, new_x, new_y)
                    states_searched.append(leaf_node)
                    print("Creating new leaf node from up move",leaf_node.state.print_puzzle())
                    print( pos_x, pos_y )
                    print( new_x, new_y )
                    continue
                else: 
                    continue
            elif i == 2:
                print("DOWN")
                pos_x, pos_y = node.state.zero
                new_x = pos_x + 1
                new_y = pos_y
                if new_x >= 0 and new_x <= max_x:
                    pos_x, pos_y = node.state.zero

                    #leaf_node = Node(puzzle=node.state.puzzle, parent=parent_node, move=DOWN).state.swap(pos_x, pos_y, new_x, new_y)
                    leaf_node = Node(puzzle=node.state, parent=parent_node, move=DOWN).state.swap(pos_x, pos_y,new_x, new_y)
                    # this shoudl be a node? 

                    states_searched.append(leaf_node)
                    print("Creating new leaf node from up move", leaf_node.state.print_puzzle() )
                    print( pos_x, pos_y )
                    print( new_x, new_y )                    
                    continue
                else: 
                    continue
            elif i == 3:
                print("RIGHT")
                pos_x, pos_y = node.state.zero
                new_x = pos_x
                new_y = pos_y + 1
                if new_y >= 0 and new_y <= max_y:
                    pos_x, pos_y = node.state.zero

                    leaf_node = Node(puzzle=node.state, parent=parent_node, move=RIGHT).state.swap(pos_x, pos_y, new_x, new_y)
                      # this shoudl be a node? 
                    states_searched.append(leaf_node)
                    print("Creating new leaf node from up move",leaf_node.state.print_puzzle())
                    print( pos_x, pos_y )
                    print( new_x, new_y )
                    continue
                else: 
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