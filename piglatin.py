original = input("Enter your name: ")
blank = original.find(" ")
first_orig = original[0:blank]
last_orig = original[blank+1:]
first_pigl = first_orig[1].upper() + first_orig[2:].lower() + first_orig[0].lower() + "ay"
last_pigl = last_orig[1].upper() + last_orig[2:].lower() + last_orig[0].lower() + "ay"
print(first_pigl, last_pigl)