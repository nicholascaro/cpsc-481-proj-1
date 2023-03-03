from search import *
# YOUR CODE GOES HERE

class WolfGoatCabbage(Problem):
    def __init__(self, initial = frozenset({'G', 'F', 'C', 'W'}), goal=set()):
        super().__init__(initial, goal)
        self.farmer = frozenset({"F"})
        self.all = frozenset({'G', 'F', 'C', 'W'})
        self.farmer_goat = frozenset({'G', 'F'})
        self.wolf_cabbage = frozenset({'W', 'C'})
        self.wolf_cabbage_farmer = frozenset({'W', 'C', 'F'})
        self.wolf_goat_farmer = frozenset({'W', 'G', 'F'})
        self.farmer_cabbage = frozenset({'C', 'F'})
        self.farmer_wolf = frozenset({'W', 'F'})
        self.wolf = frozenset({'W'})
        self.goat = frozenset({'G'})
        self.cabbage = frozenset({'C'})
        self.cabbage_goat_farmer = frozenset({'C', 'G', 'F'})

    
    def goal_test(self, state):
        """returns True if the given state is a goal state"""
        return state == self.goal
    def result(self, state, action):
        """returns the new state reached from the given state 
        and the given action. Assume that the action is valid."""
        if action.issubset(state):
            return state - action
        else:
            return state.union(action)
    
    def actions(self, state):
        """returns a list of valid actions in the given state"""
        valid_actions = list()
        if state == self.all:
            valid_actions.append(self.farmer_goat)
            return valid_actions
        elif state == self.wolf_cabbage:
            valid_actions.append(self.farmer)
            return valid_actions
        elif state == self.wolf_cabbage_farmer:
            valid_actions.append(self.farmer_cabbage)
            valid_actions.append(self.farmer_wolf)
            return valid_actions
        elif state == self.cabbage:
            valid_actions.append(self.farmer_goat)
        elif state == self.wolf:
            valid_actions.append(self.farmer_goat)
            valid_actions.append(self.farmer_cabbage)
            return valid_actions
        elif state == self.wolf_goat_farmer:
            valid_actions.append(self.farmer_wolf)
            return valid_actions
        elif state == self.goat:
            valid_actions.append(self.farmer)
            return valid_actions
        elif state == self.farmer_goat:
            valid_actions.append(self.farmer_goat)
            return valid_actions
        elif state == self.cabbage_goat_farmer:
            valid_actions.append(self.farmer_cabbage)
            return valid_actions
        return valid_actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)