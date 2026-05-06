import random
score = 0
total_questions = 0
bad_luck_answers = 0
streak = 0
power_up_in = 10
rounds_till_attack = 2
attack_power= 1
enamy_health=2
damage = 0
hit_till_deaf = 0
double_turn = 0
debt = 0
classs= 0
def clas():
    global classs
    print("      here are your random classes for this round      ")
    print("-------------------------------------------------------")
    class1= random.randint(1,3)
    if class1 == 1:
        print("tax collector/ get 2x points on questions")
    elif class1 == 2:
        print("hacker/ just hack if yu see the prompt")
    elif class1 == 3:
        print("warier/ get 2x damage end of every turn")
    class2= random.randint(1,3)
    if class2 == 1:
        print("tax collector/ get 2x points on questions")
    elif class2 == 2:
        print("hacker/ just hack if yu see the prompt")
    elif class2 == 3:
        print("warier/ get 2x damage end of every turn")
    selected = input("1 or 2: ")
    if selected == 1:
        classs= class1
    elif selected == 2:
        classs= class2
def reset():
    global score
    global total_questions
    global bad_luck_answers
    global streak
    global power_up_in
    global rounds_till_attack
    global attack_power
    global enamy_health
    global damage
    global hit_till_deaf
    global double_turn
    global debt
    score = 0
    total_questions = 0
    bad_luck_answers = 0
    streak = 0
    power_up_in = 10
    rounds_till_attack = 2
    attack_power= 1
    enamy_health=2
    damage = 0
    hit_till_deaf = 0
    double_turn = 0
    debt = 0
def tic_tack_toe():
    global damage
    print("-----------tic tack toe started-----------")
    board = [" "] * 9
    def print_board():
        print()
        for i in range(0, 9, 3):
            print(" " + " | ".join(board[i:i+3]))
            if i < 6:
                print("---+---+---")
        print()
    def check_winner(player):
        win_positions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(board[i] == player for i in combo) for combo in win_positions)
    def player_move():
        while True:
            try:
                move = int(input("Choose position (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("Invalid position.")
                    continue
                if board[move] != " ":
                    print("That spot is taken.")
                    continue
                return move
            except ValueError:
                print("Enter a number.")
    def ai_move():
        empty = [i for i in range(9) if board[i] == " "]
        return random.choice(empty)
    for turn in range(9):
        print_board()
        if turn % 2 == 0:
            move = player_move()
            board[move] = "X"
        else:
            move = ai_move()
            print(f"AI picks {move + 1}")
            board[move] = "O"
        if check_winner("X"):
            print_board()
            print("You win!")
            print("you won a password")
            print("Redpanda@67")
            return
        if check_winner("O"):
            print_board()
            print("AI wins!")
            return
    print_board()
    print("It's a draw!")
reset()
clas()
while True:
    a = random.randint(1, 2)
    b = random.randint(1, 2)
    answer2 = a + b
    answer3 = a - b
    symbol = random.randint(1, 2)
    if symbol == 1:
        print(f"\n{a} + {b}")
    else:
        print(f"\n{a} - {b}")
    answer = input("Answer: ")
    is_correct = False
    if symbol == 1:
        if int(answer) == answer2:
            is_correct = True
    else:
        if int(answer) == answer3:
            is_correct = True
    if is_correct:
        print("yes")
        if classs == 1:
            score += 2
        else:
            score += 1
        streak += 1
        power_up_in -= 1
    else:
        print("no")
        bad_luck_answers += 1
        streak = 0
    total_questions += 1
    rounds_till_attack -= 1
    if power_up_in <= 0:
        bonus = random.randint(1, 10)
        score += bonus
        print(f"POWER UP! +{bonus} points!")
        power_up_in = random.randint(5, 10)
    if rounds_till_attack <= 0:
        print("your score is" ,score)
        print("--- attack started: pick a card ---")
        print("1. weak foot troop: cost 1 point: damage 10: health 5")
        print("2. general soldier: cost 10 point: damage 20: health 10")
        print("3. megaknight: cost 20 point: damage 30: health 15")
        print("4. elite knight: cost 30 point: damage 40: health 30")
        print("5. baby dragon: cost 40 point: damage 80: health 50")
        print("6. mr brown on a code dragon(best in the game): cost 1000 point: damage 24395: health 99999999999999999")
        print("7. the card pack: basic: cost 5 point: damage 0: packs: 1")
        print("8. Frieza: cost 150: damage start at 2 but doubles evary turn: health 100 : abilatys damage doubles evary turn")
        print("9. lets play tic tack toe cost free: prize if you win")
        print("10.why would you do this it is absalutly nothing: cost free: dose nothing")
        print("11.admin only password required to buy: cost free: ability changes realaty")
        card = input("pick your card (1/2/3/4/5/6/7/8/9/10/11): ")
        if card == "1":
            print("You chose the weak foot troop.")
            score -= 1
            damage += 10
            hit_till_deaf += 5
        elif card == "2":
            print("You chose the general soldier.")
            score -= 10
            damage += 20
            hit_till_deaf += 10
        elif card == "3":
            print("You chose the megaknight.")
            score -= 20
            damage += 30
            hit_till_deaf += 15
        elif card == "4":
            print("You chose the elite knight.")
            score -= 30
            damage += 40
            hit_till_deaf += 30
        elif card == "5":
            print("You chose the baby dragon.")
            score -= 40
            damage += 80
            hit_till_deaf += 50
        elif card == "6":
            print("You chose mr brown on a code dragon.")
            score -= 1000
            damage += 24395
            hit_till_deaf += 99999999999999999
        elif card == "7":
            print("You chose a abilaty pack.")
            score -= 5
            damage += 1
            hit_till_deaf += 1
            random_card1 = random.randint(1,6)
            random_card2 = random.randint(1,6)
            random_card3 = random.randint(1,6)
            print("----------card 1 is----------")
            if random_card1 == 1:
                print("2x damage")
            if random_card1 == 2:
                print("-10 damage")
            if random_card1 == 3:
                print("+1 megaknight")
            if random_card1 == 4:
                print("+1 baby dragon")
            if random_card1 == 5:
                print("+1 absalutly nothing")
            if random_card1 == 6:
                print("+100 damage")
            print("----------card 2 is----------")
            if random_card2 == 1:
                print("2x damage")
            if random_card2 == 2:
                print("-10 damage")
            if random_card2 == 3:
                print("+1 megaknight")
            if random_card2 == 4:
                print("+1 baby dragon")
            if random_card2 == 5:
                print("+1 absalutly nothing")
            if random_card2 == 6:
                print("+100 damage")
            bonous= input("pick a card: ")
            if bonous == 1:
                if random_card2 == 1:
                    damage= damage + damage
                if random_card2 == 2:
                    damage -= 10 
                if random_card2 == 3:
                    score -= 20
                    damage += 30
                    hit_till_deaf += 15
                if random_card2 == 4:
                    score -= 40
                    damage += 80
                    hit_till_deaf += 99999999999999999
                if random_card2 == 5:
                            if bonous == 1:
                                if random_card2 == 1:
                                    damage= damage + damage
                                if random_card2 == 2:
                                    damage -= 10 
                                if random_card2 == 3:
                                    score -= 20
                                    damage += 30
                                    hit_till_deaf += 15
                                if random_card2 == 4:
                                    score -= 40
                                    damage += 80
                                    hit_till_deaf += 99999999999999999
                                if random_card2 == 5:
                                    print("absalutly nothing")
                                if random_card2 == 6:
                                    damage += 100
        elif card == "8":
            print("have you done the quest?")
            quest = input("y/n: ")
            score -= 150
            if quest == "y":
                if score >= 100:
                    double_turn += 2
                    hit_till_deaf += 100
                    score -= 150
                else:
                    print("your a liar and your pants are on fire")
        elif card == "9":
            tic_tack_toe()
            print("---------------------------------")
        elif card == "10":
            damage += 1000000
            hit_till_deaf += 9999999999
            debt += -10
            score += int(input("how much score to lose: "))
        elif card == "11":
            print("You chose :;'[{4jc@]['!")
            print("you need a password to acsess")
            password = input("enter your password: ")
            if password == "Redpanda@67":
                score = int(input("set your score: "))
                hit_till_deaf = int(input("enter your new health: "))
                damage = int(input("enter your new damage: "))
        rounds_till_attack = random.randint(2, 5)
        while hit_till_deaf > 0 and enamy_health > 0:
            hit_till_deaf -= attack_power
            enamy_health -= damage
            print("your health is" ,hit_till_deaf)
            print("enamy health is" ,enamy_health)
        if hit_till_deaf == 0:
            print("you died: reseting now")
            reset()
        else:
            print("you win: you may continue")
            enamy_health += damage + 15
            attack_power += 1
            score += 69
        double_turn += double_turn
        if score < -999:
            print(f"score={score} | total={total_questions} | wrong={bad_luck_answers} | streak={streak} | next_powerup={power_up_in} | attack_in={rounds_till_attack} | debt={debt}")
            reset()
    if score > 10:
        tic_tack_toe()
    no = input("reset (y/n): ")
    if no == "y":
        reset()
    if classs == 2:
        hack = input("enter the amount to gain 1-20: ")
        if hack < 20:
            print("to big you lost the chance")
        else:
            score += hack
            print("score added")
            print(" you score is now" ,score)
    if classs == 3:
        damage += damage
    print(f"score={score} | total={total_questions} | wrong={bad_luck_answers} | streak={streak} | next_powerup={power_up_in} | attack_in={rounds_till_attack} | debt={debt}")