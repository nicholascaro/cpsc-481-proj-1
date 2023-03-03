from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=({'F', 'W', 'G', 'C'}, {}), goal=({}, {'F', 'W', 'G', 'C'})):
        super().__init__(initial, goal)

    def goal_test(self, state):
        """returns True if the given state is a goal state"""
        return state == self.goal

    def result(self, state, action):
        """returns the new state reached from the given state
        and the given action. Assume that the action is valid."""
        if 'F' in state[0]:
            for item in action:
                state[0].remove(item)
                state[1].add(item)
        else:
            for item in action:
                state[1].remove(item)
                state[0].add(item)

    def actions(self, state):
        """returns a list of valid actions in the given state"""

        def is_restricted(state):
            """returns True if the given state is restricted"""
            restrictions = [{'W', 'G'}, {'G', 'C'}]
            for restriction in restrictions:
                if restriction.issubset(state):
                    return True
            return False

        actions = []
        bank = state[0] if 'F' in state[0] else state[1]

        # can farmer return alone?
        bank = bank.copy()
        bank.remove('F')
        if not is_restricted(bank):
            actions.append({'F'})

        # can farmer return with one item?
        for item in bank:
            items = bank.copy()
            items.remove(item)
            if not is_restricted(items):
                actions.append({'F', item})


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
