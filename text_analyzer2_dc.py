user_string = input("Enter text string: ")

vowel_dict = {v:user_string.count(v) for v in "aeiou"}

print(vowel_dict)