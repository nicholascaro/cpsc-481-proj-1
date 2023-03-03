from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial={'F', 'W', 'G', 'C'}, goal={}):
        super().__init__(initial, goal)

    def goal_test(self, state):
        """returns True if the given state is a goal state"""
        return state == self.goal

    def result(self, state, action):
        """returns the new state reached from the given state
        and the given action. Assume that the action is valid."""
        return 'to be implemented'

    def actions(self, state):
        """returns a list of valid actions in the given state"""
        return "to be implemented"


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    goal_test = wgc.goal_test(set())
    print('goal_test: ', goal_test)

    result = wgc.result(set({'F', 'W', 'G', 'C'}), set({'F', 'G'}))
    print('result: ', result)

    actions = wgc.actions(set({'F', 'W', 'G', 'C'}))
    print('actions: ', actions)

    # solution = depth_first_graph_search(wgc).solution()
    # print(solution)
    # solution = breadth_first_graph_search(wgc).solution()
    # print(solution)
