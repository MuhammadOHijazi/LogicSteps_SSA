from state import State
from levels import Levels


class Algo:
    lev = Levels.level3
    st = State(lev)
    visited = {}

    # visited[str(st)] = st
    # print(visited.keys())

    def DFS(self):
        stack = []
        stack.append(self.st)
        counter = 0
        while stack:
            counter += 1
            current_state = stack.pop()
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
                print("winnnnnn!!!!")
                print("path:", len(path), "\nnodes:", counter)
                return
            else:
                next_states = current_state.next_state()
                for state in next_states:
                    if self.visited.get((str(state)), -1) == -1:
                        # print(str(state))
                        stack.append(state)
                        state.parent = parent_key

