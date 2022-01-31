import random


score = []


def gen_num():
    """vraci vygenerovane cislo v podobe ctyrmistneho listu"""
    num = list("0000")
    i = 0
    while i < len(num):
        if i == 0:
            num[i] = int(random.randint(1, 9))
            i += 1
        else:
            num[i] = int(random.randint(0, 9))
            if num[i] in num[0:i]:
                continue
            else:
                i += 1
    return num


def user_input():
    """ vraci cislo zadane uzivatelem v podobe ctyrmistneho listu"""
    guess = []
    while True:
        repeat = False
        print("-" * 47)
        guess_str = input("Enter a number: ")
        for i, char in enumerate(guess_str):
            if guess_str[i] in guess_str[0:i]:
                repeat = True
        if (repeat == False and len(guess_str) == 4 and guess_str.isnumeric()
                and not guess_str.startswith("0")):
            guess = [int(_) for _ in list(guess_str)]
            return guess
        else:
            print("Please try again")


def evaluation_bull(guess, num):
    """bere vygenerovane cislo a vstup od uzivatele, vraci pocet bull"""
    bull = 0
    for i, nb in enumerate(num):
        if guess[i] == num[i]:
            bull += 1
    return bull


def evaluation_cow(guess, num):
    """bere vygenerovane cislo a vstup od uzivatele, vraci pocet cow"""
    cow = 0
    for i in num:
        if str(i) in str(guess):
            cow += 1
    return cow


def plural(pocet):
    """bere pocet bull/cow a vraci 's' pro mnozne cislo"""
    return "s" if pocet > 1 else ""


def plural_es(pocet):
    """bere pocet pokusu a vraci 'es' pro mnozne cislo guesses"""
    return "es" if int(pocet) > 1 else ""


def ranking(number):
    """bere pocet pokusu nez uzivatel uhodl cislo a
    vraci vyhodnoceni pro vypis"""
    if number < 5:
        return "amazing"
    elif number < 10:
        return "great"
    elif number < 15:
        return "average"
    else:
        return "not so good"


def play_again():
    while True:
        again = input("New game? (y / n): ")
        if again.lower() == "y":
            main()
        elif again.lower() == "n":
            vypsani_vysledku()
            quit()
        else:
            print("Try again")


def vypsani_vysledku():
    line = "-" * 23
    print(line)
    for index, pokusy in enumerate(score):
        print(f"| {index+1}. game | {pokusy} guess{plural_es(pokusy)} |")
    print(line)
    print("See you later!")


def main():
    pozdrav = """      
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game."""

    global score
    guesses = 0
    print(pozdrav)
    cislo = gen_num()
    while True:
        guesses += 1
        tip = user_input()
        byk = evaluation_bull(tip, cislo)
        krava = evaluation_cow(tip, cislo)
        if tip == cislo:
            print("-" * 47)
            print(f"congrats! You guessed right number in {guesses} guess{plural_es(guesses)}.")
            print(f"That's {ranking(guesses)}!")
            print("-" * 47)
            score.append(str(guesses))
            play_again()
        else:
            print(f"{byk} bull{plural(byk)}, {krava-byk} cow{plural(krava-byk)}")


main()
