import re


def word_counter(text: str) -> int:
    if text:
        text_split = re.split('[\n ]+', text)
        return len(set(text_split))
    else:
        return 0


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        text_ = reader.read().rstrip()

    print(word_counter(text_))
