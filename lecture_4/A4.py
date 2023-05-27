def find_synonym(words: list, keyword: str) -> str:
    if not keyword:
        raise ValueError('There is no word to check')
    if not isinstance(keyword, str):
        raise TypeError('Use string format')
    words_dict = {}
    for word_pair in words:
        word1, word2 = word_pair.split()
        words_dict[word1], words_dict[word2] = word2, word1
    return words_dict[keyword]


if __name__ == '__main__':
    with open('input.txt', 'r') as reader:
        n_, *words_, keyword_ = reader.read().rstrip().split('\n')

    print(find_synonym(words_, keyword_))

    assert find_synonym(['hi bye', 'left right'], 'left') == 'right'
    assert find_synonym(['hi bye', 'left right'], 'right') == 'left'
