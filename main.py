import json
import random


def print_statistics(answers: list):
    """
    Функция вывода в консоль итогов
    """
    print(f"\nВсего задачек: {len(answers)}\n"
          f"Отвечено верно: {answers.count(True)}\n"
          f"Отвечено неверно: {answers.count(False)}\n")


def load_morse_code():
    """
    Функция парсинга json-файла с морзянкой
    """

    with open('morse-code.json') as file:
        return json.loads(file.read())


def morse_encode(word, morse_dict):
    """
    Функция перевода слова на английском языке в последовательности точек и тирe
    """
    morse_word_list = []

    for symbol in word:
        morse_word_list.append(morse_dict[symbol])
    return "".join(morse_word_list)


def get_word(words_list):
    """
    Получение рандомного слова из списка слов
    """
    return str(random.choice(words_list))


def run():
    """
    Функция запуска игры
    """
    answers = []
    words_list = ["code", "bit", "list", "soul", "next"]
    morse_dict = load_morse_code()

    print("Сегодня мы потренируемся расшифровывать морзянку.\nНажмите Enter и начнем")
    input()

    for iterator in range(1, 6):
        word = get_word(words_list)

        print(f"Слово {iterator} - {morse_encode(word, morse_dict)}")
        response = input("Ввод: ")

        if response == word:
            answers.append(True)
            print(f"Верно, {word.title()}!")
        else:
            answers.append(False)
            print(f"Неверно, {word.title()}!")

    print_statistics(answers)


def main():
    """
    Просто main-функция
    """
    run()


main()
