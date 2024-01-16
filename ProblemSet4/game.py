import random
def main():
    level = input_level()
    play_game(level)


def play_game(level):
    random_number = random.randint(1,level)
    while True:
        guess = int(input("Guess: "))
        if guess < 0:
            continue
        if guess < random_number:
            print("Too small!")
        elif guess > random_number:
            print("Too large")
        else:
            print("Just right!")
            break

def input_level():
    while True:
        level = int(input("Level: "))
        if level > 0:
            return level
        
if __name__ == "__main__":
    main()