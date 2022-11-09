word_whithout_vowels = ""
user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
    if letter in "AEIOU":
        continue
    word_whithout_vowels += letter

print(word_whithout_vowels)