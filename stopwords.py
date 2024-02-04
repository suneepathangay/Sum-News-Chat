import string

#

def get_stopwords():
    with open('stopwords.txt', 'r') as file:
        file_contents = file.read()


    words = file_contents.split()

    translator = str.maketrans('', '', string.punctuation)
    words = [word.translate(translator) for word in words]

    words = list(filter(None, words))

    return words
