with open("robin.txt") as f:
    words = f.read()

cache = {}

for word in words.split():
    word = word.lower()
    if not word.islower():
        continue
    word = ''.join(e for e in word if e.isalnum())

    if word not in cache:
        cache[word] = 0
    cache[word] += 1

sorted_cache = sorted(cache.items(), key=lambda x: x[1], reverse=True)

for word in sorted_cache:
    print(f"{word[0]}".ljust(20) + ("#" * word[1]))
