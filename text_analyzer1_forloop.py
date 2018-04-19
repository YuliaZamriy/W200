user_string = input("Enter text string: ")
vowels = "aeiou"

vowel_count = 0
first_vowel = -1

for l in user_string.lower():
	if l in vowels:
		if first_vowel == -1:
			first_vowel = user_string.index(l)
		vowel_count += 1

if vowel_count == 0:
	print("No vowels")
elif first_vowel < len(user_string) - 1: 
	print("vowels:", vowel_count)
	print("first vowel:", user_string[first_vowel])
	print("character immediately after first vowel: ", user_string[first_vowel+1])
else:
	print("this vowel is the last letter of the string:", user_string[first_vowel])

