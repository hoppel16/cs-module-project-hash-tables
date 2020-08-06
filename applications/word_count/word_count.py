def word_count(s):
    words = {}

    for word in s.split():
        word = word.lower()

        if not word.islower():
            continue

        while not word[0].isalnum():
            word = word.replace(word[0], "")

        while not word[-1].isalnum():
            word = word.replace(word[-1], "")

        if word not in words:
            words[word] = 0

        words[word] += 1

    return words



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
