import state as stat
import solo as solo

print("Logic steps Games")
print("Choose the way to solve the problem")
meth = input("Enter 1 to play the game lonly\n"
             "Enter 2 to solve the porblem using BFS algo\n"
             "Enter 3 to solve the problem using DFS algo\n")
match meth:
    case "1":
        print("Start play the Game by your self")
        solo.play()
    case "2":
        print("Solve the game by the Algorithms BFS")
    case "3":
        print("Solve the game by the  Algorithms DFS")
