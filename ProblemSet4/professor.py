import random


def main():
    score = play_game()
    print("Score:",score)
    
def play_game():
    i = 0
    score = 10
    level = get_level()
    generate_new_number = True
    number_of_false_ans = 0
    while i < 10:
        if number_of_false_ans == 3:
            score-=1
            print(f"{num1} + {num2} = {num1+num2}")
            number_of_false_ans = 0
            generate_new_number =True
            i+=1
            continue
        if generate_new_number == True:
            num1 =generate_integer(level)
            num2 = generate_integer(level)
        try:
            sum = int(input(f"{num1} + {num2} = "))
        except ValueError:
            print("EEE")
            generate_new_number = False
            number_of_false_ans +=1
            continue
        if sum != num1+num2:
            print("EEE")
            generate_new_number = False
            number_of_false_ans +=1
        else:
            generate_new_number = True
            number_of_false_ans = 0
            i+=1
    return score

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
        except ValueError:
            pass


def generate_integer(level):
    return random.randint((10** (level-1)),(10 ** level) -1)


if __name__ == "__main__":
    main()
