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
    print(parent_node)
    states_searched = [Node(puzzle, parent=parent_node, move=None)] # queue
    print(states_searched[0])
    
    ##print(Node(puzzle).state.puzzle)
    ##print(Node(puzzle.swap(2,0, 0 ,0)))

    path = [] #Visited
    final_solution = []

    while states_searched:

        vertex = states_searched.pop(0)
        print(vertex.state.puzzle)
        if vertex in path: # leaf nodde or visited, go to next item. 
            continue
        
        path.append(vertex) 
        if vertex.state.check_puzzle():
            print("vertex is a solved problem.")
            return states_searched, final_solution
        # calculate how many moves i can make then add them to stack? YES add to states_se

        print("UP")
        nx = 0
        ny = 0
        for x in range(len(vertex.state.puzzle)):
            for y in range(len(vertex.state.puzzle[0])):
                if vertex.state.puzzle[x][y] == 0:
                    nx += x
                    ny += y
                    break

        print(nx)
        print(ny)

        for i in range(3):## can only generate a max of <=4 new moves
            if i == 0:
                print("UP")

            elif i == 1:
                print("LEFT")

            elif i == 2:
                print("Down")
            
            else:
                print("Error.")


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