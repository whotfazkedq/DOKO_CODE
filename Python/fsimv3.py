"""
preparation for v3

now I may add the formations 
or improve loser team randomization
this is for when I wake up xd 
or maybe i'll just continue my game, thing i totally should do
"""

import random 
result = [0, 1, 2]

def ch_res(grlA, grlB):#choose_result
    grlDif = abs(grlA - grlB)

    if grlDif <=5:
        if grlA > grlB: res_we = [45, 30, 25] 
        elif grlA < grlB: res_we = [45, 25, 30] 
        else: res_we = [50, 25, 25]
    elif grlDif in range(6, 11):
        if grlA > grlB: res_we = [30, 45, 25]
        else: res_we = [30, 25, 45]
    elif grlDif in range(11, 21):
        if grlA > grlB: res_we = [20, 65, 15]
        else: res_we = [20, 15, 65]
    elif grlDif in range(21, 36):
        if grlA > grlB: res_we = [10, 85, 5]
        else: res_we = [10, 5, 85]
    elif grlDif in range(36, 99):
        if grlA > grlB: res_we = [5, 94, 1]
        else: res_we = [5, 1, 94]

    return random.choices(result, weights=res_we, k=1)[0]

def ch_winn_goals():#choose_winner_goals
    opt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    opt_we = [20, 16.6, 13.3, 10, 7.7, 5.2, 2.7, 2, 1.5, 1]
    return random.choices(opt, weights=opt_we, k=1)[0]

def ch_score(final_res):#choose_score
    if final_res == 0:
        opt = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        opt_we = [45, 45, 40.6, 35.3, 30, 12.7, 4.2, 1.7, 1, 0.5, 0.01]
        score = random.choices(opt, weights=opt_we, k=1)[0]
        return score, score
    if final_res == 1:
        scoreA = ch_winn_goals()
        if scoreA <= 3: scoreB = random.randint(0, scoreA -1)
        elif scoreA in range(4, 6): scoreB = random.randint(0, scoreA -3)
        elif scoreA in range(6, 8): scoreB = random.randint(0, scoreA -4)
        elif scoreA in range(8, 11): scoreB = random.randint(0, scoreA -5)
        return scoreA, scoreB

    scoreB = ch_winn_goals()
    if scoreA <= 3: scoreB = random.randint(0, scoreA -1)
    elif scoreA in range(4, 6): scoreB = random.randint(0, scoreA -3)
    elif scoreA in range(6, 8): scoreB = random.randint(0, scoreA -4)
    elif scoreA in range(8, 11): scoreB = random.randint(0, scoreA -5)
    return scoreA, scoreB

def readInt(prompt):
    while True:
        raw = input(prompt)
        try:
            value = int(raw)
            if value < 0 or value > 99:
                print("Invalid input, GRL must be inside the asked range")
            else:
                return value
        except ValueError:
            print("Invalid input, enter numbers only")

def main():
    while True:
        opt = [1,   2,    3,   4,   5,   6,   7,  8,  9,  10]
        we = [ 20, 16.6, 13.3, 10, 7.7, 5.2, 2.7, 2, 1.5, 1] 

        print("Random Football Match Score")
        teamA = str(input("Enter the name of Team A: "))
        grlA = readInt(f"Enter {teamA}'s GRL(1-99): ")
        teamB = str(input("Enter the name of Team B: "))
        grlB = readInt(f"Enter {teamB}'s GRL(1-99): ")

        final_res = ch_res(grlA, grlB)
        scoreA, scoreB = ch_score(final_res)
    
        print("\nScore is:")
        print(f"{teamA} {scoreA}:{scoreB} {teamB}")
        if scoreA == scoreB:
            print("Match Result was a tie")
        elif scoreA < scoreB:
            print(f"{teamB} won")
        elif scoreA > scoreB:
            print(f"{teamA} won")

        choice = input("Would you play again? (y/n): ").strip().lower()
        if choice not in ("y", "Yes"):
            break
        
    print("Closing")
if __name__ == "__main__":
    main()