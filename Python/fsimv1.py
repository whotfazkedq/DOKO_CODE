import random

def main():
    while True:
        opt = [0, 1,    2,   3,   4,   5,  6,  7,  8,  9,  10]
        we = [20, 20, 16.6, 13.3, 10, 7.7, 5.2, 2.7, 2, 1.5, 1] 

        print("Random Football Match Score")
        teamA = str(input("Enter the name of Team A: "))
        teamB = str(input("Enter the name of Team B: "))


        scoreA = random.choices(opt, weights=we, k=1)[0]
        scoreB = random.choices(opt, weights=we, k=1)[0]

        print("\nScore is:")
        print(f"{teamA} {scoreA}:{scoreB} {teamB}")
        if scoreA == scoreB:
            print("Match Result was a tie")
        elif scoreA < scoreB:
            print(f"{teamB} won")
        elif scoreA > scoreB:
            print(f"{teamA} won")

        choice = input("Would you play again? (y/n): ").strip().lower()
        if choice not in ("y", "Y", "yes", "Yes"):
            break
        
        print("Closing")
if __name__ == "__main__":
    main()