import random

print('\t\tВас приветствует игра "угадай число"')
print("\t\tПравила игры- угадай число от 1 до 100. Поехали!")

number = random.randint(1,100)
guess = int(input("\nНу попробуй: "))
tries = 1
while guess != number:
    if guess < number:
        print("Больше. Пробуй снова")            # В этой строке не хватало отступа
    else:
        print("Меньше. Пробуй снова")
    guess = int(input("\nПробуй снова: "))       # Ещё в этой
    tries += 1                                   # И в этой

print("\n\nТы угадал!")
print("Тебе удалось угадать за ", tries," попыток")

input("\n\nНажми Enter чтобы выйти")
