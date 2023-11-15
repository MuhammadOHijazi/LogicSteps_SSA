from abc import ABC
from Algo import Algo
from state import State
from levels import Levels


class BFS(Algo, ABC):
    lev = Levels.level4
    st = State(lev)
    visited = {}

    def print_path(self, current_state):
        self.path = []
        temp_state = current_state
        while temp_state.parent != "":
            self.path.append(temp_state)  # win state -> root
            temp_state = self.visited[temp_state.parent]
        for node in self.path[::-1]:
            print(node)
            print("---------------------------------------")

    # def is_Win(self, current_state):
    #     self.check = True
    #     for player in current_state.players:
    #         if current_state.can_move(player[0], player[1]):
    #             self.check = False
    #     if self.check:
    #         print("There should be", current_state.to_win, "moves To finish the game")
    #         print("There is no place you can go with your players\n"
    #               "sorry but you lost the level")
    #         print("Your players in places\n", current_state.players)
    #         return

    def play(self):
        queue = []
        queue.append(self.st)
        counter = 0
        while queue:
            counter += 1
            # print(counter)
            current_state = queue.pop(0)
            self.visited[str(current_state)] = current_state
            parent_key = str(current_state)
            # check if the current state is a win state
            if current_state.isfinish():
                self.print_path(current_state)
                for node in self.path[::-1]:
                    print(node)
                    print("---------------------------------------")
                print("path:", len(self.path), "\nstates:", counter)
                print("You Win Congrats")
                return
            else:
                next_states = current_state.next_state()
                for state in next_states:
                    if self.visited.get((str(state)), -1) == -1:
                        queue.append(state)
                        state.parent = parent_key
