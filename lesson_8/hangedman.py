import random

WORDS = ("МЕЧ", "МЯЧ", "ШОК", "КОЛ", "ВЕК", "ВУЗ", "БОГ")
word = random.choice(WORDS) 
tire = "-" * len(word)
wrong = 0 
used = [] 
max_wrong = 5


def start:
    print("Добро пожаловать в игру 'Виселица'!")
    while wrong < max_wrong and tire != word:
         print("\nНет такой буквы:\n", used)
    print("\nТвоё слово:\n", tire)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()

def check:
    if guess in word:
        print("\nДа! Буква", guess, "есть в слове!")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += tire[i]
        tire = new
    else:
        print("\nК сожалению, буквы", guess, "нет в слове.")
        wrong += 1

def used_letters:
    while guess in used:
        print("Вы уже предлагали букву: ", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
        used.append(guess)    


def end:
    if wrong == max_wrong:
    print("Вас повесили!")
else:
    print("\nВы отгадали!")
print("\nБыло загаданно слово", word, ".")

