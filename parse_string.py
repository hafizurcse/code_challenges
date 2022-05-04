def parse_string(my_str:str) -> list:
    letters = ''.join(my_str.split('_'))
    words = []
    word = ''
    for letter in letters:
        if letter.isupper():
            if len(word) != 0:
                words.append(word)
            word = ''
            word += letter
        else:
            word += letter
    words.append(word)
    return words

my_str = "_GoodMorning_HelloWorld_"
print(parse_string(my_str)