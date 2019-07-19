letter_values_1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 80, 'g': 3, 'h': 8,
                       'i': 10, 'j': 10, 'k': 20, 'l': 30, 'm': 40, 'n': 50, 'o': 70, 'p': 80, 'q': 100,
                       'r': 200, 's': 300, 't': 400, 'u': 6, 'v': 6, 'w': 800, 'x': 60, 'y': 10, 'z': 7}

letter_values_2 = {"a": 6, "b": 12, "c": 18, "d": 24, "e": 30, "f": 36, "g": 42,
                       "h": 48, "i": 54, "j": 60, "k": 66, "l": 72, "m": 78, "n": 84, "o": 90, "p": 96,
                       "q": 102, "r": 108, "s": 114, "t": 120, "u": 126, "v": 132, "w": 138, "x": 144,
                       "y": 150, "z": 156}

def count_gematria(word, option):
    if option == 1:
        counts = []
        word = list(word)
        for i in word:
            if i in letter_values_1:
                counts.append(letter_values_1[i])
        print(sum(counts))
    else:
        counts2 = []
        word2 = list(word)
        for i in word2:
            if i in letter_values_2:
                counts2.append(letter_values_2[i])
        print(sum(counts2))

#count_gematria("Is my love", 1)
def decode(text):
    text = text.split("\n")
    list_of_chars = []
    not_words = []
    each_value = []
    counts = []
    loop = True
    while loop:
        option = input('Enter an option -> ')
        if int(option) == 1:
            for i in text:
                each_value = []
                list_of_chars =[]
                word_list = i.lower()
                for t in word_list:
                    if t.isalpha():
                        list_of_chars.append(t)
                    else:
                        not_words.append(t)
                for k in list_of_chars:
                    if k in letter_values_1:
                        each_value.append(letter_values_1[k])
                        loop = False
                    else:
                        print("I don't know this letter(")
                print(sum(each_value), ": ", i)
        elif int(option) == 2:
            for i in text:
                each_value = []
                list_of_chars = []
                word_list = i.lower()
                for t in word_list:
                    if t.isalpha():
                        list_of_chars.append(t)
                    else:
                        not_words.append(t)
                for k in list_of_chars:
                    if k in letter_values_1:
                        each_value.append(letter_values_2[k])
                        loop = False
                    else:
                        print("I don't know this letter(")
                print(sum(each_value), ": ", i)
        else:
            print("Please choose option 1 or 2")


decode("My dog is fast\nIs my love\ndog")







