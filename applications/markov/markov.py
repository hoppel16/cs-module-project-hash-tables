import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
markov_chain = {}
words_list = words.split()

for index in range(0, len(words_list) - 1):
    is_sentence_end = False
    if index + 1 >= len(words_list):
        break

    clean_word = words_list[index].lower()
    if not clean_word.islower():
        continue
    while not clean_word[0].isalnum():
        clean_word = clean_word.replace(clean_word[0], "")
    while not clean_word[-1].isalnum():
        if clean_word[-1] in ".!?":
            is_sentence_end = True
            break
        clean_word = clean_word.replace(clean_word[-1], "")

    if is_sentence_end:
        continue

    if words_list[index] not in markov_chain:
        markov_chain[clean_word] = []

    clean_next_word = words_list[index+1].lower()
    if not clean_next_word.islower():
        continue
    while not clean_next_word[0].isalnum():
        clean_next_word = clean_next_word.replace(clean_next_word[0], "")
    while not clean_next_word[-1].isalnum():
        if clean_next_word[-1] in ".!?":
            break
        clean_next_word = clean_next_word.replace(clean_next_word[-1], "")

    markov_chain[clean_word].append(clean_next_word)

# TODO: construct 5 random sentences
for x in range(5):
    sentence_list = []

    starting_word = random.choice(list(markov_chain.keys()))
    sentence_list.append(starting_word.capitalize())
    next_word = starting_word
    while next_word[-1].isalnum():
        next_word = random.choice(markov_chain[next_word])
        sentence_list.append(next_word)

    sentence = " ".join(sentence_list)

    print(sentence)
