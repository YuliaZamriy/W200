user_string = input("Enter text string: ")
vowels = "aeiou"

vowel_count = 0
vowel_index = []

for l in user_string.lower():
	if l in vowels:
		vowel_index.append(user_string.index(l))
		vowel_count += 1

if not vowel_index:
	print("No vowels")
else: 
	print("vowels:", vowel_count)
	print("first vowel:", user_string[vowel_index[0]])
	print("character immediately after first vowel: ", user_string[vowel_index[0]+1])
