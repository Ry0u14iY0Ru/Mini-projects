"""
Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее.
рограмма должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить.
"""

from random import randint
from time import sleep

def magic_ball():
    decisions = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
                 "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
                 "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет",
                 "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

    while True:
        input('Введи вопрос, на который ты хочешь получить ответ: ')
        sleep(1)
        print('Магический шар говорит: ' + decisions[randint(0, len(decisions) - 1)])
        sleep(1)
        if input('Хочешь еще раз? Да? Нет? ').lower() in ['да', 'lf']:
            magic_ball()
        else:
            print('Возвращайся, я буду скучать!')
            break

def main():
    print("Привет, я магический шар!")
    print('Ты пишешь мне вопрос, а я отвечаю на него!')
    if input('Хочешь попробовать? Да? Нет? ').lower() in ['да', 'lf']:
        magic_ball()
    else:
        print('Возвращайся, я буду скучать!')

if __name__ == '__main__':
    main()