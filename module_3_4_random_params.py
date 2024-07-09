def single_root_words(root_words, *other_words):
    same_words = []
    for i in other_words:
        if root_words.lower() in i.lower() or i.lower() in root_words.lower():
            same_words.append(i)
    print(same_words)
    return same_words
single_root_words('Hi', 'kok', 'pop', 'I', 'hi', 'HI', 'Hi')
single_root_words('Intresting', 'kfdsa', 'ing', 'Intresting', 'rest', 'int')