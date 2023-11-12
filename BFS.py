from state import State
from levels import Levels


class BFS:
    lev = Levels.level4
    st = State(lev)
    visited = {}

    def play(self):
        queue = []
        queue.append(self.st)
        counter = 0
        while queue:
            counter += 1
            current_state = queue.pop(0)
            self.visited[str(current_state)] = current_state
            parent_key = str(current_state)
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
                for state in next_states:
                    if self.visited.get((str(state)), -1) == -1:
                        print(str(state))
                        queue.append(state)
                        state.parent = parent_key

