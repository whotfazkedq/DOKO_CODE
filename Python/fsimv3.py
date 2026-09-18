"""
preparation for v3

now I may add the formations and everything it adds such as players rating, mvp, scorers, assisters, etc
or improve loser team randomization
this is for when I wake up xd 
or maybe i'll just continue my game, thing i totally should do
"""

import random 
result = [0, 1, 2]

def formA(teamA):
    ch_formA = ""
    print("1. 4-4-2")
    print("2. 4-3-3")
    print("3. 3-5-2")
    print("4. 4-5-1")
    print("5. 4-2-4")
    print("6. 3-4-3")
    print("7. 4-2-3-1")
    print("8. 3-4-2-1")
    print("9. 4-1-4-1")
    print("10. 3-3-4")
    ch_form_num = str(input(f"Which formation does {teamA} use? "))
    if ch_form_num == '1':
        ch_formA = '4-4-2'
    elif ch_form_num == '2':
        ch_formA = '4-3-3'
    elif ch_form_num == '3':
        ch_formA = '3-5-2'
    elif ch_form_num == '4':
        ch_formA = '4-5-1'
    elif ch_form_num == '5':
        ch_formA = '4-2-4'
    elif ch_form_num == '6':
        ch_formA = '3-4-3'
    elif ch_form_num == '7':
        ch_formA = '4-2-3-1'
    elif ch_form_num == '8':
        ch_formA = '3-4-2-1'
    elif ch_form_num == '9':
        ch_formA = '4-1-4-1'
    elif ch_form_num == '10':
        ch_formA = '3-3-4'
    else:
        print("Invalid option, please try again")
        return formA(teamA)
    return print(f"{teamA} formation is {ch_formA}")

def formB(teamB):
    ch_formB = ""
    print("1. 4-4-2")
    print("2. 4-3-3")
    print("3. 3-5-2")
    print("4. 4-5-1")
    print("5. 4-2-4")
    print("6. 3-4-3")
    print("7. 4-2-3-1")
    print("8. 3-4-2-1")
    print("9. 4-1-4-1")
    print("10. 3-3-4")
    ch_form_num = str(input(f"Which formation does {teamB} use? "))
    if ch_form_num == '1':
        ch_formB = '4-4-2'
    elif ch_form_num == '2':
        ch_formB = '4-3-3'
    elif ch_form_num == '3':
        ch_formB = '3-5-2'
    elif ch_form_num == '4':
        ch_formB = '4-5-1'
    elif ch_form_num == '5':
        ch_formB = '4-2-4'
    elif ch_form_num == '6':
        ch_formB = '3-4-3'
    elif ch_form_num == '7':
        ch_formB = '4-2-3-1'
    elif ch_form_num == '8':
        ch_formB = '3-4-2-1'
    elif ch_form_num == '9':
        ch_formB = '4-1-4-1'
    elif ch_form_num == '10':
        ch_formB = '3-3-4'
    else:
        print("Invalid option, please try again")
        return formB(teamB)
    return print(f"{teamB} formation is {ch_formB}")
 

def ch_res(grlA, grlB):
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

def ch_winn_goals():
    opt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    opt_we = [20, 16.6, 13.3, 10, 7.7, 5.2, 2.7, 2, 1.5, 1]
    return random.choices(opt, weights=opt_we, k=1)[0]

def ch_score(final_res):
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

    if final_res == 2:
        scoreB = ch_winn_goals()
        if scoreB <= 3: scoreA = random.randint(0, scoreB -1)
        elif scoreB in range(4, 6): scoreA = random.randint(0, scoreB -3)
        elif scoreB in range(6, 8): scoreA = random.randint(0, scoreB -4)
        elif scoreB in range(8, 11): scoreA = random.randint(0, scoreB -5)
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
        print("Random Football Match Score")
        teamA = str(input("Enter the name of Team A: "))
        grlA = readInt(f"Enter {teamA}'s GRL(1-99): ")
        formA(teamA)
        teamB = str(input("Enter the name of Team B: "))
        if teamA == teamB:
            print("Both teams can't have the same name, change at least one character (ex: TeamA1,TeamA2)")
            choice = input("Do you wanna retry from the beginning? (y/n): ").strip().lower()
            if choice in ("y", "Yes"):
                main()
            elif choice not in ("y", "Yes"):
                print("Closing")
                return
        grlB = readInt(f"Enter {teamB}'s GRL(1-99): ")
        formB(teamB)

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