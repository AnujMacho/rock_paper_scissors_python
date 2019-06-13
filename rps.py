from random import choice
user_count = 0
comp_count = 0
winning_count = int(input("What's the winning score? "))
while user_count < winning_count and comp_count < winning_count:
    user_rps_list = input("What's your choice: \n")
    user_rps_list = user_rps_list.lower()
    if user_rps_list == "quit" or user_rps_list == "q":
        break
    comp_rps_list = choice(["rock", "paper", "scissor"])
    if user_rps_list == "rock" or user_rps_list == "paper" or user_rps_list == "scissor":
        if user_rps_list == comp_rps_list:
            print("Its a Draw, You both chose: " + user_rps_list)
        elif (user_rps_list == "rock" and comp_rps_list == "scissor") or (user_rps_list == "paper" and comp_rps_list == "rock") or (user_rps_list == "scissor" and comp_rps_list == "paper"):
            print(f"You Win {user_rps_list} beats {comp_rps_list}")
            user_count += 1
        else:
            print(f"Oops You lose {user_rps_list} beaten by {comp_rps_list}")
            comp_count += 1
    else:
        print("Enter correctly")

if user_count > comp_count:
    print("Congrats you win")
elif user_count < comp_count:
    print("Oops you loose")
else:
    print("It's a tie")
print(f"Final Scores User Score: {user_count} and Computer Score: {comp_count}")
