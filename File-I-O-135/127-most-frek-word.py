from collections import Counter,defaultdict
print(repr(print))
freq = {}

with open("textfile.txt") as f:
    for line in f:
        for word in line.lower().split():
            freq[word] = freq.get(word, 0) + 1

rev = defaultdict(list)

for word, count in freq.items():
    rev[count].append(word)

max_count = max(rev)

print("Most frequent count:", max_count)
print("Words:", rev[max_count])
#1️⃣ Word Frequency Counter
with open("textfile.txt") as f:
    freq = {}

    for line in f:
        for word in line.lower().split():
            word = word.strip(".,!?;:\"'")
            freq[word] = freq.get(word, 0) + 1

print(freq)
#2️⃣ Find the Longest Word
longest = ""

with open("textfile.txt") as f:
    for line in f:
        for word in line.split():
            word = word.strip(".,!?;:\"'")
            if len(word) > len(longest):
                longest = word

print("Longest word:", longest)
print("Length:", len(longest))
#3️⃣ Detect Palindromes in a File

with open("textfile.txt") as f:
    for line in f:
        for word in line.split():
            w = word.lower().strip(".,!?")
            if len(w) > 2 and w == w[::-1]:
                print("Palindrome:", w)
#duplicate
seen = set()
duplicates = set()

with open("textfile.txt") as f:
    for line in f:
        if line in seen:
            duplicates.add(line)
        else:
            seen.add(line)

print("Duplicate lines:")
for d in duplicates:
    print(d)