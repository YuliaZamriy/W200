user_string = input("Enter text string: ")
vowels = "aeiou"

vowel_count = 0
first_vowel = len(user_string) + 1

if "a" in user_string.lower():
	first_vowel = min(first_vowel,user_string.lower().find("a"))
	vowel_count += user_string.lower().count("a")
if "e" in user_string.lower():
	first_vowel = min(first_vowel,user_string.lower().find("e"))
	vowel_count += user_string.lower().count("e")
if "i" in user_string.lower():
	first_vowel = min(first_vowel,user_string.lower().find("i"))
	vowel_count += user_string.lower().count("i")
if "o" in user_string.lower():
	first_vowel = min(first_vowel,user_string.lower().find("o"))
	vowel_count += user_string.lower().count("o")
if "u" in user_string.lower():
	first_vowel = min(first_vowel,user_string.lower().find("u"))
	vowel_count += user_string.lower().count("u")

if vowel_count == 0:
	print("No vowels")
elif first_vowel < len(user_string) - 1: 
	print("vowels:", vowel_count)
	print("first vowel:", user_string[first_vowel])
	print("character immediately after first vowel: ", user_string[first_vowel+1])
else:
	print("this vowel is the last letter of the string:", user_string[first_vowel])

