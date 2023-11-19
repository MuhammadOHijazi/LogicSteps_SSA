from abc import abstractmethod


def is_stuck(current_state):
    check = True
    for player in current_state.players:
        if current_state.can_move(player[0], player[1]):
            check = False
    return check


class Algo:
    @abstractmethod
    def print_path(self, current_state):
        pass
