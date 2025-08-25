import random
mylist=["rock","paper","scissor"]
computer_win_count=0
user_win_count=0
tie_count=0
invalid_count=0
total_matches_count=0
while 1:
    total_matches_count += 1
    print(f"Game{total_matches_count}")
    computer_choice = (random.choice(mylist))
    user_choice = input("the user chioce is")
    print(f"Computer choice is {computer_choice}")
    if computer_choice == user_choice:
            print(f"the game is tie,computer choice is {computer_choice} and the user choice is {user_choice}")
            tie_count+=1
    elif computer_choice == "rock" and user_choice == "paper":
            print("user: won")
            print("computer:lost")
            user_win_count+=1
    elif computer_choice == "rock" and user_choice == "scissor":
            print("computer : won")
            print("user: lost")
            computer_win_count+=1
    elif computer_choice == "scissor" and user_choice == "rock":
            print("user: won")
            print("computer:lost")
            user_win_count+=1
    elif computer_choice == "scissor" and user_choice == "paper":
            print("computer : won")
            print("user: lost")
            computer_win_count+=1
    elif computer_choice == "paper" and user_choice == "rock":
            print("computer : won")
            print("user: lost")
            computer_win_count+=1
    elif computer_choice == "paper" and user_choice == "scissor":
            print("user: won")
            print("computer:lost")
            user_win_count+=1
    else:
        if user_choice == "quit":
            total_matches_count-=1
            break
        else:
            print("the entered result is not valid")
            invalid_count+=1
if invalid_count >0:
    total_matches_count-=invalid_count
if total_matches_count >0:
    print(f"the total number of matches is:{total_matches_count}")
    print(f"the computer win ratio is: {(computer_win_count/total_matches_count)*100}")
    print(f"the user win ratio is: {(user_win_count/total_matches_count)*100}")
    print(f"match tie ratio is: {(tie_count/total_matches_count)*100}")
    print(f"the invalid ratio is: {(invalid_count/total_matches_count)*100}")
    if computer_win_count > user_win_count:
        print(f"the ultimate winner is computer out of {total_matches_count} times the computer has won {computer_win_count} times")
    elif user_win_count > computer_win_count:
        print(f"the ultimate winner is user out of {total_matches_count} times the user has won {user_win_count} times")
    else:
        print("Both are the winners")
else:
    print("no matches are played")