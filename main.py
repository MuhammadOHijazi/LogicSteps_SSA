from UCS import UCS
from state import State
from solo import UserPlayer
from DFS import DFS
from BFS import BFS
from recursive_DFS import RecursiveDFS
from levels import Levels

lev = Levels.level14
st = State(lev)

print("Logic steps Games")
print("Choose the way to solve the problem")
meth = input("Enter 1 to play the game lonely\n"
             "Enter 2 to solve the problem using BFS algo\n"
             "Enter 3 to solve the problem using DFS algo\n"
             "Enter 4 to solve the problem using DFS Recursively algo\n"
             "Enter 5 to solve the problem using UCS algo\n")
match meth:
    case "1":
        print("Start play the Game by your self")
        user_player = UserPlayer()
        user_player.play()
    case "2":
        print("Solve the game by the Algorithms BFS")
        algo = BFS()
        algo.play()

    case "3":
        print("Solve the game by the  Algorithms DFS")
        algo = DFS()
        algo.play()

    case "4":
        print("Solve the game by the  Algorithms Recursive DFS")
        algo = RecursiveDFS()
        algo.play(st)

    case "5":
        algo = UCS()
        algo.play()

