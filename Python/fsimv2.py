import random

def main():
    while True:
        opt = [1,   2,    3,   4,   5,   6,   7,  8,  9,  10]
        we = [ 20, 16.6, 13.3, 10, 7.7, 5.2, 2.7, 2, 1.5, 1] 
        result = [0, 1, 2]

        print("Random Football Match Score")
        teamA = str(input("Enter the name of Team A: "))
        grlA = int(input(f"Enter {teamA} GRL(0-99): "))
        teamB = str(input("Enter the name of Team B: "))
        grlB = int(input(f"Enter {teamB} GRL(0-99): "))
        grlDif = abs(grlA - grlB)
        while grlDif <= 5:
            if grlA > grlB:
                res_we = [45, 30, 25]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            elif grlA < grlB:
                res_we = [45, 25, 30]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            elif grlA == grlB:
                res_we = [50, 25, 25]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            break

        while grlDif in range(6, 10):
            if grlA > grlB:
                res_we = [30, 45, 25]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            elif grlA < grlB:
                res_we = [30, 25, 45]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            break

        while grlDif in range(11, 25):
            if grlA > grlB:
                res_we = [20, 65, 15]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            elif grlA < grlB:
                res_we = [20, 15, 65]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            break

        while grlDif in range(26, 50):
            if grlA > grlB:
                res_we = [10, 85, 5]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            elif grlA < grlB:
                res_we = [10, 5, 85]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            break

        while grlDif in range(51, 99):
            we = [1, 2, 3, 4, 5, 6, 7, 8, 8, 8] 
            if grlA > grlB:
                res_we = [5, 94, 1]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            elif grlA < grlB:
                res_we = [5, 1, 94]
                final_res = random.choices(result, weights=res_we, k=1)[0]
            break


        if final_res == 0:
            opt = [0, 1,    2,   3,   4,   5,  6,  7,  8,  9,  10]
            we = [45, 45, 40.6, 35.3, 30, 12.7, 4.2, 1.7, 1, 0.5, 0.01]
            scoreA = random.choices(opt, weights=we, k=1)[0]
            scoreB = scoreA
        elif final_res == 1:
            scoreA = random.choices(opt, weights=we, k=1)[0]
            if scoreA <= 3:
                scoreB = random.randint(0, (scoreA - 1))
            elif scoreA in range(3, 5):
                scoreB = random.randint(0, (scoreA - 3))
            elif scoreA in range(6, 10):
                scoreB = random.randint(0, (scoreA - 5))
        elif final_res == 2:
            scoreB = random.choices(opt, weights=we, k=1)[0]
            if scoreB <= 3:
                scoreA = random.randint(0, (scoreB - 1))
            elif scoreB in range(3, 5):
                scoreA = random.randint(0, (scoreB - 3))
            elif scoreB in range(6, 10):
                scoreA = random.randint(0, (scoreB - 5))

    
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