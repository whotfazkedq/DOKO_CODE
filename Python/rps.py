import random
import time
game = ['Rock', 'Paper', 'Scissors']
cpu = random.choice(game)

def tie():
    return print("Result was a tie")

def win():
    return print("You win")

def lose():
    return print("CPU win")

def main():
    print("Rock-Paper-Scissor game")
    while True:
        while True:
            print("a) Rock")
            print("b) Paper")
            print("c) Scissors")
            player = str(input("Choose your move: ")).strip().lower()
            if player == 'a':
                pl_print = 'Rock'
            elif player == 'b':
                pl_print = 'Paper'
            elif player == 'c':
                pl_print = 'Scissors'
            print(f"\nYou chose {pl_print}")
            break
        print("Waiting")
        time.sleep(1)
        print("Waiting.")
        time.sleep(1)
        print("Waiting..")
        time.sleep(1)
        print("Waiting...")
        time.sleep(1)

        print(f"CPU chose {cpu}")
        if player == 'a' and cpu == 'Rock':
            tie()
        elif player == 'b' and cpu == 'Paper':
            tie()
        elif player == 'c' and cpu == 'Scissors':
            tie()
        elif player == 'a' and cpu == 'Paper':
            lose()
        elif player == 'a' and cpu == 'Scissors':
            win()
        elif player == 'b' and cpu == 'Rock':
            win()
        elif player == 'b' and cpu == 'Scissors':
            lose()
        elif player == 'c' and cpu == 'Paper':
            win()
        elif player == 'c' and cpu == 'Rock':
            lose()
        else:
            print("That's not an available option")
        

        choice = input("Would you like to try again? (y/n): ").strip().lower()
        if choice not in ("y", "Y"):
            break

        print("Closing")
if __name__ == "__main__":
    main()