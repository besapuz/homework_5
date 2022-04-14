import random
#nkdjnd
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
    " ": "/"
}

print('Сегодня мы потренируемся расшифровывать азбуку Морзе\nНажмите Enter и начнем')
input()

words = [
    'good morning',
    'new',
    'young',
    'free',
    'open'
]
answers = []
total = 0


def get_word():
    return random.choice(words)  # случайное слово из списка words


def morse_encode(word):
    """Функция перевода случайных английских слов в азбуку Морзе"""
    word_list = []
    for letter in word:
        word_list.append(morse[letter])
    return word_list


def print_statistics(correct=0, wrong=0):
    """Подстчет правильных и не правильных ответов"""
    for a in answers:
        if a:
            correct += 1
        elif not a:
            wrong += 1
    return f'Отвечено верно: {correct}\nОтвечено неверно: {wrong}'


while total < len(words):       # основной блок программы
    word_random = get_word()
    word_morse = morse_encode(word_random)
    total += 1

    print(f'Слово {total} {" ".join(word_morse)}')      # выводит случайоное слово переведенное в азбуку Морзе

    answer_morse = input()

    if answer_morse == word_random:
        answers.append(True)
        print(f'Верно, {word_random.capitalize()}!')
    else:
        answers.append(False)
        print(f'Не верно, {word_random.capitalize()}!')

print(f'Всего задачек: {total}\n{print_statistics()}')
