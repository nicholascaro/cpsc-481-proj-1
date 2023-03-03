from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=frozenset()):
        super().__init__(initial, goal)

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

        def is_restricted(state):
            restrictions = [frozenset({'W', 'G'}), frozenset({'G', 'C'})]
            for restriction in restrictions:
                if restriction.issubset(state):
                    return True
            return False

        actions = []
        # can farmer leave alone?
        bank = state.copy()
        bank = bank - frozenset({'F'})
        if not is_restricted(bank):
            actions.append(frozenset({'F'}))

        # can farmer take one item?
        for item in bank:
           items = bank.copy() - frozenset({item})
           if not is_restricted(items):
               actions.append(frozenset({'F', item}))

        return actions


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    goal_test = wgc.goal_test(frozenset())
    print('goal_test: ', goal_test)

    # result = wgc.result(frozenset({'F', 'W', 'G', 'C'}), frozenset({'F', 'G'}))
    # print('new state: ', result)

    result = wgc.result(frozenset({'W'}), frozenset({'F', 'C'}))
    print('new state: ', result)

    actions = wgc.actions(frozenset({'F','G', 'C'}))
    print('actions: ', actions)

    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
