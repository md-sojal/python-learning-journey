word = [100]
word = input("Write you words ").lower()
i = 0
vowel_count = 0
consonant_count = 0
for letter in word:
    if letter in "aeiou":
        vowel_count += 1
    elif letter.isalpha():
        consonant_count += 1
print(f"Total number of vowel is {vowel_count}")
print(f"Total number of consonant is {consonant_count}")