def findWordsContaining(words, x):
    array = []
    for i in range(len(words)):
        if x in words[i]:
            array.append(i)
        else:
            continue
    


findWordsContaining(["leet","code"], "e")