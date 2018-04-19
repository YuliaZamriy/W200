user_string = input("Enter text string: ")

first_vowel = min([user_string.find(l) for l in "aeiou" if user_string.find(l) != -1])
vowel_count = len([l for l in user_string if l in "aeiou"])

if vowel_count == 0:
	print("No vowels")
elif first_vowel < len(user_string) - 1: 
	print("vowels:", vowel_count)
	print("first vowel:", user_string[first_vowel])
	print("character immediately after first vowel: ", user_string[first_vowel+1])
else:
	print("this vowel is the last letter of the string:", user_string[first_vowel])

