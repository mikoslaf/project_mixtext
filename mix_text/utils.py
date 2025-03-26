import random

def mix_middle_letters(word: str) -> str:
    if len(word) <= 3:
        return word

    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = list(word[1:-1])

    random.shuffle(middle_letters)
    return first_letter + ''.join(middle_letters) + last_letter

def process_file_content(file_content: str) -> list:
    words = []
    for line in file_content.split('\n'):
        for word in line.split():
            words.append(mix_middle_letters(word))
    return words