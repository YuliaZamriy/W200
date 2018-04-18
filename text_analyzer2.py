user_string = input("Enter text string: ")
vowels = "aeiou"

vowel_dict = {}

for v in vowels:
	vowel_dict[v] = user_string.count(v)

print(vowel_dict)