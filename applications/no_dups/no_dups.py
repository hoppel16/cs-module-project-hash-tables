def no_dups(s):
    s.strip()
    words = {}

    clean_sentence_list = []

    for word in s.split():
        if word in words:
            words[word] += 1
            continue
        words[word] = 1
        clean_sentence_list.append(word)

    return " ".join(clean_sentence_list)



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))