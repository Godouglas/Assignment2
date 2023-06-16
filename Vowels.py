Sentence = str(input("Enter sentence:"))
Vowels = ["a", "e", "i", "o", "u", "A", "E", "O", "I", "U",]
for char in Sentence:
    if char in Vowels:
        Sentence = Sentence.replace(char, "")
print(Sentence)