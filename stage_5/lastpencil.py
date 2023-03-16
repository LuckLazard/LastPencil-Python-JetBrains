import random

global user_count

print("How many pencils would you like to use:")
def question_player():
    global user_count
    try:
        user_count = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        question_player()
    else:
        if user_count > 0:
            print("Who will be the first (John, Jack): ")
            first_player()
        elif user_count == 0:
            print("The number of pencils should be positive")
            question_player()
        else:
            question_player()
def first_player():
    global user_first
    user_first = input()
    if user_first != "John" and user_first != "Jack":
        print("Choose between 'John' and 'Jack'")
        first_player()
    if user_first == "John" or user_first == "Jack":
        game_pencil()
def game_pencil():
    while user_count > 0:
        if user_first == "John":
            if user_count > 0:
                print("|" * user_count)
                print(f"John's turn:")
                player_john()
        if user_first == "Jack":
            if user_count > 0:
                print("|" * user_count)
                print(f"Jack's turn:")
                player_jack()
def player_john():
    global user_count
    try:
        user_john = int(input())
    except ValueError:
        print("Possible values: '1', '2' or '3'")
        player_john()
    else:
        if user_john <= user_count:
            if user_john == 1 or user_john == 2 or user_john == 3:
                user_count -= user_john
                if user_count >= 1:
                    print("|" * user_count)
                    print(f"Jack's turn:")
                    player_jack()
                elif user_count  == 0:
                    print("Jack won!")
                    exit()
            else:
                print("Possible values: '1', '2' or '3'")
                print("|" * user_count)
                player_john()
        elif user_john > user_count:
            if user_john == 1 or user_john == 2 or user_john == 3:
                print("Too many pencils were taken")
                player_john()
            else:
                print("Possible values: '1', '2' or '3'")
                print("|" * user_count)
                player_john()
        elif user_count == 0:
            print("Jack won!")
            exit()
def player_jack():
    global user_count
    if user_count > 1:
        if user_count == 4 or user_count > 4 and user_count % 4 == 0:
            print("3")
            user_count -= 3
            print("|" * user_count)
            print(f"John's turn!:")
            player_john()
        elif user_count == 3 or (user_count + 4) - user_count == 4 and user_count % 2 != 0:
            print("2")
            user_count -= 2
            print("|" * user_count)
            print(f"John's turn!:")
            player_john()
        elif user_count == 2 or user_count > 2 and user_count % 2 == 0:
            print("1")
            user_count -= 1
            print("|" * user_count)
            print(f"John's turn!:")
            player_john()
        elif user_count % 4 != 0 and user_count % 3 != 0 and user_count % 2 != 0 and user_count % 7 != 0 and user_count > 0:
            random_number = (random.randint(1, 3))
            user_count -= random_number
            if user_count > 1:
                print(random_number)
                print("|" * user_count)
                print(f"John's turn!:")
                player_john()
            elif user_count == 1:
                print(random_number)
                print("John won!")
                exit()
    elif user_count == 1:
            print("1")
            user_count -= 1
            print("John won!")
            exit()

question_player()