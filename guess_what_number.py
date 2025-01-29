"""
Описание проекта: программа генерирует случайное число в диапазоне от 1 до 100
и просит пользователя угадать это число. 
Если догадка пользователя больше случайного числа, то программа должна вывести сообщение 'Слишком много, попробуйте еще раз'. 
Если догадка меньше случайного числа, то программа должна вывести сообщение 'Слишком мало, попробуйте еще раз'. 
Если пользователь угадывает число, то программа должна поздравить его и вывести сообщение 'Вы угадали, поздравляем!'.
"""

from random import *
from time import *

def is_valid(arg):
    return arg.isdigit()

def game_rules():
    print('Отлично! Давай ознакомлю тебя с правилами игры.')
    print('Я загадаю число, а ты будешь его отгадывать.')
    print('Диапазон чисел у нас от 1 до 100.')

def guess_what_number():
    phrases_too_much = ['Ох, слишком много! Попробуй еще раз', 'Многовато будет!', 'Ого-го, это слишком много!',
                        'Много!', 'Бери ниже', 'Многовато!', 'Нужно меньшее число!']
    phrases_too_little = ['Ох, слишком мало! Попробуй еще раз', 'Маловато будет!', 'Эх, это слишком мало!',
                          'Мало!', 'Бери выше', 'Маловато!', 'Нужно большее число!']
    phrases_almost = ['Почти угадал!', 'Горячо, но не очень', 'Уже рядом', 'Ты близок', 'Ты уже рядом', 'Ну же, почти',
                      'Горячо!']
    phrases_guessed = ['Поздравляю! Ты угадал моё число :)', 'Молодец! Ты угадал :)', 'Ура, ты угадал! :)']
    phrases_too_soon = ['Ого, так быстро!', 'Да ты волшебник! Ты угадал моё число', 'Скажи честно, ты подглядывал?',
                        'У тебя отличная интуиция!', 'Даже я бы не смог отгадать так быстро!']

    num_0 = randint(1, 100)
    cnt = 0
    print('Я загадал число от 1 до 100 :)')
    print('Попробуй отгадать его')
    sleep(2)
    while True:
        num = input('Введи число: ')
        if not is_valid(num):
            print('Дурачек, я же говорил, что надо вводить только числа.')
            print('Я не буду с тобой играть :(')
            break
        else:
            cnt += 1
            if num_0 > int(num):
                if abs(num_0 - int(num)) < 5:
                    print(choice(phrases_too_little), choice(phrases_almost), sep='\n')
                else:
                    print(choice(phrases_too_little))
            elif num_0 < int(num):
                if abs(num_0 - int(num)) < 5:
                    print(choice(phrases_too_much), choice(phrases_almost), sep='\n')
                else:
                    print(choice(phrases_too_much))
            elif num_0 == int(num):
                if cnt == 1:
                    print('Ты читер? Как ты это сделал???')
                    sleep(1)
                    if input('Хочешь сыграть еще раз? Да? Нет? ').lower() in ['да', 'lf']:
                        guess_what_number()
                    else:
                        print('Возвращайся, я буду скучать!')
                        break
                elif 1 < cnt <= 5:
                    print(choice(phrases_too_soon))
                    sleep(1)
                    if input('Хочешь сыграть еще раз? Да? Нет? ').lower() in ['да', 'lf']:
                        guess_what_number()
                    else:
                        print('Возвращайся, я буду скучать!')
                        break
                else:
                    print(choice(phrases_guessed))
                    sleep(1)
                    if input('Хочешь сыграть еще раз? Да? Нет? ').lower() in ['да', 'lf']:
                        guess_what_number()
                    else:
                        print('Возвращайся, я буду скучать!')
                        break

def main():
    print('Привет! Я - игра "Угадай число".')
    sleep(0.5)
    if input('Хочешь сыграть? Да? Нет? ').lower() in ['да', 'lf']:
        game_rules()
        sleep(5)
        guess_what_number()
    else:
        print('Ну и не надо!')

if __name__ == '__main__':
    main()