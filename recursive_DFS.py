from state import State
from levels import Levels


class RecursiveDFS:
    lev = Levels.level4
    st = State(lev)
    visited = {}

    def play(self, state):
        stack = []
        stack.append(state)
        counter = 0
        if not stack:
            return
        current_state = stack.pop()
        self.visited[str(current_state)] = current_state
        parent_key = str(current_state)
        print(current_state)
        if current_state.isfinish():
            if current_state.to_win > 0:
                return
            path = []
            temp_state = current_state
            while temp_state.parent != "":
                path.append(temp_state)  # win state -> root
                temp_state = self.visited[temp_state.parent]
            for node in path[::-1]:
                print(node)
                print("---------------------------------------")
            print("path:", len(path), "\nstates:", counter)
            return
        else:
            next_states = current_state.next_state()
            last_in = next_states[-1]
            for state in next_states:
                if self.visited.get((str(state)), -1) == -1:
                    print(str(state))
                    stack.append(state)
                    state.parent = parent_key
                    last_in = state
            self.play(last_in)





