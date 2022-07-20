import random

# possible error messages for the program
non_numeric_error = "The number of pencils should be numeric"
zero_pencils_error = "The number of pencils should be positive"
proper_name_error = "Choose between Neo and Max"
possible_values_error = "Possible values: '1', '2' or '3'"
not_enough_pencils_error = "Too many pencils were taken"

while True:
    print("How many pencils?")
    no_of_pencils = input() 

    try:
        no_of_pencils = int(no_of_pencils)

        if no_of_pencils == 0:
            print(zero_pencils_error)
            continue
        elif no_of_pencils < 0:
            print(non_numeric_error)
            continue

        # break out of loop if user enters correct value for pencils
        break
    except:
        print(non_numeric_error)


while True:
    print("Who will be the first (Bob, Neo):")
    person_turn = input()

    # continue asking for proper name input
    if person_turn not in ["Bob", "Neo"]:
        print(proper_name_error)
        continue
    
    # break out if name is proper
    break

while no_of_pencils >= 1:
    print("|" * no_of_pencils)
    print(person_turn, "turn:")

    if person_turn == "Neo":
        if no_of_pencils == 1:  # corner case of 1
            no_of_pencils -= 1
            print("1")

        elif (no_of_pencils - 1) % 4 == 0:  # losing position 1,5,9,13.....
            number_random = random.randint(1,3)
            print(number_random)
            no_of_pencils -= number_random
            
        else:  # winning position
            if no_of_pencils % 4 == 2:
                winning_chosen = 1
            if no_of_pencils % 4 == 3:
                winning_chosen = 2
            if no_of_pencils % 4 == 0:
                winning_chosen = 3 
            print(winning_chosen)
            no_of_pencils -= winning_chosen
            


    else:
        pencil_taken_out = input()
        if pencil_taken_out not in ["1", "2", "3"]:
            print(possible_values_error)
            continue  # continue asking for possible values of pencils

        pencil_taken_out = int(pencil_taken_out)  # converting into int

        if pencil_taken_out > no_of_pencils:
            print(not_enough_pencils_error)
            continue  # continue asking for pencils take out if it exceed remaining pencil

        no_of_pencils -= pencil_taken_out  # subtract the pencil taken out

    # switching turns
    if person_turn == "Bob":
        person_turn = "Neo"
    else:
        person_turn = "Bob"

    # That person wins who doesn't takes the last pencil
    if no_of_pencils == 0:
        print(person_turn, "won!")

